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


def substitute_args(message, member) -> str:

	return Template(message).safe_substitute(
        {
            "MENTION": member.mention,
			"MEMBER": member,
			"ID": member.id,
			"NAME": member.name,
			'DISCRIM': member.discriminator,
			"GUILD": member.guild,
		
        }
        )



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

class Mute(commands.Cog):

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
			await ctx.message.add_reaction(self.bot.cross)
			return await ctx.reply("You cannot mute yourself",mention_author=False)

		if member.guild_permissions.manage_guild or member.guild_permissions.administrator:
			await ctx.message.add_reaction(self.bot.cross)
			return await ctx.send("This person is a moderator/admin so you can't mute them!",mention_author=False)

		guild = ctx.guild

		settings = await self.bot.settings.get_by_id(ctx.message.guild.id)
		muteRole = settings["muteRole"]

		if muteRole is None:
			muteRole = discord.utils.get(guild.roles, name="Muted")

			if muteRole is None:

				embed = discord.Embed(title="Error!",description=f"You don't have a mute role set or a role called Muted! \n\n If you have a mute role already set up run: ``{ctx.prefix}set muteRole <role>`` \n\n If you don't have a mute role set up and would like me to create one run: ``{ctx.prefix}muteRole``",color=0xFFFF00, timestamp=ctx.message.created_at)
				await ctx.message.add_reaction(self.bot.cross)
				return await ctx.reply(embed=embed,mention_author=False)

		else:
			muteRole = discord.utils.get(guild.roles, id=muteRole)

		if muteRole in member.roles:
			await ctx.message.add_reaction(self.bot.cross)
			return await ctx.reply("This person is already muted!",mention_author=False)


		minutes, seconds = divmod(time, 60)
		hours, minutes = divmod(minutes, 60)
		days, hours = divmod(hours, 24)


		if not int(time):
			secondsTime = None
			time = f"None - (muted until someone unmutes)"

		else:
			secondsTime = time
			if int(days):
				time = f"**{days}** days, **{hours}** hours, **{minutes}** minutes, **{seconds}** seconds"
			if int(hours):
				time = f"**{hours}** hours, **{minutes}** minutes, **{seconds}** seconds"
			if int(minutes):
				time = f"**{minutes}** minutes, **{seconds}** seconds"
			if int(seconds):
				time = f"**{seconds}** seconds"

		data = {'_id': member.id, 'mutedAt': datetime.datetime.now(),'muteDuration': secondsTime,'mutedBy': ctx.author.id,'guildId': ctx.guild.id, 'reason': reason}
		await self.bot.mutes.upsert(data)

		self.bot.muted_users[member.id] = data

		await member.add_roles(muteRole)

		info = await self.bot.logs.find(ctx.message.guild.id)

		log = info["mute"]
		if not log is None:
			logs = self.bot.get_channel(log)
			embed = discord.Embed(
				title="mute",
				description=f"**Offender:** {member} - {member.mention} -``{member.id}`` \n**Time:** {time} \n**Reason:** {reason}\n**Responsible Moderator:** {ctx.author} - {ctx.author.mention} -``{ctx.author.id}``",
				color=self.bot.orange,
				timestamp=ctx.message.created_at)
			await logs.send(embed=embed)


		msg_member = discord.Embed(
				title="Muted!",
				description=f"You were muted in **{guild}**! \n\n**Responsible Moderator:** {ctx.author.mention} - ``{ctx.author.id}`` \n**Time:** {time} \n**Reason:** {reason}",
				color=self.bot.red,
				timestamp=ctx.message.created_at)
		msg_channel = discord.Embed(
				title="Success!",
				description=f"You successfully muted {member.mention}! \n\n**Responsible Moderator:** {ctx.author.mention} \n**Time:** {time} \n**Reason:** {reason}",
				color=self.bot.green,
				timestamp=ctx.message.created_at)

		if secondsTime is None:
			try:
				await member.send(embed=msg_member)
				await ctx.message.add_reaction(self.bot.check)
				await ctx.reply(embed=msg_channel,mention_author=False)

			except:
				await ctx.message.add_reaction(self.bot.check)
				msg_channel.set_footer(text="Note that I couldn't DM them because they were closed")
				await ctx.reply(embed=msg_channel,mention_author=False)


		else:

			msgMember = discord.Embed(
						title="Muted!",
						description=f"You were muted in **{guild}**! \n\n**Responsible Moderator:** {ctx.author.mention} - ``{ctx.author.id}`` \n**Time:** {time} \n**Reason:** {reason}",
						color=self.bot.red,
						timestamp=ctx.message.created_at)

			msgChannel = discord.Embed(
						title="Success!",
						description=f"You successfully muted {member.mention}! \n\n**Responsible Moderator:** {ctx.author.mention} \n**Time:** {time} \n**Reason:** {reason}",
						color=self.bot.green,
						timestamp=ctx.message.created_at)

			msgNoDm = discord.Embed(
						title="Success!",
						description=f"You successfully muted {member.mention}! \n\n**Responsible Moderator:** {ctx.author.mention} \n**Time:** {time} \n**Reason:** {reason}",
						color=self.bot.green,
						timestamp=ctx.message.created_at)
			msgNoDm.set_footer(text="Note that I couldn't DM them because they were closed")

			try:
				await member.send(embed=msgMember)
				await ctx.message.add_reaction(self.bot.check)
				await ctx.reply(embed=msgChannel,mention_author=False)

				muteMessage = settings["muteMessage"]
				if not muteMessage is None:
					embed = discord.Embed(description=muteMessage,color=self.bot.red)
					await member.send(embed=embed)

			except:
				await ctx.message.add_reaction(self.bot.check)
				await ctx.reply(embed=msgNoDm,mention_author=False)

		if secondsTime and secondsTime < 300:
			await asyncio.sleep(secondsTime)

			if mutedRole in member.roles:

				after_mute	= discord.Embed(title='Unmuted!',description=f'You were unmuted in **{guild}** because your mute ended',color=0x00FF00)

				await member.remove_roles(mutedRole)
				await member.send(embed=after_mute)

				await self.bot.mutes.delete(member.id)

			try:
				self.bot.muted_users.pop(member.id)

			except KeyError:
				pass



	@commands.command(hidden=True)
	@commands.has_guild_permissions(manage_roles=True)
	async def muteRole(self, ctx):

		check = await self.bot.settings.find(ctx.message.guild.id)
		oldMute = check["muteRole"]

		if not oldMute is None:
			await ctx.message.add_reaction(self.bot.cross)
			return await ctx.reply(f"You already have a mute role set up!  \nIf you think this is a mistake or it says @deleted-role run: ``{ctx.prefix}reset muteRole``",mention_author=False)

		guild = ctx.guild

		await ctx.message.add_reaction(self.bot.check)
		await ctx.reply("Setting up Muted Role for your server! Starts in 3 seconds",mention_author=False)
		await asyncio.sleep(3)

		mutedRole = await guild.create_role(name="Muted")
		await ctx.send(f":one: Created the role! ({mutedRole.mention})")
		await asyncio.sleep(1)

		for channel in guild.channels:
			await channel.set_permissions(mutedRole, speak=False, send_messages=False)

		await ctx.send(f":two: Set the permissions across all channels!")
		await asyncio.sleep(1)

		data = {"_id" : ctx.message.guild.id, "muteRole" : mutedRole.id}
		await self.bot.settings.update(data)
		await ctx.send(f":three: Uploaded the muted role to our database!")

		await asyncio.sleep(1)
		await ctx.send(f":tada: Successfully created the mute role ({mutedRole.mention}) and is automaticly set as the default mute role!")






	@commands.command()
	@commands.has_guild_permissions(manage_roles=True)
	async def unmute(self, ctx, member : discord.Member, *, reason=None):

		guild = ctx.guild

		await self.bot.mutes.delete(member.id)

		try:
			self.bot.muted_users.pop(member.id)

		except KeyError:
			pass

		muteRole = await self.bot.settings.find(ctx.message.guild.id)

		info = await self.bot.logs.find(ctx.message.guild.id)

		log = info["mute"]
		if not log is None:
			logs = self.bot.get_channel(log)
			embed = discord.Embed(
				title="unmute",
				description=f"**Offender:** {member} - {member.mention} -``{member.id}`` \n**Reason:** {reason}\n**Responsible Moderator:** {ctx.author} - {ctx.author.mention} -``{ctx.author.id}``",
				color=self.bot.green,
				timestamp=ctx.message.created_at)
			await logs.send(embed=embed)

		if not muteRole:

			role = discord.utils.get(member.guild.roles, name = "Muted")
			mutedRole = discord.utils.get(member.roles, name="Muted")

			if role not in member.roles:
				not_muted = discord.Embed(title='Error!',
										  description=f"This person isn't even muted! \n Use ``{ctx.prefix}mute <member> [time] [reason]`` to mute someone!",
										  color=self.bot.orange)

				await ctx.message.add_reaction(self.bot.cross)
				return await ctx.reply(embed=not_muted,mention_author=False)

			msg_channel = discord.Embed(title='Sucess!',description=f'You unmuted {member.mention}! \n**Reason:** {reason}',color=self.bot.green)
			msg_member	= discord.Embed(title='Unmuted!',description=f'You were unmuted in **{guild}**! \n**Reason:** {reason} \n**Note:** Your mute was ended early because {ctx.author.mention} unmuted you',color=self.bot.green)

			await member.remove_roles(role)
			await ctx.message.add_reaction(self.bot.check)
			await ctx.reply(embed=msg_channel,mention_author=False)

			return await member.send(embed=msg_member)

		else:
			role = muteRole["muteRole"]
			roleObj = discord.utils.get(member.guild.roles, id = role)
			mutedRole = discord.utils.get(member.roles, id = role)

			if roleObj not in member.roles:
				not_muted = discord.Embed(title='Error!',
										  description=f"This person isn't even muted! \n Use ``{ctx.prefix}mute <member> [time] [reason]`` to mute someone!",
										  color=self.bot.orange)

				await ctx.message.add_reaction(self.bot.cross)
				return await ctx.reply(embed=not_muted,mention_author=False)

			msg_channel = discord.Embed(title='Sucess!',
										description=f'You unmuted {member.mention}! \n**Reason:** {reason}',
										color=self.bot.green)
			msg_member = discord.Embed(title='Unmuted!',
									   description=f'You were unmuted in **{guild}**! \n**Reason:** {reason} \n**Note:** Your mute was ended early because {ctx.author.mention} unmuted you',
									   color=self.bot.green)

			await member.remove_roles(roleObj)
			await ctx.message.add_reaction(self.bot.check)
			await ctx.reply(embed=msg_channel,mention_author=False)

			return await member.send(embed=msg_member)




	@mute.error
	async def mute_error(self, ctx, error):
	
		if isinstance(error, commands.MissingRequiredArgument):
		
			embed = discord.Embed(
					title="Mute Command",
					description=f"```yaml\nCommand: {ctx.prefix}mute```\n\n **Mutes a member in the current guild** \n\n Correct usage: **{ctx.prefix}mute <member> [time] [reason]**",
					color=0xFFFF00,
					timestamp=ctx.message.created_at)
			await ctx.send(embed=embed)

		if isinstance(error, commands.CommandInvokeError):
			await ctx.send(f"```py\n{error}```")

		




















































def setup(bot):
	bot.add_cog(Mute(bot))
