import re
import random
import asyncio

import discord
from discord.ext import commands, tasks

from utils.util import GetMessage
import datetime
from utils.mongo import Document
from copy import deepcopy
import re
from dateutil.relativedelta import relativedelta

import platform

time_regex = re.compile(r"(?:(\d{1,5})(h|s|m|d))+?")
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
	
	
	
class Giveaway(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

		self.timer_end = self.update_timer.start()

	def cog_unload(self):
		self.timer_end.cancel()


	@commands.Cog.listener()
	async def on_ready(self):
		print(f"{self.__class__.__name__} Cog has been loaded\n-----")
		
		
		
		


	
	
	@tasks.loop(seconds=2)
	async def update_timer(self):
	
		currentTimers = await self.bot.timer.get_all()
	
		for timer in currentTimers:
			self.bot.timers[timer["_id"]] = timer
		
	
		currentTime = datetime.datetime.now()

		timers = deepcopy(self.bot.timers)
		
	
		
		for key, value in timers.items():
		
			if value['_id'] is None:
				return	

			
			end = value["timerEnd"]
			
		
			message = value["_id"]
			id = value['channel']
			timer = value["name"]
			guild = value["guild"]
			

				
			realChannel = self.bot.get_channel(id)
			message = int(message)
			
			message = realChannel.get_partial_message(message)
			
			
				
			if end < currentTime:
				
				e = discord.Embed(title=timer, description=":tada: **Timer Ended!** :tada:")
				await message.edit(embed=e)	
				message = value["_id"]
				await realChannel.send(f"The timer for **{timer}** has ended! \n https://discord.com/channels/{guild}/{id}/{message}")	
				print("Ended a timer")
			
				await self.bot.timer.delete(value["_id"])
				
				
			try:
				message = value["_id"]
				message = int(message)
				self.bot.timers.pop(message)

			except KeyError:
				pass
					
				
	@tasks.loop(seconds=69)
	async def edit_timer(self):
		print("e")
	
			
				
		
				
			

	@update_timer.before_loop
	async def before_update_timer(self):
		await self.bot.wait_until_ready()
		
	@commands.group(invoke_without_command=True,case_insensitive=True)
	async def timer(self, ctx):
	
		data = await self.bot.config.get_by_id(ctx.message.guild.id)
		prefix = data["prefix"]
	
		e = discord.Embed(
			title=f"Timer Module",
			description=f"```yaml\nCommand: {prefix}timer``` \n\n **Please use the following sub-commands:** \n\n ``start`` - instantly start a timer \n``end`` - end an exsisting timer",
			color=self.bot.aqua,
			timestamp = ctx.message.created_at)
			
		await ctx.send(embed=e)
		
	@timer.command(description="Instanly start a timer")
	@commands.cooldown(rate=1, per=3, type=commands.BucketType.user)
	async def start(self, ctx, time : TimeConverter, *,timer="Timer"):
	
		currentTime = datetime.datetime.now()
	
		if time > 259200:
			return await ctx.send(f"Timers cannot be longer than 3 days")
		if time < 10:
			return await ctx.send(f"Timers cannot be shorter than 10 seconds")
		
	
		minutes, seconds = divmod(time, 60)
		hours, minutes = divmod(minutes, 60)
		days, hours = divmod(hours, 24)
	
		if int(days):
		
			d = discord.Embed(
				title=timer,
				description=f"**{int(days)}** days, **{int(hours)}** hours, **{int(minutes)}** minutes, **{int(seconds)}** seconds",
				color=self.bot.aqua)
				
			msg = await ctx.send(embed=d)
			await ctx.message.add_reaction(self.bot.check)
			await msg.add_reaction("⏲️")
			
			timerEnd = currentTime + relativedelta(seconds=time)
			
			data = {"_id" : msg.id , "channel" : ctx.channel.id, "guild" : ctx.guild.id, "timerEnd" : timerEnd, "timerStart" : currentTime, "timerLength" : time, "name" : timer}
			await self.bot.timer.upsert(data)
			return
			
			
		if int(hours):
			
			h = discord.Embed(
				title=timer, 
				description=f"**{int(hours)}** hours, **{int(minutes)}** minutes, **{int(seconds)}** seconds",
				color=self.bot.aqua)
				
			msg = await ctx.send(embed=h)
			await ctx.message.add_reaction(self.bot.check)
			await msg.add_reaction("⏲️")
			
			timerEnd = currentTime + relativedelta(seconds=time)
			
			data = {"_id" : msg.id , "channel" : ctx.channel.id, "guild" : ctx.guild.id, "timerEnd" : timerEnd, "timerStart" : currentTime, "timerLength" : time, "name" : timer}
			await self.bot.timer.upsert(data)
			return
			
			
		
		if int(minutes):
			
			m = discord.Embed(
				title=timer,
				description=f"**{int(minutes)}** minutes, **{int(seconds)}** seconds",
				color=self.bot.aqua)
				
			msg = await ctx.send(embed=m)
			await ctx.message.add_reaction(self.bot.check)
			await msg.add_reaction("⏲️")
			
			timerEnd = currentTime + relativedelta(seconds=time)
			
			data = {"_id" : msg.id , "channel" : ctx.channel.id, "guild" : ctx.guild.id, "timerEnd" : timerEnd, "timerStart" : currentTime, "timerLength" : time, "name" : timer}
			await self.bot.timer.upsert(data)
			
			return
			
				
				
		if int(seconds):
		
			s = discord.Embed(
				title=timer,
				description=f"**{int(seconds)}** seconds",
				color=self.bot.aqua)
				
			msg = await ctx.send(embed=s)
			await ctx.message.add_reaction(self.bot.check)
			await msg.add_reaction("⏲️")
			
			timerEnd = currentTime + relativedelta(seconds=time)
			
			data = {"_id" : msg.id , "channel" : ctx.channel.id, "guild" : ctx.guild.id, "timerEnd" : timerEnd, "timerStart" : currentTime, "timerLength" : time, "name" : timer}
			await self.bot.timer.upsert(data)
			return
			
			

			
		
	
	@commands.command(aliases=["60s",'60'])
	async def _60seconds(self, ctx):
			
		embed = discord.Embed(title="Timer",description="**1** minute, **0** seconds",color=self.bot.aqua)
		
		message = await ctx.send(embed=embed)
		await asyncio.sleep(4)
		
		embed = discord.Embed(title="Timer",description="**56** seconds",color=self.bot.aqua)
		await message.edit(embed=embed)
		await asyncio.sleep(4)
		
		embed = discord.Embed(title="Timer",description="**52** seconds",color=self.bot.aqua)
		await message.edit(embed=embed)
		await asyncio.sleep(4)		
		
		embed = discord.Embed(title="Timer",description="**48** seconds",color=self.bot.aqua)
		await message.edit(embed=embed)
		await asyncio.sleep(4)	
		
		embed = discord.Embed(title="Timer",description="**44** seconds",color=self.bot.aqua)
		await message.edit(embed=embed)
		await asyncio.sleep(4)			
		
		embed = discord.Embed(title="Timer",description="**40** seconds",color=self.bot.aqua)
		await message.edit(embed=embed)
		await asyncio.sleep(4)		
	
		embed = discord.Embed(title="Timer",description="**36** seconds",color=self.bot.aqua)
		await message.edit(embed=embed)
		await asyncio.sleep(4)	
		
		embed = discord.Embed(title="Timer",description="**32** seconds",color=self.bot.aqua)
		await message.edit(embed=embed)
		await asyncio.sleep(4)			
		
		embed = discord.Embed(title="Timer",description="**28** seconds",color=self.bot.aqua)
		await message.edit(embed=embed)
		await asyncio.sleep(4)
		
		embed = discord.Embed(title="Timer",description="**24** seconds",color=self.bot.aqua)
		await message.edit(embed=embed)
		await asyncio.sleep(4)			
		
		embed = discord.Embed(title="Timer",description="**20** seconds",color=self.bot.aqua)
		await message.edit(embed=embed)
		await asyncio.sleep(4)	
		
		embed = discord.Embed(title="Timer",description="**16** seconds",color=self.bot.aqua)
		await message.edit(embed=embed)
		await asyncio.sleep(6)	
		
		
		embed = discord.Embed(title="Timer",description="**10** seconds",color=self.bot.aqua)
		await message.edit(embed=embed)
		await asyncio.sleep(3)
		
		embed = discord.Embed(title="Timer",description="**7** seconds",color=self.bot.aqua)
		await message.edit(embed=embed)
		await asyncio.sleep(3)	
		
		embed = discord.Embed(title="Timer",description="**4** seconds",color=self.bot.aqua)
		await message.edit(embed=embed)
		await asyncio.sleep(2)
		
		embed = discord.Embed(title="Timer",description="**2** seconds",color=self.bot.aqua)
		await message.edit(embed=embed)
		await asyncio.sleep(1)	
		
		
		embed = discord.Embed(title="Timer",description="**1** second",color=self.bot.aqua)
		await message.edit(embed=embed)
		await asyncio.sleep(2)
		
		embed = discord.Embed(title="Timer Ended",description=":tada: :tada: 60 second timer ended :tada: :tada:",color=self.bot.aqua)
		await message.edit(embed=embed)
	
	
		
			
		
		
		
				
		
		
			
def setup(bot):
    bot.add_cog(Giveaway(bot))
	
