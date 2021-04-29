import discord
from discord.ext import commands
import datetime
import asyncio
import re

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


class Remind(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.__class__.__name__} Cog has been loaded\n-----")


    @commands.command(name="reminder",aliases=["rm", "remindme","remind"])
    async def _remind(self, ctx, time : TimeConverter, *, something="something"):

        time_int = time

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


        em = discord.Embed(
            title="New Reminder!",
            description=f"I'll remind you about `{something}` in\n{time}",
            color=self.bot.yellow
        )
        await ctx.reply(embed=em,mention_author=False)
        await asyncio.sleep(time_int)

        em = discord.Embed(
            title="Reminder",
            description=f"You asked to be reminded of `{something}` \n{time} ago",
            color=self.bot.green
        )
        await ctx.author.send(embed=em)



























































































def setup(bot):
    bot.add_cog(Remind(bot))