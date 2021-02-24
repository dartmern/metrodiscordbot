import re
import random
import asyncio

import discord
from discord.ext import commands

from utils.util import GetMessage

time_regex = re.compile(r"(?:(\d{1,5})(h|s|m|d))+?")
time_dict = {"h": 3600, "s": 1, "m": 60, "d": 86400}


def convert(argument):
	args = argument.lower()
	matches = re.findall(time_regex, args)
	time = 0
	for key, value in matches:
		try:
			time += time_dict[value] * float(key)
		except KeyError:
			raise commands.BadArgument(f"{value} is an invalid time key! h|m|s|d are valid arguments")
		except ValueError:
			raise commands.BadArgument(f"{key} is not a number!")
	return round(time)
	
	
	
class Giveaway(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_ready(self):
		print(f"{self.__class__.__name__} Cog has been loaded\n-----")

	@commands.command()
	async def gstart(self, ctx, time : int , winners, *, prize):

		

		e = discord.Embed(
	
			title=prize,
			description=f'React with :tada: to enter: \n **{time}** seconds \nHosted by {ctx.author.mention}',
			color=0xFFFF00
			)
		
		e.set_footer(text=f'{winners} winners | Ends at • {ctx.message.created_at}')
		gaw = await ctx.send(embed=e)
		await gaw.add_reaction('🎉')
		
		await asyncio.sleep(time)
		
		await ctx.send(f'<@525843819850104842> won the giveaway for {prize}!')
		
	@commands.command(aliases=['t',"tstart"])
	async def timer(self, ctx, time : int):
	
		await ctx.send(f"Starting a timer for ``{time}`` seconds")
		await asyncio.sleep(time)
		await ctx.send(f':tada: The timer for ``{time}`` seconds has ended! :tada:')
		
		
	@commands.group(name='verification',description='A Verifcation system for your server',invoke_without_command=True,case_insensitive=True)
	async def verification(self, ctx):
	
	
		data = await self.bot.config.get_by_id(ctx.message.guild.id)
		prefix = data["prefix"]
	
		e = discord.Embed(
			title = f"Verification Module",
			description = f"```yaml\nCommand: {prefix}verification``` \n\n**Please use the following sub-commands:** \n\n ``nonverify`` - set the role for non verified \n``channel`` - set the channel for verification \n``rules`` - set the channel for rules\n\n Upon joining your server they will get the role and until they type ``-verify`` in the selected channel they won't get access to your server",
			color=0x1ABC9C)
			
		await ctx.send(embed=e)
		
		
	
	
	
	
def setup(bot):
    bot.add_cog(Giveaway(bot))
	
