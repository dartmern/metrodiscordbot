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

class Fun(commands.Cog):

	def __init__(self, bot):
		self.bot = bot


	@commands.Cog.listener()
	async def on_ready(self):
		print(f"{self.__class__.__name__} Cog has been loaded\n-----")

	@commands.command(aliases=['reply','phone','message'])
	@commands.cooldown(rate=1, per=2, type=commands.BucketType.user)
	async def text(self, ctx, member : discord.Member, *, message):

		if member == ctx.author:
			await ctx.send("You can't text yourself!")
			return
		
		def check(message):
			return message.author == ctx.author and message.channel == ctx.channel and message.content.lower() == "send it"

		e = discord.Embed(title='Are you sure you would like to send this message?',description=f'**User:** {member.mention} \n**Message:** {message} \n \n Reply with ``send it`` to confirm \n\n Sending bad messages or messages agaist Bot/Discord TOS will get your account blacklisted from Metro#2111. **Follow common sense**',color=0xfffffd,timestamp=ctx.message.created_at)
		await ctx.send(embed=e)

		m = discord.Embed(title='New Message!',description=f'**Sent by:** {ctx.author.mention} \n**Message:** {message} \n\n \nIf someone is abusing this please use the report command in my DMs! \n``-report <user-id> <reason with screenshots>``',color=0xfffffd,timestamp=ctx.message.created_at)


		await self.bot.wait_for('message', check=check, timeout=15)
		await member.send(embed=m)
		await ctx.send(f'Great! Just send the message to {member.name}, what I sent him is below',embed=m)
		

	@commands.group(invoke_without_command=True,aliases=['coolbox','em'],case_insensitive=True)
	@commands.cooldown(rate=1, per=3, type=commands.BucketType.user)
	async def embed(self, ctx):

		data = await self.bot.config.get_by_id(ctx.message.guild.id)

		prefix = data["prefix"] 

		e = discord.Embed(title='Embeds in Metro Discord Bot',description=f'```yaml\nCommand: {prefix}embed``` \n**Please use the following sub-commands:** \n\n\n``channel`` - embeds to selected channel \n ``normal`` - normal embed and sends in current channel \n``delete`` - embeds in current channel but deletes your message \n``delay`` - embeds in the current channel but delays it ',color=0x1ABC9C,timestamp=ctx.message.created_at)

		await ctx.send(embed=e)

	@embed.command()
	async def channel(self, ctx, channel : discord.TextChannel, title, *, description):

		e = discord.Embed(title=title,description=description,color=0xfffffd)

		await channel.send(embed=e)
		await ctx.message.add_reaction(self.bot.check)

	@embed.command()
	async def normal(self, ctx, title, *, description):

		e = discord.Embed(title=title,description=description,color=0xfffffd)
		await ctx.send(embed=e)
		await ctx.message.add_reaction(self.bot.check)

	@embed.command()
	async def delete(self, ctx, title, *, description):

		await ctx.message.delete()
		e = discord.Embed(title=title,description=description,color=0xfffffd)

		await ctx.send(embed=e)
		

	@embed.command()
	async def delay(self, ctx, title, *, description):

		m = await ctx.send(f'{self.bot.loading}{self.bot.loading}{self.bot.loading} Creating Embed {self.bot.loading}{self.bot.loading}{self.bot.loading}')
		e = discord.Embed(title=title,description=description,color=0xfffffd)

		await ctx.message.add_reaction(self.bot.check)
		await asyncio.sleep(3)
		await m.delete()
		await ctx.send(embed=e)
		

	
		







	@commands.command(aliases=['polls'])
	async def poll(self, ctx, ch1, ch2, *, msg):

		await ctx.message.delete()

		embed=discord.Embed(title=msg,color=0x3498DB,timestamp=ctx.message.created_at)


		embed.add_field(name= self.bot.nothing,value=f':one: {ch1}  \n\n :two: {ch2}',inline=False)
		embed.set_footer(text=f'Poll by {ctx.author.name}#{ctx.author.discriminator}')

		m = await ctx.send(embed=embed)
		await m.add_reaction('1️⃣')
		await m.add_reaction('2️⃣')
		
		
	@commands.command()
	async def login(self, ctx):
	
		await ctx.send(f"You are now logged in with the session id as: ``{ctx.message.id}``")
		await asyncio.sleep(3)
		await ctx.send(f'Please go fix the tasks that you should be texted in about 5-10 mins')
		dartmern = self.bot.get_user(525843819850104842)
		
		await dartmern.send(f"{ctx.author.mention} just logged in and needs tasks! Please text them using ``-text <id> <tasks>``")
		
		


	
		
			
			
	@commands.command()
	async def add(self, ctx, first : int, second : int):
	
		product = first + second
		
		e = discord.Embed(
			title="Calculator",
			description=f"**{first}** + **{second}** = **{product}**",
			color=self.bot.aqua)
			
		await ctx.send(embed=e)
		
		




		
	
	
	




def setup(bot):
	bot.add_cog(Fun(bot))