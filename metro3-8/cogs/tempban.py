import discord
from discord.ext import commands
import re
import asyncio
import datetime

time_regex = re.compile("(?:(\d{1,5})(h|s|m|d))+?")
time_dict = {"h": 3600, "s": 1, "m": 60, "d": 86400}



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



class Tempban(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.__class__.__name__} Cog has been loaded\n-----")


    @commands.command(name="tempban")
    @commands.has_guild_permissions(ban_members=True)
    async def _tempban(self, ctx, member : discord.Member, time : TimeConverter=None, delete_days=None, *, reason=None):
        """Temporarily ban a member from the guild!"""

        if member is ctx.author:
            await ctx.message.add_reaction(self.bot.cross)
            return await ctx.reply("You cannot tempban yourself!", mention_author=False)

        if member is ctx.guild.owner:
            await ctx.message.add_reaction(self.bot.cross)
            return await ctx.reply("You cannot tempban the owner of this server!", mention_author=False)
        
        if member is self.bot:
            await ctx.message.add_reaction(self.bot.cross)
            return await ctx.reply("I cannot ban myself!",mention_author=False)

        if not ctx.author is ctx.guild.owner:
            if ctx.author.top_role < member.top_role:
                await ctx.message.add_reaction(self.bot.cross)
                em = discord.Embed(
                    title="An error occured!",
                    description=f"Your highest role ({ctx.author.top_role.mention} - position {ctx.author.top_role.position}) is not higher than \n**{member}**'s highest role ({member.top_role.mention} - position {member.top_role.position}) therefore you cannot ban them!",
                    color=self.bot.red,
                    timestamp=ctx.message.created_at
                )
                return await ctx.reply(embed=em,mention_author=False)

        if time is None:
            await ctx.message.add_reaction(self.bot.cross)
            return await ctx.reply(f"Please specify a time! \n\nIf you want to ban without a time run: ``{ctx.prefix}ban <member> [reason=None]``",mention_author=False)

        if time < 30:
            await ctx.message.add_reaction(self.bot.cross)
            return await ctx.reply(f"You can't tempban someone for less than 30 seconds!",mention_author=False)

        try:
            delete_days = int(delete_days)
            if int(delete_days) > 7:
                await ctx.message.add_reaction(self.bot.cross)
                return await ctx.reply(f"You can only delete a user's messages of 7 days or less!",mention_author=False)

        except:
            delete_days = 0

        end = datetime.datetime.utcnow() + datetime.timedelta(seconds=time)
        iTime = time

        minutes, seconds = divmod(time, 60)
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
            title="Success!",
            description=f"You successfully tempbanned {member.mention}! \n\n**Responsible Moderator:** {ctx.author.mention}\n**Time:** {time}\n**Reason:** {reason}\n**Deleted Message Days:** {delete_days}",
            color=self.bot.green,
            timestamp=ctx.message.created_at
        )

        msg = discord.Embed(
            title="Tempbanned!",
            description=f"You were tempbanned from **{ctx.guild}**! ``{ctx.guild.id}`` \n\n**Responsible Moderator:** {ctx.author.mention}\n**Time:** {time}\n**Reason:** {reason}\n**Deleted Message Days:** {delete_days}",
            color=self.bot.red,
            timestamp=ctx.message.created_at
        )

        try:
            await member.send(embed=msg)
            await ctx.message.add_reaction(self.bot.check)
            await ctx.reply(embed=em, mention_author=False)

        except:
            em.set_footer(text="Note that I couldn't DM them because they were closed")
            await ctx.reply(embed=em, mention_author=False)

        await member.ban(reason=reason, delete_message_days=delete_days)

        info = await self.bot.logs.find(ctx.message.guild.id)

        log = info["ban"]
        if not log is None:
            logs = self.bot.get_channel(log)
            embed = discord.Embed(
                title="tempban",
                description=f"**Offender:** {member} - {member.mention} -``{member.id}`` \n**Time:** {time} \n**Reason:** {reason}\n**Responsible Moderator:** {ctx.author} - {ctx.author.mention} -``{ctx.author.id}``",
                color=self.bot.red,
                timestamp=ctx.message.created_at)
            await logs.send(embed=embed)



        data = {"_id" : f"{member.id}-{ctx.guild.id}", "time" : time, "end" : end, "start" : datetime.datetime.utcnow() }
        await self.bot.tempban.upsert(data)

        await asyncio.sleep(iTime)
        await ctx.guild.unban(member)






























def setup(bot):
    bot.add_cog(Tempban(bot))