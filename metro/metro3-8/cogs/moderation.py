import discord
from discord.ext import commands, tasks
import platform
import datetime

import utils.json_loader
from utils.mongo import Document
from discord.ext.commands.cooldowns import BucketType
import asyncio
from copy import deepcopy
import re
from dateutil.relativedelta import relativedelta

import random

time_regex = re.compile("(?:(\d{1,5})(h|s|m|d))+?")
time_dict = {"h": 3600, "s": 1, "m": 60, "d": 86400}



class TimeConverter(commands.Converter):
    async def convert(self, ctx, argument):
        args = argument.lower()
        matches = re.findall(time_regex, args)
        time = 0
        for key, value in matches:
            try:
                time += time_dict[value] * float(key)
            except KeyError:
                raise commands.BadArgument(
                    f"{value} is an invalid time key! h|m|s|d are valid arguments"
                )
            except ValueError:
                raise commands.BadArgument(f"{key} is not a number!")
        return round(time)

class Moderation(commands.Cog):

	def __init__(self, bot):
		self.bot = bot
		self.mute_task = self.check_current_mutes.start()

	def cog_unload(self):
		self.mute_task.cancel()

	@commands.Cog.listener()
	async def on_ready(self):
		print(f"{self.__class__.__name__} Cog has been loaded\n-----")



	@tasks.loop(minutes=5)
	async def check_current_mutes(self):
		currentTime = datetime.datetime.now()
		mutes = deepcopy(self.bot.muted_users)
		for key, value in mutes.items():
			if value['muteDuration'] is None:
				continue

			unmuteTime = value['mutedAt'] + relativedelta(seconds=value['muteDuration'])

			if currentTime >= unmuteTime:
				guild = self.bot.get_guild(value['guildId'])
				member = guild.get_member(value['_id'])


				role = discord.utils.get(guild.roles, name="Muted")

				if role in member.roles:
					await member.remove_roles(role)

					print(f"Unmuted: {member.display_name}")

					await self.bot.mutes.delete(member.id)

				try:
					self.bot.muted_users.pop(member.id)

				except KeyError:
					pass




	@check_current_mutes.before_loop
	async def before_check_current_mutes(self):
		await self.bot.wait_until_ready()

		
	@commands.command()
	@commands.cooldown(rate=1, per=3, type=commands.BucketType.user)
	@commands.has_guild_permissions(mute_members=True)
	async def mute(self, ctx, member: discord.Member, time: TimeConverter=None, *, reason=None):
	
		
	
		if member == ctx.author:
			await ctx.send("You cannot mute yourself")
			return

		guild = ctx.guild

		data = await self.bot.config.get_by_id(ctx.message.guild.id)
		prefix = data["prefix"]

		mutedRole = discord.utils.get(guild.roles, name="Muted")
		role1 = discord.utils.get(member.guild.roles, name = "Muted")

		error = discord.Embed(title='Error!',description='This member is a **mod/admin.** I cannot mute them.',color=0xFFA500)
		alr_muted = discord.Embed(title='User already Muted!',description=f'The user is already muted! Use ``{prefix}unmute <member>`` to unmute them',color=0xFFA500)


		msg_member = discord.Embed(title='Muted!',description=f"You were muted in **{guild}**! \n**Time:** None (the person who muted you didn't specify a time) \n**Reason:** {reason}", color=0xff0000)
		msg_channel= discord.Embed(title='Sucess!',description=f'You muted {member.mention}! \n\n**Time:** None (member is muted until someone unmutes him/her) \n**Reason:** {reason}', color=0x00FF00)	

		msg_channel2= discord.Embed(title='Sucess!',description=f'You muted {member.mention}! \n\n**Time:** None (member is muted until someone unmutes him/her) \n**Reason:** {reason} \n**Note:** I could not DM them but they are indeed Muted', color=0x00FF00)
		
		if member.guild_permissions.manage_guild or member.guild_permissions.administrator:
			await ctx.send(embed=error)
			return
			
		if not mutedRole:
			mutedRole = await guild.create_role(name = "Muted")
			await ctx.send('im creating a mute role since it has not been setup yet do not change the name of it')

			for channel in guild.channels:
				await channel.set_permissions(mutedRole, speak=False, send_messages=False)



		if role1 in member.roles:
			await ctx.send(embed=alr_muted)
			return
		
		try:
			for channel in guild.channels:
				await channel.set_permissions(mutedRole, speak=False, send_messages=False)
				
		except: 
			raise error
		

		data = {'_id': member.id,'mutedAt': datetime.datetime.now(),'muteDuration': time or None,'mutedBy': ctx.author.id,'guildId': ctx.guild.id, 'reason': reason}



		await self.bot.mutes.upsert(data)

		self.bot.muted_users[member.id] = data


		await member.add_roles(mutedRole)

		if not time:
			try:
				await member.send(embed=msg_member)
				await ctx.send(embed=msg_channel)

			except:
				await ctx.send(embed=msg_channel2)

		else:
			minutes, seconds = divmod(time, 60)
			hours, minutes = divmod(minutes, 60)

			if int(hours):
				hours = discord.Embed(title='Muted!',description=f'You were muted in **{guild}**! \n **Time:** {hours} hours \n**Reason:** {reason}', color=0xff0000)
				hours_channel= discord.Embed(title='Sucess!',description=f'You muted {member.mention} \n\n **Time:** {hours} hours \n**Reason:** {reason}', color=0x00FF00)
				hours_channel.set_footer(text=f'Use {prefix}unmute <member> to unmute someone')

				hours_no_dm =  discord.Embed(title='Sucess!',description=f'You muted {member.mention} \n\n **Time:** {hours} hours  \n**Reason:** {reason} \n**Note:** I could not DM them but they are indeed Muted', color=0x00FF00)

				try:
					await member.send(embed=hours)
					await ctx.send(embed=hours_channel)

				except:
					await ctx.send(embed=hours_no_dm)

			elif int(minutes):
				mins = discord.Embed(title='Muted!',description=f'You were muted in **{guild}**! \n **Time:** {minutes} minutes \n**Reason:** {reason}', color=0xff0000)
				mins_channel = discord.Embed(title='Sucess!',description=f'You muted {member.mention} \n\n **Time:** {minutes} minutes \n**Reason:** {reason}', color=0x00FF00)
				mins_channel.set_footer(text=f'Use {prefix}unmute <member> to unmute someone')

				mins_no_dm =  discord.Embed(title='Sucess!',description=f'You muted {member.mention} \n\n **Time:** {minutes} minutes  \n**Reason:** {reason} \n**Note:** I could not DM them but they are indeed Muted', color=0x00FF00)

				try:
					await member.send(embed=mins)
					await ctx.send(embed=mins_channel)

				except:
					await ctx.send(embed=mins_no_dm)

			elif int(seconds):
				sec = discord.Embed(title='Muted!',description=f'You were muted in **{guild}**! \n **Time:** {seconds} seconds \n**Reason:** {reason}', color=0xff0000)
				sec_channel = discord.Embed(title='Sucess!',description=f'You muted {member.mention} \n\n **Time:** {seconds} seconds \n**Reason:** {reason}', color=0x00FF00)
				sec_channel.set_footer(text=f'Use {prefix}unmute <member> to unmute someone')
				
				sec_no_dm =  discord.Embed(title='Sucess!',description=f'You muted {member.mention} \n\n **Time:** {seconds} seconds  \n**Reason:** {reason} \n**Note:** I could not DM them but they are indeed Muted', color=0x00FF00)

				try:
					await member.send(embed=sec)
					await ctx.send(embed=sec_channel)

				except:
					await ctx.send(embed=sec_no_dm)


		if time and time < 300:
			await asyncio.sleep(time)

			if mutedRole in member.roles:

				after_mute	= discord.Embed(title='Unmuted!',description=f'You were unmuted in **{guild}** because your mute ended',color=0x00FF00)

				await member.remove_roles(mutedRole)
				await member.send(embed=after_mute)

				await self.bot.mutes.delete(member.id)

			try:
				self.bot.muted_users.pop(member.id)

			except KeyError:
				pass

	@commands.command()
	@commands.has_guild_permissions(manage_roles=True)
	async def unmute(self, ctx, member : discord.Member, *, reason=None):

		data = await self.bot.config.get_by_id(ctx.message.guild.id)
		prefix = data["prefix"]

		guild = ctx.guild

		await self.bot.mutes.delete(member.id)

		try:
			self.bot.muted_users.pop(member.id)

		except KeyError:
			pass
		
		role = discord.utils.get(member.guild.roles, name = "Muted")
		mutedRole = discord.utils.get(member.roles, name="Muted")

		

		if role not in member.roles:
			not_muted = discord.Embed(title='Error!', description=f"This person isn't even muted! Use ``{prefix}mute <member> (time) (reason)`` to muted someone!",color=0xFFA500)

			await ctx.send(embed=not_muted)
			return

		if not mutedRole:
			not_setup = discord.Embed(title='No Muted Role detected!',description=f'Please do **not** change the name of the role. Run ``{prefix}mute <member> (reason)`` to mute this person again and setup a Muted Role!',color=0xFFA500)

			await ctx.send(embed=not_setup)
			return


		msg_channel = discord.Embed(title='Sucess!',description=f'You unmuted {member.mention}! \n**Reason:** {reason}',color=0x00FF00)
		msg_member	= discord.Embed(title='Unmuted!',description=f'You were unmuted in **{guild}**! \n**Reason:** {reason}) \n**Note:** Your mute was ended early because {ctx.author.mention} unmuted you',color=0x00FF00)

		await member.remove_roles(role)
		await ctx.send(embed=msg_channel)

		await member.send(embed=msg_member)

	@commands.command(aliases=['clear', 'clearmessages'])
	@commands.guild_only()
	@commands.has_guild_permissions(manage_messages=True)
	async def purge(self, ctx, amount=0):

			if amount >= 1001:
				embed = discord.Embed(title='Error!',description=f'Too many messages! 1000 messages max - ({amount}/1000)',color=0xE74C3C)
				embed.set_footer(text='This message will delete in 3 seconds')
				
				message = await ctx.send(f'{ctx.author.mention}',embed=embed)

				await asyncio.sleep(3)
				await message.delete()

				return

			if amount >= 1:
				perfect = discord.Embed(title='Sucess!',description=f'I sucessfully deleted/purged {amount} message(s)',color=0x2ECC71)
				perfect.set_footer(text='This message will delete in 3 seconds')

				await ctx.channel.purge(limit=amount+1)

				message2 = await ctx.send(embed=perfect)

				await asyncio.sleep(3)
				await message2.delete()
				return

			else:
				data = await self.bot.config.get_by_id(ctx.message.guild.id)
				prefix = data["prefix"]

				description = discord.Embed(title='Purge Command',description=f'**Aliases:** clear, clearmessages \n**Cooldown:** 3 seconds \n**Description:** Deletes a set amount of messages \n**Usage:** {prefix}purge <amount> \n**Examples:** \n{prefix}purge 100 \n{prefix}clear 10 \n{prefix}clear 2',color=0xE67E22)
				description.set_footer(text='Objects in <> are required and objects in () are optional')

				await ctx.send(embed=description)
				
	@purge.error
	async def purge_error(self, ctx, error):
	
		if isinstance(error, commands.BadArgument):
		
			await ctx.send('Converting to "int" failed for parameter "amount"')

	@commands.command(aliases=['repeat','repeatthis','copyme'])
	@commands.cooldown(rate=1, per=3, type=commands.BucketType.user)
	@commands.has_guild_permissions(manage_messages=True) 
	async def echo(self, ctx, *, message):

		await ctx.message.delete()
		await ctx.send(message)



















































def setup(bot):
	bot.add_cog(Moderation(bot))
