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

class config(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

		
	@commands.Cog.listener()
	async def on_ready(self):
		print(f"{self.__class__.__name__} Cog has been loaded\n-----")
		
		
	@commands.command()
	async def test(self, ctx):
		await ctx.send("test idiot")
	
		
	
	
def setup(bot):
	bot.add_cog(config(bot))