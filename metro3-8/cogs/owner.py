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
import traceback
import os




class Owner(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_ready(self):
		print(f"{self.__class__.__name__} Cog has been loaded\n-----")
		


	@commands.group(hidden=True,invoke_without_command=True,case_insensitive=True)
	@commands.is_owner()
	async def dev(self, ctx):

		await ctx.invoke(self.bot.get_command("help"), entity="dev")



	@dev.command()
	async def reset(self, ctx, guild : int):


		await self.bot.settings.delete(guild)
		await self.bot.logs.delete(guild)

		data = {"_id" : guild,
				"muteRole" : None,
				"muteMessage" : None}

		data1 = {"_id": guild,
				"mute": None,
				"ban": None,
				"kick": None,
				"other": None}

		await self.bot.settings.upsert(data)
		await self.bot.logs.upsert(data1)
		await ctx.send(f"Reset the data for: ``{guild}``")


	@dev.command(hidden=True)
	async def online(self, ctx, *, status):
		await self.bot.change_presence(status=discord.Status.online, activity=discord.Game(name=status))
		await ctx.reply(f"Set the status to {self.bot.online} and playing **{status}**",mention_author=False)

	@dev.command(hidden=True)
	async def idle(self, ctx, *, status):
		await self.bot.change_presence(status=discord.Status.idle, activity=discord.Game(name=status))
		await ctx.reply(f"Set the status to {self.bot.idle} and playing **{status}**",mention_author=False)

	@dev.command(hidden=True)
	async def dnd(self, ctx, *, status):
		await self.bot.change_presence(status=discord.Status.dnd, activity=discord.Game(name=status))
		await ctx.reply(f"Set the status to {self.bot.dnd} and playing **{status}**",mention_author=False)

	@dev.command(hidden=True)
	async def offline(self, ctx, *, status):
		await self.bot.change_presence(status=discord.Status.invisible, activity=discord.Game(name=status))
		await ctx.reply(f"Set the status to {self.bot.offline} and playing **{status}**",mention_author=False)



	@commands.command(name='reload', description="Reload all/one of the bots cogs!",hidden=True)
	@commands.is_owner()
	async def reload(self, ctx, cog=None):
		guild = ctx.guild
		if not cog:
			# No cog, means we reload all cogs
			async with ctx.typing():
				embed = discord.Embed(
					title="Reloading all cogs!",
					color=0x9B59B6,
					timestamp=ctx.message.created_at
				)
				for ext in os.listdir("./cogs/"):
					if ext.endswith(".py") and not ext.startswith("_"):
						try:
							self.bot.unload_extension(f"cogs.{ext[:-3]}")
							self.bot.load_extension(f"cogs.{ext[:-3]}")
							embed.add_field(
								name=f"Reloaded: `{ext}`",
								value='\uFEFF',
								inline=False
							)
						except Exception as e:
							embed.add_field(
								name=f"Failed to reload: `{ext}`",
								value=e,
								inline=False
							)
						await asyncio.sleep(0.5)

		else:
			# reload the specific cog
			async with ctx.typing():
				embed = discord.Embed(
					title="Reloading all cogs!",
					color=0x9B59B6,
					timestamp=ctx.message.created_at
				)
				ext = f"{cog.lower()}.py"
				if not os.path.exists(f"./cogs/{ext}"):
					# if the file does not exist
					embed.add_field(
						name=f"Failed to reload: `{ext}`",
						value="This cog does not exist.",
						inline=False
					)

				elif ext.endswith(".py") and not ext.startswith("_"):
					desired_trace = traceback.format_exc()
					try:
						self.bot.unload_extension(f"cogs.{ext[:-3]}")
						self.bot.load_extension(f"cogs.{ext[:-3]}")
						embed.add_field(
							name=f"Reloaded: `{ext}`",
							value='\uFEFF',
							inline=False
						)
					except Exception:
						desired_trace = traceback.format_exc()
						embed.add_field(
							name=f"Failed to reload: `{ext}`",
							value=desired_trace,
							inline=False
						)

				await ctx.send(f"```py\n{desired_trace}```",mention_author=False)


	@commands.command(hidden=True)
	@commands.is_owner()
	async def unload(self, ctx, cog=None):

		guild=ctx.guild

		ext = f"{cog.lower()}.py"
		self.bot.unload_extension(f"cogs.{ext[:-3]}")

		await ctx.send(f"Unloaded ``{ext}``")

	@commands.command(hidden=True)
	@commands.is_owner()
	async def load(self, ctx, cog=None):

		guild=ctx.guild

		ext = f"{cog.lower()}.py"
		self.bot.load_extension(f"cogs.{ext[:-3]}")

		await ctx.send(f"Loaded ``{ext}``")

	@commands.group(hidden=True, aliases=["pm"],invoke_without_command=True,case_insensitive=True)
	async def premium(self, ctx):

		await ctx.reply(f"Incorrect usage! \n\n``{ctx.prefix}premium give <guild>`` -owner only\n``{ctx.prefix}premium revoke <guild>`` -owner only\n``{ctx.prefix}premium status [guild=None]``",mention_author=False)


	@premium.command(name="give",aliases=["+" , "add"])
	@commands.is_owner()
	async def _give(self, ctx, id : int):

		try:
			guild = self.bot.get_guild(id)

		except:
			await ctx.message.add_reaction(self.bot.cross)
			return await ctx.reply(f"That is not a vaild guild!",mention_author=False)

		if guild is None:
			await ctx.message.add_reaction(self.bot.cross)
			return await ctx.reply(f"That guild does not have Metro in it!", mention_author=False)



		data = await self.bot.premium.find(guild.id)

		if data is None:

			info = {"_id" : guild.id}
			await self.bot.premium.upsert(info)

			await ctx.reply(f"Added premium to **{guild}**",mention_author=False)
			await ctx.message.add_reaction(self.bot.check)


		else:
			await ctx.message.add_reaction(self.bot.cross)
			return await ctx.reply(f"This guild already has premium! \n\nUse ``{ctx.prefix}premium revoke <guild>`` to remove it!",mention_author=False)


	@premium.command(name="revoke",aliases=["-", "remove"])
	@commands.is_owner()
	async def _revoke(self, ctx, id : int):

		try:
			guild = self.bot.get_guild(id)
		except:
			await ctx.message.add_reaction(self.bot.cross)
			return await ctx.reply(f"That is not a vaild guild!",mention_author=False)

		if guild is None:
			await ctx.message.add_reaction(self.bot.cross)
			return await ctx.reply(f"That guild does not have Metro in it!", mention_author=False)


		data = await self.bot.premium.find(guild.id)

		if not data is None:
			await self.bot.premium.delete(guild.id)

			await ctx.reply(f"Removed premium to **{guild}**", mention_author=False)
			await ctx.message.add_reaction(self.bot.check)

		else:
			await ctx.message.add_reaction(self.bot.cross)
			return await ctx.reply(f"This guild doesn't have premium! \n\nUse ``{ctx.prefix}premium give <guild>`` to give them premium!", mention_author=False)

	@premium.command(name="status",description="Check if a server has Metro Premium")
	async def _status(self, ctx, guild : int = None):

		if guild is None:
			guild = ctx.guild

		data = await self.bot.premium.find(guild)

		if data is None:
			status = f"doesn't have premium {self.bot.cross}"
		else:
			status = f"has premium {self.bot.check}"

		await ctx.reply(f"**{guild}** {status}",mention_author=False)




def setup(bot):
	bot.add_cog(Owner(bot))