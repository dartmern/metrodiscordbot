import discord
from discord.ext import commands
import re
import asyncio
import datetime

import random

from utils.util import Pag

time_regex = re.compile("(?:(\d{1,5})(h|s|m|d))+?")
time_dict = dict(h=3600, s=1, m=60, d=86400)



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



class Timer(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.__class__.__name__} Cog has been loaded\n-----")

    @commands.command(aliases=["tend","tcancel","tlist","tsettings"],hidden=True)
    async def tstart(self, ctx):

        e = discord.Embed(
            title="Commands have changed!",
            description=f"All timer commands have been made into one big sub-command! \n\n Run ``{ctx.prefix}timer`` for more details!",
            color=self.bot.red,
            timestamp=ctx.message.created_at
        )
        await ctx.reply(embed=e, mention_author=False)


    @commands.group(name="timer",aliases=["t"],
                    description="Start, stop, configure timers with Metro!",
                    invoke_without_command=True,case_insensitive=True)
    @commands.has_guild_permissions(manage_guild=True)
    async def _timer(self, ctx):


        e = discord.Embed(
            title="Timers in Metro",
            description=f"```yaml\nCommand: {ctx.prefix}timer \nAliases: {ctx.prefix}t``` \n**{ctx.command.description}** \n\n**Sub-commands for timers:** \n``start`` - instantly start a timer\n``end`` - end a timer early\n``list`` - list all the on-going timers in the guild",
            color=self.bot.aqua,
            timestamp=ctx.message.created_at
        )
        e.set_footer(text="This command is currently under development and report bugs to support!")
        await ctx.reply(embed=e, mention_author=False)

    @_timer.command(name="start",description="Instantly start a new timer!")
    @commands.cooldown(1, 1.5, commands.BucketType.default)
    async def _start(self, ctx, time : TimeConverter, *, timer="Timer"):

        time_int = time

        if ctx.channel.is_news():
            await ctx.message.add_reaction(self.bot.cross)
            return await ctx.reply("You cannot make timers in annoucement channels!",mention_author=False)

        if time < 3:
            await ctx.message.add_reaction(self.bot.cross)
            return await ctx.reply("Timers cannot be shorter than 3 seconds",mention_author=False)
        if time > 604800:
            await ctx.message.add_reaction(self.bot.cross)
            return await ctx.reply("Timers cannot be longer than 7 days!",mention_author=False)

        current_timer_count = len(
            await self.bot.timers.find_many_by_custom(
                {
                    "guild": ctx.guild.id
                }
            )
        )

        data = await self.bot.premium.find(ctx.message.guild.id)
        if data is None:

            if current_timer_count >= 20:
                await ctx.message.add_reaction(self.bot.cross)
                return await ctx.reply("You have reached the max amount of timers in this guild! (20)",mention_author=False)

        else:

            if current_timer_count >= 40:
                await ctx.message.add_reaction(self.bot.cross)
                return await ctx.reply("You have reached the max amount of timers in this guild! (40)",mention_author=False)


        ending = datetime.datetime.utcnow() + datetime.timedelta(seconds=time)

        minutes, seconds = divmod(time, 60)
        hours, minutes = divmod(minutes, 60)
        days, hours = divmod(hours, 24)
        weeks, days = divmod(days, 7)

        if int(weeks):
            time = f"**{weeks}** weeks, **{days}** days, **{hours}** hours, **{minutes}** minutes, **{seconds}** seconds"
        if int(days) and int(weeks) == 0:
            time = f"**{days}** days, **{hours}** hours, **{minutes}** minutes, **{seconds}** seconds"
        if int(hours) and int(days) == 0:
            time = f"**{hours}** hours, **{minutes}** minutes, **{seconds}** seconds"
        if int(minutes) and int(hours) == 0:
            time = f"**{minutes}** minutes, **{seconds}** seconds"
        if int(seconds) and int(minutes) == 0:
            time = f"**{seconds}** seconds"

        new_embed = discord.Embed(
            title=timer,
            description=time,
            color=random.choice(self.bot.color_list),
            timestamp=ending
        )
        new_embed.set_footer(text="Ends at ")

        msg = await ctx.send(embed=new_embed)
        await ctx.message.add_reaction(self.bot.check)
        await msg.add_reaction("⏲")




        timer_filter = {"guild": ctx.guild.id, "number": current_timer_count + 1, "channel" : ctx.channel.id, "user" : ctx.author.id,"id" : msg.id}

        timer_data = {"timer" : timer, "time" : time_int, "msg" : msg.id, "channel" : ctx.channel.id, "ending" : ending }

        await self.bot.timers.upsert_custom(timer_filter, timer_data)

        time_left = int(time_int)

        while time_left > 0:
            time_left -= 5
            await asyncio.sleep(5)


            timer_filter = {"id" : msg.id}
            timers = await self.bot.timers.find_many_by_custom(timer_filter)

            if bool(timers) is False:
                return

            minutes, seconds = divmod(time_left, 60)
            hours, minutes = divmod(minutes, 60)
            days, hours = divmod(hours, 24)
            weeks, days = divmod(days, 7)

            if int(weeks):
                new_time = f"**{weeks}** weeks, **{days}** days, **{hours}** hours, **{minutes}** minutes, **{seconds}** seconds"
            if int(days) and int(weeks) == 0:
                new_time = f"**{days}** days, **{hours}** hours, **{minutes}** minutes, **{seconds}** seconds"
            if int(hours) and int(days) == 0:
                new_time = f"**{hours}** hours, **{minutes}** minutes, **{seconds}** seconds"
            if int(minutes) and int(hours) == 0:
                new_time = f"**{minutes}** minutes, **{seconds}** seconds"
            if int(seconds) and int(minutes) == 0:
                new_time = f"**{seconds}** seconds"


            em = discord.Embed(
                title=timer,
                description=new_time,
                color=random.choice(self.bot.color_list),
                timestamp=ending
            )
            em.set_footer(text="Ends at ")
            await msg.edit(embed=em)



            if time_left <= 1:

                em = discord.Embed(
                    title=timer,
                    description="Timer Completed!",
                    timestamp=ending
                )
                em.set_footer(text="Ended at ")

                await msg.edit(embed=em)

                await self.bot.timers.delete_by_custom({"id" : msg.id})
                await msg.reply(
                    f"The timer for **{timer}** has ended!\nhttps://discord.com/channels/{ctx.guild.id}/{ctx.channel.id}/{msg.id}")
                return





    @_timer.group(name="end",description="End a selected timer early or the lastest one in the current channel",invoke_without_command=True,case_insensitive=True)
    @commands.cooldown(1, 2, commands.BucketType.default)
    async def _end(self, ctx, id : discord.Message=None):

        if id is None:
            timer_filter = {"channel" : ctx.channel.id}
            timers = await self.bot.timers.find_many_by_custom(timer_filter)

        else:
            timer_filter = {"id" : id.id}
            timers = await self.bot.timers.find_many_by_custom(timer_filter)


        if not timers:
            await ctx.message.add_reaction(self.bot.cross)
            return await ctx.reply(f"There are no on going timers in this guild!",mention_author=False)

        for timer in timers:

            msg = timer["msg"]
            channel = timer["channel"]
            name = timer["timer"]
            length = timer["time"]

        channelObj = self.bot.get_channel(channel)

        message = channelObj.get_partial_message(msg)
        await self.bot.timers.delete_by_custom({"id" : message.id})
        await ctx.message.delete()

        ending = datetime.datetime.utcnow() + datetime.timedelta(seconds=length)

        await message.reply(f"The timer for **{name}** has ended!\nhttps://discord.com/channels/{ctx.guild.id}/{channelObj.id}/{msg}")

        em = discord.Embed(
                title=name,
                description=f"Timer Completed!",
                timestamp=ending
        )
        em.set_footer(text="Would have ended at ")
        await message.edit(embed=em)

    @_end.command(name="channel",description="End all the timers in the selected channel")
    @commands.cooldown(1, 2, commands.BucketType.default)
    async def _channel(self, ctx, channel : discord.TextChannel=None):

        if channel is None:
            channel = ctx.channel

        current_timer_count = len(
            await self.bot.timers.find_many_by_custom(
                {
                    "channel": channel.id
                }
            )
        )

        if current_timer_count == 0:
            await ctx.message.add_reaction(self.bot.cross)
            return await ctx.reply(f"There are no on going timers in {channel.mention}",mention_author=False)

        em = discord.Embed(
            title="Are you sure?",
            description=f"Are you sure you want to end all **{current_timer_count}** timers in {channel.mention}?",
            color=self.bot.yellow
        )


        m = await ctx.send(embed=em)
        await m.add_reaction(self.bot.check)
        await m.add_reaction(self.bot.cross)

        try:
            reaction, member = await self.bot.wait_for(
                "reaction_add",
                timeout=60,
                check=lambda reaction, user: user == ctx.author
                and reaction.message.channel == ctx.channel
            )
        except asyncio.TimeoutError:
            await ctx.send("Confirmation Failure. Please try again.")
            return

        if str(reaction.emoji) not in [self.bot.check, self.bot.cross] or str(reaction.emoji) == self.bot.cross:
            await ctx.send("Canceling timer end task!")
            return

        await m.delete()


        timer_filter = {"channel" : channel.id}
        timers = await self.bot.timers.find_many_by_custom(timer_filter)

        c = await ctx.send(f"{self.bot.loading} Ending timers please wait {self.bot.loading}")
        await ctx.message.delete()


        for timer in timers:

            msg = timer["msg"]
            channel = timer["channel"]
            name = timer["timer"]
            length = timer["time"]

            channelObj = self.bot.get_channel(channel)

            message = channelObj.get_partial_message(msg)
            await self.bot.timers.delete_by_custom({"id": message.id})


            ending = datetime.datetime.utcnow() + datetime.timedelta(seconds=length)

            await message.reply(
                f"The timer for **{name}** has ended!\nhttps://discord.com/channels/{ctx.guild.id}/{channelObj.id}/{msg}")

            em = discord.Embed(
                title=name,
                description=f"Timer Completed!",
                timestamp=ending
            )
            em.set_footer(text="Would have ended at ")
            await message.edit(embed=em)

        await c.delete()
        em = discord.Embed(
            title="Ended all timers!",
            description=f"Successfully ended all **{current_timer_count}** timers in {channel.mention}",
            color=self.bot.green)
        await ctx.send(embed=em)

    @_end.command(name="all",description="End all the timers in the current guild")
    @commands.cooldown(1, 2, commands.BucketType.default)
    async def _all(self, ctx):

        current_timer_count = len(
            await self.bot.timers.find_many_by_custom(
                {
                    "guild": ctx.guild.id
                }
            )
        )

        if current_timer_count == 0:
            await ctx.message.add_reaction(self.bot.cross)
            return await ctx.reply(f"There are no on going timers in **{ctx.guild}**!",mention_author=False)

        em = discord.Embed(
            title="Are you sure?",
            description=f"Are you sure you want to end all **{current_timer_count}** timers in {ctx.guild}?",
            color=self.bot.yellow
        )


        m = await ctx.send(embed=em)
        await m.add_reaction(self.bot.check)
        await m.add_reaction(self.bot.cross)

        try:
            reaction, member = await self.bot.wait_for(
                "reaction_add",
                timeout=60,
                check=lambda reaction, user: user == ctx.author
                and reaction.message.channel == ctx.channel
            )
        except asyncio.TimeoutError:
            await ctx.send("Confirmation Failure. Please try again.")
            return

        if str(reaction.emoji) not in [self.bot.check, self.bot.cross] or str(reaction.emoji) == self.bot.cross:
            await ctx.send("Canceling timer end task!")
            return

        await m.delete()


        timer_filter = {"guild" : ctx.guild.id}
        timers = await self.bot.timers.find_many_by_custom(timer_filter)

        c = await ctx.send(f"{self.bot.loading} Ending timers please wait {self.bot.loading}")
        await ctx.message.delete()


        for timer in timers:

            msg = timer["msg"]
            channel = timer["channel"]
            name = timer["timer"]
            length = timer["time"]

            channelObj = self.bot.get_channel(channel)

            message = channelObj.get_partial_message(msg)
            await self.bot.timers.delete_by_custom({"id": message.id})


            ending = datetime.datetime.utcnow() + datetime.timedelta(seconds=length)

            await message.reply(
                f"The timer for **{name}** has ended!\nhttps://discord.com/channels/{ctx.guild.id}/{channelObj.id}/{msg}")

            em = discord.Embed(
                title=name,
                description=f"Timer Completed!",
                timestamp=ending
            )
            em.set_footer(text="Would have ended at ")
            await message.edit(embed=em)

        await c.delete()
        em = discord.Embed(
            title="Ended all timers!",
            description=f"Successfully ended all **{current_timer_count}** timers in **{ctx.guild}**",
            color=self.bot.green)
        await ctx.send(embed=em)

    @_end.command(name="user",description="End all the timers started by a user",aliases=["member"])
    @commands.cooldown(1, 2, commands.BucketType.default)
    async def _user(self, ctx, user : discord.Member = None):

        if user is None:
            user = ctx.author

        current_timer_count = len(
            await self.bot.timers.find_many_by_custom(
                {
                    "user": user.id
                }
            )
        )

        if current_timer_count == 0:
            await ctx.message.add_reaction(self.bot.cross)
            return await ctx.reply(f"There are no on going timers started by **{user}**",mention_author=False)

        em = discord.Embed(
            title="Are you sure?",
            description=f"Are you sure you want to end all **{current_timer_count}** timers started by **{user}**",
            color=self.bot.yellow
        )


        m = await ctx.send(embed=em)
        await m.add_reaction(self.bot.check)
        await m.add_reaction(self.bot.cross)

        try:
            reaction, member = await self.bot.wait_for(
                "reaction_add",
                timeout=60,
                check=lambda reaction, user: user == ctx.author
                and reaction.message.channel == ctx.channel
            )
        except asyncio.TimeoutError:
            await ctx.send("Confirmation Failure. Please try again.")
            return

        if str(reaction.emoji) not in [self.bot.check, self.bot.cross] or str(reaction.emoji) == self.bot.cross:
            await ctx.send("Canceling timer end task!")
            return

        await m.delete()


        timer_filter = {"user" : user.id}
        timers = await self.bot.timers.find_many_by_custom(timer_filter)

        c = await ctx.send(f"{self.bot.loading} Ending timers please wait {self.bot.loading}")
        await ctx.message.delete()


        for timer in timers:

            msg = timer["msg"]
            channel = timer["channel"]
            name = timer["timer"]
            length = timer["time"]

            channelObj = self.bot.get_channel(channel)

            message = channelObj.get_partial_message(msg)
            await self.bot.timers.delete_by_custom({"id": message.id})


            ending = datetime.datetime.utcnow() + datetime.timedelta(seconds=length)

            await message.reply(
                f"The timer for **{name}** has ended!\nhttps://discord.com/channels/{ctx.guild.id}/{channelObj.id}/{msg}")

            em = discord.Embed(
                title=name,
                description=f"Timer Completed!",
                timestamp=ending
            )
            em.set_footer(text="Would have ended at ")
            await message.edit(embed=em)

        await c.delete()
        em = discord.Embed(
            title="Ended all timers!",
            description=f"Successfully ended all **{current_timer_count}** timers started by **{user}**",
            color=self.bot.green)
        await ctx.send(embed=em)


    @_timer.command(name="list",description="List all the current running timers in the current guild")
    @commands.cooldown(1, 3, commands.BucketType.default)
    async def _list(self, ctx):


        current_timer_count = len(
            await self.bot.timers.find_many_by_custom(
                {
                    "guild": ctx.guild.id
                }
            )
        )
        if current_timer_count is 0:
            return await ctx.reply("There are no on-going timers in this guild!",mention_author=False)

        await ctx.reply(f"{self.bot.loading} Please wait as this might take a while {self.bot.loading}",mention_author=False)


        timer_filter = {"guild": ctx.guild.id}
        timers = await self.bot.timers.find_many_by_custom(timer_filter)

        pages = []
        for timer in timers:

            ending = timer["ending"]
            time_left = ending - datetime.datetime.utcnow()

            time_left = int(time_left.total_seconds())


            minutes, seconds = divmod(time_left, 60)
            hours, minutes = divmod(minutes, 60)
            days, hours = divmod(hours, 24)

            if int(days):
                time = f"**{days}** days, **{hours}** hours, **{minutes}** minutes, **{seconds}** seconds"
            if int(hours) and int(days) == 0:
                time = f"**{hours}** hours, **{minutes}** minutes, **{seconds}** seconds"
            if int(minutes) and int(hours) == 0:
                time = f"**{minutes}** minutes, **{seconds}** seconds"
            if int(seconds) and int(minutes) == 0:
                time = f"**{seconds}** seconds"

            guild = timer["guild"]
            channel = timer["channel"]
            message = timer["id"]

            link = f"https://discord.com/channels/{guild}/{channel}/{message}"


            description = f"""
            Time Id: `{timer["id"]}`
            Timer Number: `{timer['number']}`
            Time Left: {time}
            Time Link: [Click Here]({link})
            """
            pages.append(description)


        await Pag(
            title=f"Timers for `{ctx.guild}` ",
            colour=self.bot.aqua,
            entries=pages,
            length=3,

        ).start(ctx)
        




























def setup(bot):
    bot.add_cog(Timer(bot))