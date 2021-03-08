import discord
from discord.ext import commands
import platform
import datetime
import random

from discord.ext.commands.cooldowns import BucketType
import asyncio
import os

import traceback

import time

class cmds(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.__class__.__name__} Cog has been loaded\n-----")

    @commands.command(aliases=['status','botinfo','version'])
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
        

    @commands.command(aliases=['disconnect', 'close', 'stopbot'])
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






    @commands.command(aliases=['bl'])
    @commands.is_owner()
    async def blacklist(self, ctx, user: discord.Member, reason=None):


        await self.bot.blacklist.upsert({"_id": user.id})

        await ctx.send(f"Blacklisted **{user.name}** for you.")
        await user.send(f"You have been permanently blacklisted by a bot moderator from Metro Discord Bot \n\n You can appeal in our support server: https://discord.gg/tVutR342Sq \n\n **Reason:** {reason}")
		

    @commands.command(aliases=['ub'])
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

    @prefix.command(aliases=['del','delete'])
    async def remove(self, ctx, prefix):

        await ctx.send(f'removed: {prefix}')

    @prefix.command()
    async def list(self, ctx):
        await ctx.send('here are all the prefixes: ')

    @prefix.command()
    async def reset(self, ctx):

        await ctx.send(f'ARE YOU FUCKING SURE YOU WANT TO RESET ALL YOUR PREFIXES?')

    



    @commands.command(name='reload', description="Reload all/one of the bots cogs!")
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
                await ctx.send(embed=embed)

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

    @commands.command(aliases=['gimmeboost','gb','gp'])
    @commands.cooldown(1, 5, commands.BucketType.guild)
    async def gimmeperks(self, ctx):
		
	
       
        if channel == ctx.channel:
            e = discord.Embed(title='Thanks so much for donating/boosting!',description='Enjoy [donator/booster perks](https://discord.com/channels/774738985355837470/793973271833083924/793976661237825596) for 30 days!',color=0xE91E63,timestamp=ctx.message.created_at)
            await channel.set_permissions(ctx.author, send_messages=False, read_messages=True, add_reactions=False)
            await ctx.author.send('Thanks for donating/boosting once again! Go to the following message link for perks: \n <https://discord.com/channels/774738985355837470/793973271833083924/793976661237825596> \n If something is wrong DM <@525843819850104842>')
            await ctx.send(embed=e)
            m = discord.Embed(title='Command Used',description=f"**Used by:** {ctx.author.mention} - {ctx.author} - {ctx.author.id} \n **Guild:** {guild} - {guild.id} \n **Command:** gimmeperks \n **Did it work?** {self.bot.check}",timestamp=ctx.message.created_at, color=0x71368A)
            await logs.send(embed=m)

            return

        if support == ctx.channel:
            await ctx.send("Go run this command in <#793973271833083924>! If you can't see it that means you didn't donate/boost :sob: DM dartmern#6969 if this is a mistake.")
            m = discord.Embed(title='Command Used',description=f"**Used by:** {ctx.author.mention} - {ctx.author} - {ctx.author.id} \n **Guild:** {guild} - {guild.id} \n **Command:** gimmeperks \n **Did it work?** {self.bot.cross} - either didn't donate/boost or didn't run in proper channel but did run in support server ",timestamp=ctx.message.created_at, color=0x71368A)
            await logs.send(embed=m)
            return

        if bot_cmd == ctx.channel:
            await ctx.send("Go run this command in <#793973271833083924>! If you can't see it that means you didn't donate/boost :sob: DM dartmern#6969 if this is a mistake.")
            m = discord.Embed(title='Command Used',description=f"**Used by:** {ctx.author.mention} - {ctx.author} - {ctx.author.id} \n **Guild:** {guild} - {guild.id} \n **Command:** gimmeperks \n **Did it work?** {self.bot.cross} - either didn't donate/boost or didn't run in proper channel but did run in support server ",timestamp=ctx.message.created_at, color=0x71368A)
            await logs.send(embed=m)
            return



        else:
            await ctx.send('bro go run this in our support server \n discord.gg/Pmavu9DV2J')
            m = discord.Embed(title='Command Used',description=f"**Used by:** {ctx.author.mention} - {ctx.author} - {ctx.author.id} \n **Guild:** {guild} - {guild.id} \n **Command:** gimmeperks \n **Did it work?** {self.bot.cross} - didn't run in support server",timestamp=ctx.message.created_at, color=0x71368A)
            await logs.send(embed=m)
            return


    @commands.command()
    @commands.has_any_role(789168729451659264,789576204508069929,789168777446817823,812513862082363405)
    async def support_pin(self, ctx):

        guild = ctx.guild

        await ctx.message.delete()

        e = discord.Embed(title='Support Channel for Metro#2111',description='Ping <@&789168729451659264> and ask your question! Try not to ask if it is answered in the FAQ  \n  (Channel will be purge at the end of each day)',color=0x1ABC9C)
        e.add_field(name="Metro's FAQ",value=" \u3164 \n **Q:** I donated/boosted server and I didn't get my perks? \n**A:** There should be a channel called <#793973271833083924> If you don't see it then you didn't boost/donate. If this is a mistake DM <@525843819850104842> \n\n**Q:** How do I invite bot? \n**A:** Click on [this link](https://dsc.gg/metro) to invite Metro to your server \n\n **Q:** Why is support staff so slow? \n**A:** Support Staff Team is 100% volunteers and we are humans so we are not as fast as robots. Please kinda wait and don't DM staff. \n\n **Q:** Why is the bot offline? \n**A:** Check out <#789007891583336450> for the status of the bot and the bot is currently in BETA and won't be online all the time. We are sorry about this",inline=True)

    @commands.command(name="ping")
    async def ping(self, ctx):
        """Get the bot's current websocket and API latency."""
        start_time = time.time()
        message = await ctx.send("Testing Ping...")
        end_time = time.time()

        await message.edit(content=f"Pong! {round(self.bot.latency * 1000)}ms\nAPI: {round((end_time - start_time) * 1000)}ms")



		
    








def setup(bot):
    bot.add_cog(cmds(bot))