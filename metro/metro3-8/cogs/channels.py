import re
import math
import random

import discord
from discord.ext import commands
import platform
import datetime


from discord.ext.commands.cooldowns import BucketType
import asyncio

import utils.json_loader
from utils.mongo import Document



class Channels(commands.Cog):

	def __init__(self, bot):
		self.bot = bot



	@commands.Cog.listener()
	async def on_ready(self):
		print(f"{self.__class__.__name__} Cog has been loaded\n-----")

	@commands.command(aliases=['cs'])
	@commands.bot_has_guild_permissions(manage_channels=True)
	async def channelstats(self, ctx):
		channel = ctx.channel

		embed = discord.Embed(title=f"Channel Stats for **{channel.name}**", description=f"{'Category: {}'.format(channel.category.name) if channel.category else 'This channel is not in a category'}", color=0x34495E)
		embed.add_field(name="Channel Guild", value=ctx.guild.name, inline=True)
		embed.add_field(name="Channel Id", value=channel.id, inline=True)
		embed.add_field(name="Channel Topic", value=f"{channel.topic if channel.topic else 'No topic.'}", inline=True)
		embed.add_field(name="Channel Position", value=channel.position, inline=True)
		embed.add_field(name="Channel Slowmode Delay", value=channel.slowmode_delay, inline=True)
		embed.add_field(name="Channel is NSFW?", value=channel.is_nsfw(), inline=True)
		embed.add_field(name="Channel is Annoucements?", value=channel.is_news(), inline=True)
		embed.add_field(name="Channel Creation Time", value=channel.created_at, inline=True)
		embed.add_field(name="Channel Permissions Synced", value=channel.permissions_synced, inline=True)
		embed.add_field(name="Channel Hash", value=hash(channel), inline=True)

		await ctx.send(embed=embed)
		
		
	@commands.command()
	async def report(self, ctx, member : discord.Member, *,reason=None):
	
		await ctx.send(f"Thanks for submitting the report please wait 2-3 days and you'll get a DM from <@788543184082698252> and not anyone else. You will get a DM weather it was accepted or not. If you have more reports please do them in my DMs by using the command: ``-report <user-id> <reason with screenshots>`` \n\n\n Report ID: {ctx.message.id}")
		dartmern = self.bot.get_user(525843819850104842)
		channel = self.bot.get_channel(812193283803447316)
		
		await channel.send(f'A report was submitted! \n\n User: {ctx.author.mention} \n User Id: {ctx.author.id} \n\n Report ID: {ctx.message.id} \n\n \n Report Details: \n\n**Person reported:** {member.mention} ({member.id}) \n**Reason:** {reason}')
		await dartmern.send(f'A report was submitted! Please go check <#812193283803447316>')
		


	









def setup(bot):
    bot.add_cog(Channels(bot))
