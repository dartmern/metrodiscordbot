import asyncio
import platform
import time

import discord
from discord.ext import commands
import  os

class cmds(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.__class__.__name__} Cog has been loaded\n-----")

    @commands.command(aliases=['botinfo','version'],
                      description="View some bot stats!")
    @commands.cooldown(rate=1, per=2, type=commands.BucketType.user)
    async def stats(self, ctx):


        logs = self.bot.get_channel(794747515291041803)
        guild = ctx.guild
        m = discord.Embed(title='Command Used',description=f"**Used by:** {ctx.author.mention} - {ctx.author} - {ctx.author.id} \n **Guild:** {ctx.guild} - {ctx.guild.id} \n **Command:** stats \n **Did it work?** {self.bot.check}",timestamp=ctx.message.created_at, color=0x71368A)
        await logs.send(embed=m)


        pythonVersion = platform.python_version()
        dpyVersion = discord.__version__
        serverCount = len(self.bot.guilds)
        memberCount = len(self.bot.users)

        embed = discord.Embed(title=f'{self.bot.user.name} Stats', description='\uFEFF', colour=0xFFFFFD, timestamp=ctx.message.created_at)

        embed.add_field(name='Bot Version:', value=self.bot.version)
        embed.add_field(name='Python Version:', value=pythonVersion)
        embed.add_field(name='Discord.Py Version', value=dpyVersion)
        embed.add_field(name='Total Guilds:', value=serverCount)
        embed.add_field(name='Total Users:', value=memberCount)
        embed.add_field(name='Bot Developers:', value="<@525843819850104842> dartmern#7563 \n<@716441826982232125> Gamer97878#0516 \n<@708143475186597909> Pickles#0751")

        embed.set_footer(text=f"©Metro 2020 | {self.bot.user.name}")
        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)

        await ctx.send(embed=embed)
        

    @commands.command(aliases=['disconnect', 'close', 'stopbot'],hidden=True)
    @commands.has_role(812513862082363405)
    async def logout(self, ctx):

        logs = self.bot.get_channel(794747515291041803)
        guild = ctx.guild
        m = discord.Embed(title='Command Used',description=f"**Used by:** {ctx.author.mention} - {ctx.author} - {ctx.author.id} \n **Guild:** {ctx.guild} - {ctx.guild.id} \n **Command:** logout \n **Did it work?** {self.bot.check}",timestamp=ctx.message.created_at, color=0x71368A)
        await logs.send(embed=m)

        def check(message):
            return message.author == ctx.author and message.channel == ctx.channel and message.content.lower() == "logout"


        embed = discord.Embed(title=f'Logout of {self.bot.user.name}?',description='Reply with ``logout`` to confirm. You have 5 seconds to reply',color=0xE74C3C)
        await ctx.send(f'{ctx.author.mention}',embed=embed)

        await self.bot.wait_for('message', check=check, timeout=5)
        await asyncio.sleep(1)

        em = discord.Embed(title=f'Logout of {self.bot.user.name} successful!',description=f'I successfully logged out of {self.bot.user.name} and is offline.',color=0x2ECC71)

        await ctx.send(embed=em)
        await self.bot.logout()






    @commands.command(aliases=['bl'],hidden=True)
    @commands.is_owner()
    async def blacklist(self, ctx, user: discord.Member, reason=None):


        await self.bot.blacklist.upsert({"_id": user.id})

        await ctx.send(f"Blacklisted **{user.name}** for you.")
        await user.send(f"You have been permanently blacklisted by a bot moderator from Metro Discord Bot \n\n You can appeal in our support server: https://discord.gg/tVutR342Sq \n\n **Reason:** {reason}")
		

    @commands.command(aliases=['ub'],hidden=True)
    @commands.is_owner()
    async def unblacklist(self, ctx, user: discord.Member, reason=None):

        await self.bot.blacklist.delete_by_id(user.id)

        await ctx.send(f"Unblacklisted **{user.name}** for you.")
        await user.send(f"You have been unblacklisted by a bot moderator from Metro Discord Bot for the reason: {reason}")



    @commands.group(invoke_without_command=True,case_insensitive=True)
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 5, commands.BucketType.guild)
    async def prefix(self, ctx):

        data = await self.bot.config.get_by_id(ctx.message.guild.id)
        prefix = data["prefix"] 

        e = discord.Embed(title='Change prefix in Metro Discord Bot',description=f'```yaml\nCommand: {prefix}prefix``` \n**Please use the following sub-commands:** \n \n\n``set`` - changes the existing prefix to the one you select \n ``remove`` - remove a prefix \n ``list`` - list all the prefixes on this server \n``reset`` - reset all the prefixes',color=0x1ABC9C,timestamp=ctx.message.created_at)

        await ctx.send(embed=e)

    @prefix.command()
    async def set(self, ctx, prefix):

        await self.bot.config.upsert({"_id": ctx.guild.id, "prefix": prefix})

        e = discord.Embed(title='Prefix Changed!',description=f'```yaml\nCommand: {prefix}prefix set``` \n \n **Prefix changed successfully** \n \n Use ``{prefix}prefix`` for help on prefixes',color=0x2ECC71,timestamp=ctx.message.created_at)
        await ctx.send(embed=e)




    





    @commands.command()
    async def typing(self, ctx, time=5):
        
        if time > 30:
            await ctx.send("That time is too long")
            return
        async with ctx.typing():
            await ctx.send(f"Alright. I'm typing right now for {time} seconds")
            await asyncio.sleep(time)
            

    @commands.command(aliases=['support','links','socials','twitter'])
    async def invite(self, ctx):


        e = discord.Embed(title='Links for Metro Discord Bot',description='[Invite Metro](https://dsc.gg/metro) - Add Metro to another server! \n [Metro on Twitter](https://twitter.com/MetroDiscordBot) - Follow us for updates! \n [Support Server](https://dsc.gg/metrosupport) - Join to ask questions and hangout!',color=0xFFFFFD)
        await ctx.send(embed=e)


    @commands.command(name="ping")
    async def ping(self, ctx):
        """Get the bot's current websocket and API latency."""
        start_time = time.time()
        message = await ctx.send("Testing Ping...")
        end_time = time.time()

        await message.edit(content=f"Pong! {round(self.bot.latency * 1000)}ms\nAPI: {round((end_time - start_time) * 1000)}ms")



		
    








def setup(bot):
    bot.add_cog(cmds(bot))