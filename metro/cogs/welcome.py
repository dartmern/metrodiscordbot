import discord
from discord.ext import commands


from discord.ext.commands.cooldowns import BucketType
import asyncio

from string import Template

def substitute_args(message, member) -> str:

	return Template(message).safe_substitute(
        {
            "MENTION": member.mention,
			"MEMBER": member,
			"ID": member.id,
			"NAME": member.name,
			'DISCRIM': member.discriminator,
			"GUILD": member.guild,
		
        }
        )



class Welcome(commands.Cog):

	def __init__(self, bot):
		self.bot = bot



	@commands.Cog.listener()
	async def on_ready(self):
		print(f"{self.__class__.__name__} Cog has been loaded\n-----")



	@commands.Cog.listener()
	async def on_member_join(self, member):



		await asyncio.sleep(1)

		welcomeChannel = await self.bot.welcomeChannel.get_by_id(member.guild.id)
		welcomeMsg = await self.bot.welcomeMsg.get_by_id(member.guild.id)

		channel = welcomeChannel["channel"]
		message = welcomeMsg['message']

		msg = substitute_args(message=message, member=member)

		welcome = self.bot.get_channel(channel)
		await welcome.send(msg)




	@commands.group(invoke_without_command=True,case_insensitive=True)
	async def welcome(self, ctx):
		
		data = await self.bot.config.get_by_id(ctx.message.guild.id)
		prefix = data["prefix"]
		
		e = discord.Embed(title='Welcome Module',description=f'```yaml\nCommand: {prefix}welcome``` \n \n**Please use the following sub-commands:** \n\n\n ``channel`` - set the channel to send welcome messages \n``message`` - set the message sent in welcome channel\n``variables`` - see variables/args you can use in welcome message \n``test`` - test your welcome message and channel  ',color=0x1ABC9C,timestamp=ctx.message.created_at)

			
		
		await ctx.send(embed=e)

	@welcome.command()
	async def channel(self, ctx, channel : discord.TextChannel):
	
		data = await self.bot.config.get_by_id(ctx.message.guild.id)
		prefix = data["prefix"] 


		data = {"_id": ctx.guild.id, 'channel': channel.id}

		await self.bot.welcomeChannel.upsert(data)

		await ctx.send(f'Nice! I just set the welcome channel to: {channel.mention} ``{channel.id}``')

	@welcome.command(aliases=['msg'])
	async def message(self, ctx, *, message):

		data = await self.bot.config.get_by_id(ctx.message.guild.id)
		prefix = data["prefix"] 

		data = {'_id': ctx.guild.id, 'message':message}

		await self.bot.welcomeMsg.upsert(data)

		await ctx.send(f'Nice your welcome message is below: \n``{message}``')
		
	@welcome.command(aliases=['args','varib'])
	async def variables(self, ctx):
	
		data = await self.bot.config.get_by_id(ctx.message.guild.id)
		prefix = data["prefix"]
		
		e = discord.Embed(title='Welcome Message Variables',description=f"```yaml\nCommand: {prefix}welcome variables``` \n\n The following are variables to make your welcome message more spicier. \n\n ``$MEMBER`` - the member's name and tag \n``$MENTION`` - the member's mention\n``$ID`` - the member's id \n``$NAME`` - the member's name\n``$DISCRIM`` - the member's tag without # \n\n ``$GUILD`` - the guild's name\n\n Make sure you put them in caps and look at example below: \n **{prefix}welcome message Welcome to our server $MENTION!**",color=0x1ABC9C,timestamp=ctx.message.created_at)
		
		
		await ctx.send(embed=e)
	
	@welcome.command()
	async def test(self, ctx):
	
		data = await self.bot.config.get_by_id(ctx.message.guild.id)
		prefix = data["prefix"]
		
		member = ctx.author
		
		welcomeChannel = await self.bot.welcomeChannel.get_by_id(member.guild.id)
		welcomeMsg = await self.bot.welcomeMsg.get_by_id(member.guild.id)
		
		if welcomeChannel == None:
		
			await ctx.send(f"You haven't set a channel yet! Set one by running: \n``{prefix}welcome channel <channel>``")
			return
		
		if welcomeMsg == None:
		
			await ctx.send(f"You haven't set a message yet! Set one by running: \n``{prefix}welcome message <message>``")
			return
		channel = welcomeChannel["channel"]
		message = welcomeMsg['message']
		

			
		msg = substitute_args(message=message, member=member)
	
		welcome = self.bot.get_channel(channel)
		await welcome.send(msg)
		await ctx.send(f'I just sent a test message to {welcome.mention} \n (Note: It might still have the varibles but it will work)')	
	
	

			
			
			
		
		
		
	
		
	@channel.error
	async def channel_error(self, ctx, error):
		
		
		if isinstance(error, commands.MissingRequiredArgument):
			await ctx.send('Please put in a channel to make this work \n (Can be a channel name, mention, or id)')
		if isinstance(error, commands.errors.ChannelNotFound):
			await ctx.send("This channel wasn't found. Check for spacing, caplization, or try to mention the channel")		
		else:
			raise error
			
	@message.error
	async def message_error(self, ctx, error):

	
		data = await self.bot.config.get_by_id(ctx.message.guild.id)
		prefix = data["prefix"]
	
		if isinstance(error, commands.MissingRequiredArgument):
		
			await ctx.send(f'Please put a message to make this work \n To see the variables you can use run ``{prefix}welcome args``')
			

			
		
























def setup(bot):
    bot.add_cog(Welcome(bot))



