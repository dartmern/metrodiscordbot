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

class currency(commands.Cog):

	def __init__(self, bot):
		self.bot = bot


	@commands.Cog.listener()
	async def on_ready(self):
		print(f"{self.__class__.__name__} Cog has been loaded\n-----")
		
		
		
	@commands.command(aliases=['balance','coins'])
	async def bal(self, ctx, member : discord.Member=None):
	
		data = await self.bot.config.get_by_id(ctx.message.guild.id)
		prefix = data["prefix"] 
	
		if member == None:
			bal = await self.bot.Bal.get_by_id(ctx.author.id)
		
		
			if bal == None:
				await ctx.send(f"Woah there you don't have an account. Type ``{prefix}register``")
				return
			
			coins = bal["botBal"]
			
			e = discord.Embed(
			title=f"{ctx.author.name}'s balance",
			description=f"**Wallet:** {coins} :coin:",
			color=random.choice(self.bot.color_list))
			e.set_footer(text="Imagine being poor")
			await ctx.send(embed=e)
			return

			
		else:
			memberBal = await self.bot.Bal.get_by_id(member.id)
			
			if memberBal == None:
				await ctx.send(f"Woah there this person hasn't even registered yet")
				return
			
			memberCoins = memberBal["botBal"]
			
			e = discord.Embed(
				title=f"{member.name}'s balance",
				description=f"**Wallet:** {memberCoins} :coin:",
				color=random.choice(self.bot.color_list))
			e.set_footer(text="Imagine being poor")
			await ctx.send(embed=e)
		
	@commands.command(aliases=['reg'])
	async def register(self, ctx):
	
		bal = await self.bot.Bal.get_by_id(ctx.author.id)
		
		if bal == None:
			
			data = {"_id": ctx.author.id, "botBal": "250"}
			
			await self.bot.Bal.upsert(data)
			await ctx.send("Great! You now have 250 starting cash")
			
			inv = {"_id" : ctx.author.id, "pig" : 0, "cow" : 0}
			await self.bot.inv.upsert(inv)
			return
			
		else:
			
			await ctx.send("You can't register because you already have money")
	
	

	@commands.command(aliases=['share'])
	@commands.cooldown(rate=1, per=6, type=commands.BucketType.user)
	async def give(self, ctx, member : discord.Member, amount:str):
	
		if member == None:
			await ctx.send("Try running that command but mentioning someone")
			return
	
		bal = await self.bot.Bal.get_by_id(ctx.author.id)
		
		if bal == None:
		
			await ctx.send("You haven't registered! Type ``-reg``")
			return
			
		data = bal["botBal"]
		
		
		data = int(data)
		amount = int(amount)
		if amount > data:
		
			await ctx.send("You don't have that much cash idiot")
			return
			
		else:
			data = int(data)
			amount = int(amount)
			
			sheet = data - amount
			print(sheet)
			
			
			
			newAmount = {"_id":ctx.author.id, "botBal": sheet}
			
			await self.bot.Bal.upsert(newAmount)
			
			oldMemberBal = await self.bot.Bal.get_by_id(member.id)
			realBal = oldMemberBal["botBal"]
			
			realBal = int(realBal)
			amount = int(amount)
			memberBal = realBal + amount
			
			newMemberBal = {"_id":member.id, "botBal":memberBal}
			
			await self.bot.Bal.upsert(newMemberBal)
			await ctx.send(f"Great I Successfully sent ``{amount}`` coins to **{member.name}**")
			await member.send(f"**You have been given coins!** \n\n {ctx.author.mention} has given you **{amount}** :coin:")
	
		
	
	@commands.command()
	@commands.has_role(812513862082363405)
	async def setmoney(self, ctx, amount):
	
		amount = int(amount)
	
		data = {"_id": ctx.author.id, "botBal" : amount}
	
		await self.bot.Bal.upsert(data)
		
		await ctx.send(f"Set your balance to ``{amount}``")
	
			
	
	@commands.command()
	@commands.cooldown(rate=1, per=10, type=commands.BucketType.user)
	async def beg(self, ctx):
	
		amount = random.randint(0,696) 
		
		
		bal = await self.bot.Bal.get_by_id(ctx.author.id)
		oldBal = bal["botBal"]
		oldBal = int(oldBal)

		await ctx.send(f"Take {amount} for begging you idiot")
		
		newBal = amount + oldBal
		data = {"_id" : ctx.author.id, "botBal" : newBal}
		
		await self.bot.Bal.upsert(data)
		
	@commands.command()
	@commands.cooldown(rate=1, per=86400, type=commands.BucketType.user)
	async def daily(self, ctx):
	
		
		
		bal = await self.bot.Bal.get_by_id(ctx.author.id)
		oldBal = bal["botBal"]
		oldBal = int(oldBal)
		
		newBal = oldBal + 10000
		newBal = int(newBal)
		data = {"_id": ctx.author.id, "botBal" : newBal}
	
		await self.bot.Bal.upsert(data)
		
		await ctx.send("Here are your **daily** coins! (10,000)")
		
	
	@commands.command()
	async def rob(self, ctx, member : discord.Member):
	
		if member.bot:
			await ctx.send("You can't rob bots dummy")
			return
			
	
		if member == ctx.author:
			await ctx.send("You idiot you can't rob yourself!")
			return
	
		bal = await self.bot.Bal.get_by_id(ctx.author.id)
		coins = bal["botBal"]
		
		memberBal = await self.bot.Bal.get_by_id(member.id)
		memberCoins = memberBal["botBal"]
		
		coins = int(coins)
		memberCoins = int(memberCoins)
		
		
		if not coins >= 500:
			await ctx.send("You need at least 500 :coin: to rob someone")
			return
			
		if memberCoins <= 999:
			await ctx.send("This person doesn't have at least 1000 :coin: so it's not worth robbing them")
			return
			
	
		amount = random.randint(1,10)
		
		if amount == 1:	
			newCoins = coins + memberCoins
			data = {"_id":ctx.author.id, "botBal":newCoins}
			await self.bot.Bal.upsert(data)
			
			newMemberCoins = {"_id" : member.id, "botBal": "0"}
			await self.bot.Bal.upsert(newMemberCoins)
			
			await ctx.send(f":money_with_wings: **You stole EVERYTHING** LMFAO :money_with_wings: \n Your payout was **{memberCoins}** coins")
			await member.send(f"{ctx.author.mention} just stole **{memberCoins}** from you in {ctx.guild}")
			return
			
			
		if amount == 2:
			newCoins = coins + memberCoins
			data = {"_id":ctx.author.id, "botBal":newCoins}
			await self.bot.Bal.upsert(data)
			
			newMemberCoins = {"_id" : member.id, "botBal": "0"}
			await self.bot.Bal.upsert(newMemberCoins)
			
			await ctx.send(f":money_with_wings: **You stole EVERYTHING** LMFAO :money_with_wings: \n Your payout was **{memberCoins}** coins")
			await member.send(f"{ctx.author.mention} just stole **{memberCoins}** from you in {ctx.guild}")
			return
		
		if amount == 3:
			newCoins = coins + memberCoins
			data = {"_id":ctx.author.id, "botBal":newCoins}
			await self.bot.Bal.upsert(data)
			
			newMemberCoins = {"_id" : member.id, "botBal": "0"}
			await self.bot.Bal.upsert(newMemberCoins)
			
			await ctx.send(f":money_with_wings: **You stole EVERYTHING** LMFAO :money_with_wings: \n Your payout was **{memberCoins}** coins")
			await member.send(f"{ctx.author.mention} just stole **{memberCoins}** from you in {ctx.guild}")
			return
		
		if amount == 4:
			newCoins = coins + memberCoins
			data = {"_id":ctx.author.id, "botBal":newCoins}
			await self.bot.Bal.upsert(data)
			
			newMemberCoins = {"_id" : member.id, "botBal": "0"}
			await self.bot.Bal.upsert(newMemberCoins)
			
			await ctx.send(f":money_with_wings: **You stole EVERYTHING** LMFAO :money_with_wings: \n Your payout was **{memberCoins}** coins")
			await member.send(f"{ctx.author.mention} just stole **{memberCoins}** from you in {ctx.guild}")
			return
		
			
		if amount == 5:
		
			newMembercoins = memberCoins / 3
		
			newCoins2 = coins + newMembercoins
			newCoins2 = int(newCoins2)
			data = {"_id" : ctx.author.id, "botBal":newCoins2}
			await self.bot.Bal.upsert(data)
			
			
			
			newMembercoins = int(newMembercoins)
			
			newOi = memberCoins - newMembercoins
			newOi = int(newOi)
			newMemberCoins2 = {"_id" : member.id, "botBal":newOi}
			await self.bot.Bal.upsert(newMemberCoins2)
			await ctx.send(f":moneybag: You stole **a little bit** of cash :moneybag: \n Your payout was **{newMembercoins}** coins")
			await member.send(f"{ctx.author.mention} just stole **{newMembercoins}** from you in {ctx.guild}")
			return
			
		if amount == 6:
			newMembercoins = memberCoins / 3
		
			newCoins2 = coins + newMembercoins
			newCoins2 = int(newCoins2)
			data = {"_id" : ctx.author.id, "botBal":newCoins2}
			await self.bot.Bal.upsert(data)
			
			
			
			newMembercoins = int(newMembercoins)
			
			newOi = memberCoins - newMembercoins
			newOi = int(newOi)
			newMemberCoins2 = {"_id" : member.id, "botBal":newOi}
			await self.bot.Bal.upsert(newMemberCoins2)
			await ctx.send(f":moneybag: You stole **a little bit** of cash :moneybag: \n Your payout was **{newMembercoins}** coins")
			await member.send(f"{ctx.author.mention} just stole **{newMembercoins}** from you in {ctx.guild}")
			return
		
		if amount == 7:
			newMembercoins = memberCoins / 3
		
			newCoins2 = coins + newMembercoins
			newCoins2 = int(newCoins2)
			data = {"_id" : ctx.author.id, "botBal":newCoins2}
			await self.bot.Bal.upsert(data)
			
			
			
			newMembercoins = int(newMembercoins)
			
			newOi = memberCoins - newMembercoins
			newOi = int(newOi)
			newMemberCoins2 = {"_id" : member.id, "botBal":newOi}
			await self.bot.Bal.upsert(newMemberCoins2)
			await ctx.send(f":moneybag: You stole **a little bit** of cash :moneybag: \n Your payout was **{newMembercoins}** coins")
			await member.send(f"{ctx.author.mention} just stole **{newMembercoins}** from you in {ctx.guild}")
			return
		
			
		if amount == 8:
			await ctx.send("You idiot! You were caught by him trying to steal")
			await ctx.send(f"{ctx.author.mention} tried to steal from you in {ctx.guild} but failed")
			return
		if amount == 9:
			await ctx.send("You idiot! You were caught by him trying to steal")
			await ctx.send(f"{ctx.author.mention} tried to steal from you in {ctx.guild} but failed")
			return
		if amount == 10:
			await ctx.send("You idiot! You were caught by him trying to steal")
			await ctx.send(f"{ctx.author.mention} tried to steal from you in {ctx.guild} but failed")
			return
			
	@rob.error
	async def rob_error(self, ctx, error):
	
		if isinstance(error, commands.errors.MemberNotFound):
			await ctx.send(f"Member Not Found! Try turning off caps lock or mentioning them")
			
		if isinstance(error, commands.errors.MissingRequiredArgument):
			await ctx.send(f"Try running that command again but mentioning someone to rob. (make sure they are in the server)")
			

	
		
	@commands.command()
	async def deposit(self, ctx, amount=0):
	
		if amount == 0:
			await ctx.send(f"Try running that command again but put how much you want to deposit")
	
	
	
	
	
	
	
	
	

def setup(bot):
	bot.add_cog(currency(bot))