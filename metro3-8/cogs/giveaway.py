import discord
from discord.ext import commands
import re
import asyncio
import datetime
import random
from utils.giveaway import draw_winner


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



class Giveaway(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    def gaw_check(ctx):
        if ctx.author.guild_permissions.manage_guild is True:
            return True
        try:
            role = discord.utils.get(ctx.guild.roles, name="Giveaways")

            if role in ctx.author.roles:
                return True
            else:
                return False
        except:
            return False


    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.__class__.__name__} Cog has been loaded\n-----")

    @commands.command(aliases=["gend","greroll","glist","gsettings"],hidden=True)
    async def gstart(self, ctx):

        e = discord.Embed(
            title="Commands have changed!",
            description=f"All giveaway commands have been made into one big sub-command! \n\n Run ``{ctx.prefix}giveaway`` for more details!",
            color=self.bot.red,
            timestamp=ctx.message.created_at
        )
        await ctx.reply(embed=e, mention_author=False)


    @commands.group(name="giveaway",aliases=["g"],description="Create/Manage giveaways easily in your server!",invoke_without_command=True,case_insensitive=True)
    async def giveaway(self, ctx):



        embed = discord.Embed(
            title="Giveaways in Metro",
            description=f"```yaml\nCommand: {ctx.prefix}{ctx.command} \nAliases: {ctx.prefix}g``` \n**{ctx.command.description}** \n\n **Sub-commands for giveaways:** \n``start`` - instantly start a giveaway",
            color=self.bot.aqua,
            timestamp=ctx.message.created_at
        )
        embed.set_footer(text="This command is currently under development and report bugs to support!")
        await ctx.reply(embed=embed, mention_author=False)


    @giveaway.command()
    @commands.check(gaw_check)
    async def start(self, ctx, time : TimeConverter, winners, *, prize):

        time_int = time

        if ctx.channel.is_news():
            await ctx.message.add_reaction(self.bot.cross)
            return await ctx.reply("You cannot make giveaways in annoucement channels!", mention_author=False)

        if time < 3:
            await ctx.message.add_reaction(self.bot.cross)
            return await ctx.reply("Giveaways must be longer than 3 seconds!",mention_author=False)
        if time > 604800:
            await ctx.message.add_reaction(self.bot.cross)
            return await ctx.reply("Giveaways cannot be longer than 7 days!",mention_author=False)

        if winners.endswith("w"):
            winners = winners[:-1]
            winners = int(winners)

        else:
            try:
                winners = int(winners)
            except:
                await ctx.message.add_reaction(self.bot.cross)
                return await ctx.reply(f"I couldn't convert `{winners}` into an int!",mention_author=False)

        winners_int = winners

        if winners < 0:
            await ctx.message.add_reaction(self.bot.cross)
            return await ctx.reply("You cannot have less than 0 winners!",mention_author=False)

        if winners > 5:
            await ctx.message.add_reaction(self.bot.cross)
            return await ctx.reply("You cannot have more than 5 winners! (since it's in beta)",mention_author=False)

        current_gaw_count = len(
            await self.bot.giveaway.find_many_by_custom(
                {
                    "guild": ctx.guild.id
                }
            )
        )
        

            

        await ctx.message.delete()
        ending = datetime.datetime.utcnow() + datetime.timedelta(seconds=time_int)

        minutes, seconds = divmod(time_int, 60)
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

        embed = discord.Embed(
                title=prize,
                description=f"React with :tada: to enter! \nTime Left: {time} \nHosted by: {ctx.author.mention}",
                color=self.bot.aqua,
                timestamp=ending
            )
        embed.set_footer(text=f"Winners: {winners} | Ends at ")

        gaw_msg = await ctx.send(":tada: **GIVEAWAY** :tada:",embed=embed)
        await gaw_msg.add_reaction("🎉")

        gaw_filter = {"guild": ctx.guild.id, "number": current_gaw_count + 1, "channel": ctx.channel.id,
                        "user": ctx.author.id, "id": gaw_msg.id}

        gaw_data = {"prize": prize, "time": time_int, "msg": gaw_msg.id, "channel": ctx.channel.id, "ending": ending, "winners" : winners, "id" : gaw_msg.id}

        await self.bot.giveaway.upsert_custom(gaw_filter, gaw_data)


        time_left = time_int

        while time_left > 0:
            time_left -= 5
            await asyncio.sleep(5)

            minutes, seconds = divmod(time_left, 60)
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
                            title=prize,
                            description=f"React with :tada: to enter! \nTime Left: {time}\nHosted by: {ctx.author.mention}",
                            color = self.bot.aqua,
                            timestamp = ending)
            new_embed.set_footer(text=f"Winners: {winners} | Ends at ")

            await gaw_msg.edit(embed=new_embed)


            if time_left <= 0:
                message = await ctx.channel.fetch_message(gaw_msg.id)


                users = await message.reactions[0].users().flatten()
                users.pop(users.index(ctx.guild.me))

                if len(users) == 0:
                    em = discord.Embed(title=prize,
                                       description=f"Winner: No vaild entries!\nHosted by: {ctx.author.mention}",
                                       timestamp=ending)
                    em.set_footer(text="Winners: 0 | Ended at ")
                    await gaw_msg.edit(embed=em)
                    return await gaw_msg.reply(f"There were no vaild entries for the **{prize}** giveaway")


                users = await message.reactions[0].users().flatten()
                users.pop(users.index(ctx.guild.me))


                winners = await draw_winner(users, winners)


                em = discord.Embed(
                    title=prize,
                    description="Winner: {}\nHosted by: {}".format(", ".join(winners), ctx.author.mention),
                    color=self.bot.black,
                    timestamp=ending
                )
                em.set_footer(text=f"Winners: {winners_int} | Ended at ")

                await gaw_msg.edit(content=":tada: **GIVEAWAY ENDED** :tada:",embed=em)



                await gaw_msg.reply(":tada: Congrats {}, you won **{}** :tada:".format(", ".join(winners), prize))


                for winner in winners:
                    return





















































def setup(bot):
    bot.add_cog(Giveaway(bot))