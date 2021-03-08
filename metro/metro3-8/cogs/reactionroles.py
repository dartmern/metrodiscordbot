import discord
from discord.ext import commands, tasks
import platform
import datetime
import random
import utils.json_loader
from utils.mongo import Document
from discord.ext.commands.cooldowns import BucketType
import asyncio
import re
from fuzzywuzzy import process
import datetime

from dateutil.relativedelta import relativedelta

import random


import typing
import emojis



class ReactionRolesNotSetup(commands.CommandError):
	pass
	
	
def is_setup():
	async def wrap_func(ctx):
		data = await ctx.bot.config.find(ctx.guild.id)
		if data is None:
			raise ReactionRolesNotSetup
			
		if data.get("message_id") is None:
			raise ReactionRolesNotSetup
			
		return True
	return commands.check(wrap_func)
		
class ReactionRoles(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_ready(self):
		print(f"{self.__class__.__name__} Cog has been loaded\n-----")



	@commands.group(aliases=["rr"],invoke_without_command=True)
	async def reactionrole(self, ctx):
	
		await ctx.invoke(self.bot.get_command("help"), entity="reactionroles")
		
		
	@reactionrole.command()
	async def channel(self, ctx, channel : discord.TextChannel = None):
	
		if channel == None:
			return await ctx.send(f"Please input a channel!")
			
		try:
			await channel.send("testing if I can send messages",delete_after=0.5)
		except discord.HTTPExeception:
			return await ctx.send(f"I can't send messages in that channel please try giving me admin perms")
			

		embed = discord.Embed(title="Reaction Roles!")
		
		desc = ""
		reaction_roles = await self.bot.reactionroles.get_all()
		reaction_roles = list(filter(lambda r: r["guild_id"] == ctx.guild.id, reaction_roles))
		
		for item in reaction_roles:
			role = ctx.guild.get_role(item=["role"])
			desc += f"{item['_id']} : {role.mention}\n"
			
		embed.description=desc
		
		m = await channel.send(embed=embed)
		
		for item in reaction_roles:
			await m.add_reaction(item["_id"])
			
		await self.bot.config.upsert(
		{
			"_id":ctx.guild.id,
			"message_id":m.id,
			"channel_id":channel.id,
			"is_enabled":True,
			
			
		})
		
		await ctx.send(f"That should be all setup for you!")
		
		












def setup(bot):
	bot.add_cog(ReactionRoles(bot))