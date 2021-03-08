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

time_regex = re.compile("(?:(\d{1,5})(h|s|m|d))+?")
time_dict = {"h": 3600, "s": 1, "m": 60, "d": 86400}

class BetterRoles(commands.Converter):
	async def convert(self, ctx, argument):
		try:
			return await commands.RoleConverter().convert(ctx, argument)
		except commands.BadArgument:
			role_to_return = discord.utils.find(lambda x: x.name.lower() == argument.lower(), ctx.guild.roles)
			if role_to_return is not None:
				return role_to_return
		roles_and_aliases = {}
	
		for r in ctx.guild.roles:
			roles_and_aliases[r.name] = r.id

			name, ratio = process.extractOne(argument, [x for x in roles_and_aliases])
			if ratio >= 75:
				role_to_return = discord.utils.get(ctx.guild.roles, id=roles_and_aliases[name])
				return role_to_return
				
				
				
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
		
		
class Roles(commands.Cog):

	def __init__(self, bot):
		self.bot = bot


	@commands.Cog.listener()
	async def on_ready(self):
		print(f"{self.__class__.__name__} Cog has been loaded\n-----")



	@commands.group(invoke_without_command=True,case_insensitive=True)
	@commands.has_permissions(manage_roles=True)
	async def role(self, ctx):
	
		data = await self.bot.config.get_by_id(ctx.message.guild.id)
		prefix = data["prefix"] 
		
		e = discord.Embed(
			title=f"Role Utilites",
			description=f"```yaml\nCommand: {prefix}role``` \n\n **Please use the following sub-commands:** \n\n{self.bot.check}``add`` - add a role to user \n{self.bot.check}``remove`` - remove a role from user \n{self.bot.check}``temp`` - give a role temporarily\n{self.bot.cross}``color`` - color a exisiting role \n{self.bot.cross}``create`` - create a new role \n{self.bot.cross}``list`` - list all the roles in the server",
			color=self.bot.aqua)
			
		await ctx.send(embed=e)
		
	@role.command(aliases=["+","give"])
	async def add(self, ctx, member : discord.Member, role : BetterRoles=None):
		if role == None:
			return await ctx.send(f"Specify a role please!")
			
		add_or_remove = role not in member.roles
		
		if add_or_remove:
			await member.add_roles(role)
			return await ctx.send(f"Added **{role.name}** to **{member.name}**")
			
		else:
			return await ctx.send(f"This person already has this role!")
			
	@role.command(aliases=["ri","vanish","-"])
	async def remove(self, ctx, member : discord.Member, role : BetterRoles=None):
		if role == None:
			return await ctx.send(f"Specify a role please!")
			
		add_or_remove = role in member.roles
		
		if add_or_remove:
			await member.remove_roles(role)
			return await ctx.send(f"Removed **{role.name}** from **{member.name}**")
			
		else:
			return await ctx.send(f"This person doesn't even have this role!")
			
	
	@role.command(aliases=["temporarily"])
	async def temp(self, ctx, member : discord.Member,time: TimeConverter, role : BetterRoles=None):
		
		if role == None:
			return await ctx.send(f"Specify a role please!")
		
		if time == None:
			return await ctx.send(f"Specfy a time please!")
			
		minutes, seconds = divmod(time, 60)
		hours, minutes = divmod(minutes, 60)
		
		add_or_remove = role not in member.roles
		
		if add_or_remove:
			
			if int(hours):
				await member.add_roles(role)
				h = discord.Embed(title="Temp Role Added!",description=f"Added {role.mention} to {member.mention} for: \n **{int(hours)}** hours, **{int(minutes)}** minutes and **{int(seconds)}** seconds",color=0xFFFF00)
				await ctx.send(embed=h)
				await asyncio.sleep(time)
				return await member.remove_roles(role)
				
			
			if int(minutes):
				
				await member.add_roles(role)
				m = discord.Embed(title='Temp Role Added!',description=f"Added {role.mention} to {member.mention} for: \n **{int(minutes)}** minutes and **{int(seconds)}** seconds",color=0xFFFF00)
				await ctx.send(embed=m)
				await asyncio.sleep(time)
				return await member.remove_roles(role)
				
			if int(seconds):
				
				await member.add_roles(role)
				s = discord.Embed(title="Temp Role Added!",description=f"Added {role.mention} to {member.mention} for: \n **{int(seconds)}** seconds",color=0xFFFF00)
				await ctx.send(embed=s)
				await asyncio.sleep(time)
				return await member.remove_roles(role)
				
			
		else:
			await ctx.send(f"This person already has it")
				
	
	
	
	
	

	
	
	@commands.command(aliases=["rm"])
	async def remind(self, ctx, time: TimeConverter=None, *, message="something"):
	
		if not time:
			await ctx.send(f"Okay! I'll remind you in ``10 mins.`` about ``{message}``")
			await asyncio.sleep(600)
			return await ctx.author.send(f"``10 mins.`` ago you asked to be reminded of ``{message}`` \n\n {ctx.message.link}")
			
		else:
			minutes, seconds = divmod(time, 60)
			hours, minutes = divmod(minutes, 60)
			
			if int(hours):
				await ctx.send(f"Okay! I'll remind you in ``{int(hours)} hours, {int(minutes)} mins, {int(seconds)} seconds`` about ``{message}``")
				await asyncio.sleep(time)
				return await ctx.author.send(f"``{int(hours)} hours, {int(minutes)} mins, {int(seconds)} seconds`` ago you asked to be reminded of ``{message}``")
				
			if int(minutes):
				await ctx.send(f"Okay I'll remind you in ``{int(minutes)} mins, {int(seconds)} seconds`` about ``{message}``")
				await asyncio.sleep(time)
				return await ctx.author.send(f"``{int(minutes)} mins, {int(seconds)} seconds`` ago you asked to be reminded of ``{message}``")
		
			if int(seconds):
				await ctx.send(f"Okay! I'll remind you in ``{int(seconds)} seconds`` about ``{message}``")
				await asyncio.sleep(time)
				return await ctx.author.send(f"``{int(seconds)} seconds`` ago you asked to be reminded of ``{message}``")
		
	
		
		
			































def setup(bot):
	bot.add_cog(Roles(bot))