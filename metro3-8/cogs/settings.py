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
	
		
	
	@commands.group(invoke_without_command=True,case_insensitive=True,aliases=["setting"])
	@commands.has_guild_permissions(manage_guild=True)
	async def settings(self, ctx):
	
	
		data = await self.bot.config.get_by_id(ctx.message.guild.id)
		prefix = data["prefix"] 
		
		guild = ctx.guild or guild
	
		embed = discord.Embed(
			title= f"Settings for {guild} ({guild.id})",
			description=f":small_blue_diamond: ``{prefix}set <setting> <arguments>`` - Set a setting \n:small_blue_diamond: ``{prefix}setting <module>`` - See your settings for that module \n:octagonal_sign: ``{prefix}reset <setting>`` - Reset a certain setting\n\n  To view the settings you can change run ``{prefix}settings <module>`` ",
			color=self.bot.aqua)
			
		embed.add_field(name="Moderation",value="Mute Message, Ban Message, etc",inline=True)
		embed.add_field(name="Logging",value="Ban Logs, Mod Logs, etc", inline=True)
		embed.add_field(name="Bot Config",value="Prefixes, Setup, etc",inline=True)
		embed.add_field(name="Giveaway",value="Default Time, DM, etc",inline=True)
		embed.add_field(name="Timers",value="Timer colors, etc",inline=True)
		
			
		await ctx.send(embed=embed)


	@settings.command()
	async def moderation(self, ctx):

		data = await self.bot.config.find(ctx.message.guild.id)
		prefix = data["prefix"]

		embed = discord.Embed(
			title=f"Moderation Settings",
			description=f"Use ``{prefix}set <settings> <arguments>`` to set the setting!",
			color=self.bot.green,
			timestamp=ctx.message.created_at)

		settings = await self.bot.settings.find(ctx.message.guild.id)

		muteRole = settings["muteRole"]
		muteMessage = settings["muteMessage"]

		embed.add_field(name="Mute Settings",value=f":small_red_triangle: ``muteRole``: Set the role to give to people that are muted \n:small_blue_diamond: {muteRole} \n\n:small_red_triangle: ``muteMessage`` : Set a message to go along with the default mute message (sends a 2nd embed with a message of your choice) \n:small_blue_diamond: {muteMessage}")
		await ctx.send(embed=embed)

	@settings.command(aliases=["logs","logging","log"])
	async def _logs(self, ctx):

		em = discord.Embed(
			title=f"Logging Settings",
			description=f'Use ``{ctx.prefix}set <settings> <arguments>`` to set the setting!',
			color=self.bot.green,
			timestamp=ctx.message.created_at
		)
		logs = await self.bot.logs.find(ctx.message.guild.id)

		mute = logs["mute"]
		ban = logs["ban"]
		kick = logs["kick"]
		other = logs["other"]

		if not mute is None:
			mute = self.bot.get_channel(mute)
		if not ban is None:
			ban = self.bot.get_channel(ban)
		if not kick is None:
			kick = self.bot.get_channel(kick)
		if not other is None:
			other = self.bot.get_channel(other)

		em.add_field(name="Logging Settings",value=f":small_red_triangle: ``muteLogs``: Set the channel where mutes a logged \n:small_blue_diamond: {mute} \n\n:small_red_triangle: ``banLogs`` - Set the channel where bans are logged \n:small_blue_diamond: {ban} \n\n:small_red_triangle: ``kickLogs`` - Set the channel where kicks are logged \n:small_blue_diamond: {kick}\n\n:small_red_triangle: ``otherLogs`` - Set the channel where other things are logged \n:small_blue_diamond: {other}",inline=True)
		await ctx.send(embed=em)

	@commands.group(invoke_without_command=True, case_insensitive=True)
	@commands.has_guild_permissions(manage_guild=True)
	async def set(self, ctx):
	
		data = await self.bot.config.get_by_id(ctx.message.guild.id)
		prefix = data["prefix"] 
		
		await ctx.send(f"Run the command ``{prefix}settings`` for info on this command")
	
	
	@set.command(name="muteRole")
	async def _muteRole(self, ctx, role : discord.Role):
		
		data = {"_id" : ctx.message.guild.id, "muteRole" : role.id}
		await self.bot.settings.update(data)
		
		await ctx.send(f"I changed the mute role to: ``{role.name}`` ({role.id})")


	@set.command(aliases=["muteMsg","muteMessage"])
	async def _muteMessage(self, ctx, *, message):

		data = {"_id" : ctx.message.guild.id, "muteMessage" : message}
		await self.bot.settings.update(data)

		await ctx.send(f"I changed the mute message to:\n\n > {message}")


	@set.command(aliases=["muteLogs","muteLog"])
	async def _muteLogs(self, ctx, channel : discord.TextChannel):
		await self.bot.logs.update({"_id" : ctx.message.guild.id, "mute" : channel.id})
		await ctx.reply(f"I changed ``muteLogs`` to {channel.mention}",mention_author=False)

	@set.command(aliases=["banLogs","banLog"])
	async def _banLogs(self, ctx, channel : discord.TextChannel):
		await self.bot.logs.update({"_id" : ctx.message.guild.id, "ban" : channel.id})
		await ctx.reply(f"I changed ``banLogs`` to {channel.mention}",mention_author=False)

	@set.command(aliases=["kickLogs","kickLog"])
	async def _kickLogs(self, ctx, channel : discord.TextChannel):
		await self.bot.logs.update({"_id" : ctx.message.guild.id, "kick" : channel.id})
		await ctx.reply(f"I changed ``kickLogs`` to {channel.mention}",mention_author=False)

	@set.command(aliases=["otherLogs","otherLog"])
	async def _otherLogs(self, ctx, channel : discord.TextChannel):
		await self.bot.logs.update({"_id" : ctx.message.guild.id, "other" : channel.id})
		await ctx.reply(f"I changed ``otherLogs`` to {channel.mention}",mention_author=False)

	@commands.group(invoke_without_command=True,case_insensitive=True)
	@commands.has_guild_permissions(manage_guild=True)
	async def reset(self, ctx):

		data = await self.bot.config.find(ctx.message.guild.id)
		prefix = data["prefix"]

		await ctx.send(f"Please specify a setting to reset! If you need help run ``{prefix}settings``")

	@reset.command(pass_context=True)
	async def muteRole(self, ctx):

		def check(message):
			return message.author == ctx.author and message.channel == ctx.channel and message.content.lower() == "reset"
	
		embed = discord.Embed(
			title="Confirmation!",
			description="You are about to reset the ``muteRole`` setting! \n\n If you are sure about this type: ``reset`` (exact - no caps)",
			color=self.bot.red,
			timestamp=ctx.message.created_at
		)
		embed.set_footer(text="You have 5 seconds to respond!")
		await ctx.send(embed=embed)

		await self.bot.wait_for('message', check=check, timeout=5)
		await ctx.send(f"{self.bot.loading}{self.bot.loading}{self.bot.loading} Removing ``muteRole`` from our database")
		data = {"_id" : ctx.message.guild.id, "muteRole" : None}
		await self.bot.settings.update(data)
		await ctx.send(f"{self.bot.check} Successfully reset ``muteRole`` and is removed from our database.")

	@reset.command(pass_context=True)
	async def muteMessage(self, ctx):
		def check(message):
			return message.author == ctx.author and message.channel == ctx.channel and message.content.lower() == "reset"

		embed = discord.Embed(
			title="Confirmation!",
			description="You are about to reset the ``muteMessage`` setting! \n\n If you are sure about this type: ``reset`` (exact - no caps)",
			color=self.bot.red,
			timestamp=ctx.message.created_at
		)
		embed.set_footer(text="You have 5 seconds to respond!")
		await ctx.send(embed=embed)

		await self.bot.wait_for('message', check=check, timeout=5)
		await ctx.send(f"{self.bot.loading}{self.bot.loading}{self.bot.loading} Removing ``muteMessage`` from our database")
		data = {"_id": ctx.message.guild.id, "muteMessage": None}
		await self.bot.settings.update(data)
		await ctx.send(f"{self.bot.check} Successfully reset ``muteMessage`` and is removed from our database.")
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
def setup(bot):
	bot.add_cog(Settings(bot))