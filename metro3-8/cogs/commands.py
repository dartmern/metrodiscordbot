import asyncio
import platform
import time
import datetime

import discord
from discord.ext import commands
import os

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




    





            

    @commands.command(aliases=['support','links','socials','twitter'])
    async def invite(self, ctx):


        em = discord.Embed(
            title="Invite Links",
            description="> [Metro Bot Invite (admin)](https://discord.com/oauth2/authorize?client_id=788543184082698252&permissions=8&scope=bot) \n > [Metro Bot Invite (regular)](https://discord.com/oauth2/authorize?client_id=788543184082698252&permissions=470150352&scope=bot) \n\n> [Metro Support Server](https://discord.gg/2ceTMZ9qJh)",
            color=self.bot.aqua,
            timestamp=ctx.message.created_at
        )
        await ctx.reply(embed=em,mention_author=False)

    @commands.command(aliases=["info"],description=f"Get information about Metro")
    async def information(self, ctx):
        """Get bot information"""

        em = discord.Embed(
            title="Metro Information",
            description=f"• `{ctx.prefix}help [command]` - Get help on a command or see all the commands \n\n• `{ctx.prefix}stats` - View Metro's stats like guilds, member, etc\n\n• `{ctx.prefix}uptime` - View Metro's uptime \n\n• `{ctx.prefix}ping` - View Metro's latency/ping\n\n• `{ctx.prefix}links` - View Metro's links such as invite and support server \n\n\n**Still need help?**\n- Join our [ [ `SUPPORT SERVER` ] ](https://discord.gg/2ceTMZ9qJh) for additional help and support!",
            color=self.bot.green,
            timestamp=ctx.message.created_at
        )
        await ctx.reply(embed=em,mention_author=False)


    @commands.command(name="ping")
    async def ping(self, ctx):
        """Get the bot's current websocket and API latency."""

        await ctx.send(f"{self.bot.loading} Pinging . . .",delete_after=0.5)
        await asyncio.sleep(1)

        em = discord.Embed(
            title="Pong!",
            description=f"Discord WebSocket Latency: {round(self.bot.latency * 1000)}ms",
            color=self.bot.green
        )
        start_time = time.time()
        message = await ctx.reply(embed=em,mention_author=False)


        end_time = time.time()
        await asyncio.sleep(1.5)

        send_lag = round((end_time - start_time) * 1000)

        em = discord.Embed(
            title="Pong!",
            description=f"Discord WebSocket Latency: {round(self.bot.latency * 1000)}ms \nSend Messages Latency: {send_lag}ms",
            color=self.bot.green
        )
        start_time = time.time()

        await message.edit(embed=em)
        end_time = time.time()
        await asyncio.sleep(1.5)

        editlag = round((end_time - start_time) * 1000)

        em = discord.Embed(
            title="Pong!",
            description=f"Discord WebSocket Latency: {round(self.bot.latency * 1000)}ms \nSend Messages Latency: {send_lag}ms\nEdit Messages Latency: {editlag}ms",
            color=self.bot.green
        )

        await message.edit(embed=em)
        await asyncio.sleep(1.5)

        overalllag = round(self.bot.latency * 1000) + send_lag + editlag
        overalllag = round(overalllag / 3)

        em = discord.Embed(
            title="Pong!",
            description=f"Discord WebSocket Latency: {round(self.bot.latency * 1000)}ms \nSend Messages Latency: {send_lag}ms\nEdit Messages Latency: {editlag}ms\n\n**Overall Latency:** {overalllag}ms",
            color=self.bot.green
        )
        await message.edit(embed=em)

        await asyncio.sleep(1.5)

        em = discord.Embed(
            title="Pong!",
            description=f"Discord WebSocket Latency: {round(self.bot.latency * 1000)}ms \nSend Messages Latency: {send_lag}ms\nEdit Messages Latency: {editlag}ms\n\n**Overall Latency:** {overalllag}ms\n\nDiscord Status: [Click Here](https://discordstatus.com)\nSupport Server: [Click Here](https://discord.gg/2ceTMZ9qJh)",
            color=self.bot.green
        )
        em.set_footer(text="Join my support server to report high latency!")
        await message.edit(embed=em)


    @commands.command()
    async def uptime(self, ctx):

        data = await self.bot.stats.get_by_id(788543184082698252)
        old = data["uptime"]
        now = datetime.datetime.now()

        new = now - old
        time_seconds = int(new.total_seconds())

        minutes, seconds = divmod(time_seconds, 60)
        hours, minutes = divmod(minutes, 60)
        days, hours = divmod(hours, 24)

        if int(days):
            time = f"**{days}** days, **{hours}** hours, **{minutes}** minutes, **{seconds}** seconds"
        if int(hours) and int(days) is 0:
            time = f"**{hours}** hours, **{minutes}** minutes, **{seconds}** seconds"
        if int(minutes) and int(hours) is 0:
            time = f"**{minutes}** minutes, **{seconds}** seconds"
        if int(seconds) and int(minutes) is 0:
            time = f"**{seconds}** seconds"


        em = discord.Embed(
            title="Metro Discord Bot's Uptime",
            description=f"Been up for: {time}",
            color=self.bot.green
        )
        await ctx.reply(embed=em,mention_author=False)




    @commands.command()
    async def faq(self, ctx):

        em = discord.Embed(
            title="Metro Discord Bot's FAQ",
            description='**FAQ #1:** How do I start a giveaway?\n**A:** Use the command: `-g start <time> <winners> <prize>`\n\n**FAQ #2:** How do I start a timer? \n**A:** Use the command: `-t start <time> [name="Timer"]`\n\n**FAQ #3:** How do I set the muted role?\n**A:** Run the command: `-set muteRole <role>`',
            color=self.bot.aqua
        )
        await ctx.send(embed=em)

    @commands.command()
    async def readb4(self, ctx):
        await ctx.message.delete()

        em = discord.Embed(
            title="Metro Discord Bot's FAQ",
            description='**FAQ #1:** How do I start a giveaway?\n**A:** Use the command: `-g start <time> <winners> <prize>`\n\n**FAQ #2:** How do I start a timer? \n**A:** Use the command: `-t start <time> [name="Timer"]`\n\n**FAQ #3:** How do I set the muted role?\n**A:** Run the command: `-set muteRole <role>`',
            color=self.bot.aqua
        )
        msg = await ctx.send(embed=em)

        em = discord.Embed(
            title="Why is the bot so slow/offline?",
            description="If the bot is offline/slow please check out <#813641674071998484> for updates. If you don't find anything there try asking in <#814210882557050930>",
            color=self.bot.orange
        )
        msg2 = await ctx.send(embed=em)
        
        em = discord.Embed(
            title="Read before asking questions in support!",
            description=f"• See if your question is [answered here](https://discord.com/channels/812143286457729055/{ctx.channel.id}/{msg.id}) \n• If your question is about the bot being slow/offline [read here](https://discord.com/channels/812143286457729055/{ctx.channel.id}/{msg2.id}) \n• Is the bot not responding but online? Try giving the bot **Administrator** permissions. \n\nIf your question isn't answered above please ask your question in <#814210882557050930> and do **not** ping anyone. (even people who you think may be staff)",
            color=self.bot.green
        )
        await ctx.send(embed=em)

    @commands.command()
    async def sup(self, ctx):

        await ctx.message.delete()

        channel = self.bot.get_channel(814210882557050930)

        em = discord.Embed(
            title="Support Guidelines",
            description="• Read <#834562553413238819> before posting here to see if your question is answered \n• Do not ping staff, or anyone you think is staff \n• Have patience. We are not required to help you\n\n• Please keep off-topic conversation in <#812143286969040979>",
            color=self.bot.yellow
        )
        await channel.send(embed=em)


    @commands.command()
    async def noping(self, ctx, member : discord.Member = None, *, reason=None):

        if reason is None:
            reason = '\n'


        await ctx.message.delete()

        if not member is None:
            return await ctx.send(f"{member.mention} **Do not ping anyone in replies or messages**\n{reason}")
        else:
            return await ctx.send(f"**Do not ping anyone in replies or messages**\n{reason}")









		
    








def setup(bot):
    bot.add_cog(cmds(bot))