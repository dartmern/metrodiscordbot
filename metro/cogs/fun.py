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

		e = discord.Embed(title='Embeds in Metro Discord Bot',description=f'```yaml\nCommand: {prefix}embed``` \n**Please use the following sub-commands:** \n\n\n``channel`` - embeds to selected channel \n ``normal`` - normal embed and sends in current channel \n``delete`` - embeds in current channel but deletes your message \n``delay`` - embeds in the current channel but delays it',color=0x1ABC9C,timestamp=ctx.message.created_at)

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
			
			data = {"_id": ctx.author.id, "botBal":"250"}
			
			await self.bot.Bal.upsert(data)
			await ctx.send("Great! You now have 250 starting cash")
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
	
		respond = [
		"hmmm I'll give you {amount} coins then",
		"eh? your smelly so take {amount} coins ",
		"take yo {amount} coins and leave idiot",
		"awwwww here take {amount} coins ",
		"the person who gave you cash saw that you needed more so take more cash he said and he also said take {amount}",
		"stfu here {amount} coins",
		"take {amount} coins and go treat ya self"
		]
		
		respond = random.choice(respond)
		await ctx.send(respond)
		
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
			

	
		
			
			
			
			
		
	




def setup(bot):
	bot.add_cog(Fun(bot))