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

class afk(commands.Cog):

	def __init__(self, bot):
		self.bot = bot


	@commands.Cog.listener()
	async def on_ready(self):
		print(f"{self.__class__.__name__} Cog has been loaded\n-----")
		
	@commands.group(invoke_without_command=True,case_insensitive=True,name="AFK")
	async def afk(self, ctx):
		"""Set your AFK status"""
		
		data = await self.bot.config.get_by_id(ctx.message.guild.id)
		prefix = data["prefix"]
		
		
		
		e = discord.Embed(
		
			title = "AFK Module",
			description = f"```yaml\nCommand: {prefix}afk``` \n\n**Please use the following sub-commands:** \n\n ``on`` - turn on and set an afk message \n``off`` turn off afk competly",
			color=self.bot.aqua)
			
		await ctx.send(embed=e)
		
	@afk.command()
	async def on(self, ctx, *,afk="AFK"):
		"""Turn your AFK status on and set a custom message"""
		
		data = await self.bot.config.get_by_id(ctx.message.guild.id)
		prefix = data["prefix"]
		
		check = await self.bot.afk.find(ctx.author.id)
		
		if check is None:
		
			data = {"_id" : ctx.author.id, "afk" : afk}
			await self.bot.afk.upsert(data)
			
			e = discord.Embed(title="AFK Status",description=f"I set your AFK status to **{afk}**!",color=0x1ABC9C)
			e.set_footer(text=f"To turn this off run: {prefix}afk off")
			await ctx.send(embed=e)
			
			
		else:
		
			return await ctx.send(f"Your AFK status is already on!")
	
	
	@afk.command()
	async def off(self, ctx):
	
		data = await self.bot.config.get_by_id(ctx.message.guild.id)
		prefix = data["prefix"]
		
		check = await self.bot.afk.find(ctx.author.id)
		
		if check is None:
			e = discord.Embed(title="Error!",description=f"Your AFK status isn't even on! \n\n To turn this on run: ``{prefix}afk on <afk-message>``",color=self.bot.aqua)
			
			return await ctx.send(embed=e)
			
		else:
			await self.bot.afk.delete(ctx.author.id)
			e = discord.Embed(title="AFK Status",description=f"I turned off your AFK!",color=0xF1C40F)
			e.set_footer(text=f"To turn this on run: {prefix}afk on <afk-message>")
			await ctx.send(embed=e)





	

























def setup(bot):
	bot.add_cog(afk(bot))