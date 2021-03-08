import discord
from discord.ext import commands, tasks
import platform
import datetime
import random
import utils.json_loader
from utils.mongo import Document
from discord.ext.commands.cooldowns import BucketType
import asyncio
from copy import deepcopy
import re
from dateutil.relativedelta import relativedelta
import time

from TagScriptEngine import Interpreter, adapter, block








class Settings(commands.Cog):

	def __init__(self, bot):
		self.bot = bot


	@commands.Cog.listener()
	async def on_ready(self):
		print(f"{self.__class__.__name__} Cog has been loaded\n-----")
		
		
		
	
	@commands.group(invoke_without_command=True,case_insensitive=True)
	@commands.has_guild_permissions(manage_guild=True)
	async def settings(self, ctx):
	
	
		data = await self.bot.config.get_by_id(ctx.message.guild.id)
		prefix = data["prefix"] 
		
		guild = ctx.guild or guild
	
		embed = discord.Embed(
			title= f"Settings for {guild} ({guild.id})",
			description=f"You can change settings for {guild} here and most things are fully custom such as default mute duration or ban message/logs. If you don't set anything they will still work but will come more basic, such as: You were muted in Bot Server for 10 mins. \n\n **How to set settings:**\nUse the command ``{prefix}set <setting> <value>`` \n\n **Examples:** \n{prefix}set muteDuration 10m \n{prefix}set modLogs #modlogs \n\n To view the settings you can change run ``{prefix}settings <module>`` (module's are listed below)",
			color=self.bot.aqua)
			
		embed.add_field(name="Moderation",value="Default Mute, Ban Message, warn threshold, etc",inline=False)
		embed.add_field(name="Logging",value="Ban Logs, Mod Logs, etc", inline=False)
		embed.add_field(name="Bot Config",value="Prefixes, Setup, etc",inline=False)
		
			
		await ctx.send(embed=embed)
		
		
	@commands.group(invoke_without_command=True, case_insensitive=True)
	@commands.has_guild_permissions(manage_guild=True)
	async def set(self, ctx):
	
		data = await self.bot.config.get_by_id(ctx.message.guild.id)
		prefix = data["prefix"] 
		
		await ctx.send(f"Run the command ``{prefix}settings`` for info on this command")
	
	
	@set.command()
	async def muteDmMessage(self, ctx, *, args):
		
		data = {"_id" : ctx.message.guild.id, "muteDmMessage" : args}
		await self.bot.settings.updata(data)
		
		embed = discord.Embed(title="Sucessfully updated Mute DM Message",description="I changed the DM message to muted users to: \n\n ``{args}``",color=self.bot.aqua)
		await ctx.send(embed=embed)
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
def setup(bot):
	bot.add_cog(Settings(bot))