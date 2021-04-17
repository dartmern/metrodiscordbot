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



class Giveaway(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


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
            description=f"```yaml\nCommand: {ctx.prefix}{ctx.command} \nAliases: {ctx.prefix}g``` \n**{ctx.command.description}** \n\n **Sub-commands for giveaways:** \n``start`` - instantly start a giveaway\n``reroll`` - reroll a giveaway that has ended \n``end`` - end a giveaway early \n``cancel`` - cancel a giveaway",
            color=self.bot.aqua,
            timestamp=ctx.message.created_at
        )
        embed.set_footer(text="This command is currently under development and report bugs to support!")
        await ctx.reply(embed=embed, mention_author=False)


    @giveaway.command()
    async def start(self, ctx, time : TimeConverter, winners, *, prize):



        if time < 3:
            await ctx.message.add_reaction(self.bot.cross)
            return await ctx.reply("Giveaways must be longer than 3 seconds!")
        if time > 3600:
            await ctx.message.add_reaction(self.bot.cross)
            return await ctx.reply("Giveaways cannot be longer than 1 hour! (since it's in beta)")

        if winners.endswith("w"):
            winners = winners[:-1]
            winners = int(winners)

            if winners < 0:
                return await ctx.reply("You cannot have less than 0 winners!")

            if winners > 5:
                return await ctx.reply("You cannot have more than 5 winners! (since it's in beta)")



        endTime = datetime.datetime.now() + datetime.timedelta(seconds=time)

        data = {"_id" : ctx.message.id, "end" : endTime, "start" : datetime.datetime.now(), "winners" : winners, "prize" : prize, "time" : time }
        await self.bot.giveaways.upsert(data)

        try:
            ending = datetime.datetime.utcnow() + datetime.timedelta(seconds=time)

            minutes, seconds = divmod(time, 60)
            hours, minutes = divmod(minutes, 60)

            if int(hours):

                embed = discord.Embed(
                    title=prize,
                    description=f"React with :tada: to enter! \nTime left: **{hours}** hours, **{minutes}** minutes, **{seconds}** seconds \nHosted by: {ctx.author.mention}",
                    color=self.bot.aqua,
                    timestamp=ending
                )
                embed.set_footer(text=f"Winners: {winners} | Ends at ")

                gaw_msg = await ctx.send(":tada: **GIVEAWAY** :tada:",embed=embed)
                await gaw_msg.add_reaction("🎉")

                time_left = time

                while time_left > 0:
                    time_left -= 5
                    await asyncio.sleep(5)

                    minutes, seconds = divmod(time_left, 60)
                    hours, minutes = divmod(minutes, 60)

                    if int(hours):

                        new_embed = discord.Embed(
                            title=prize,
                            description=f"React with :tada: to enter! \nTime left: **{hours}** hours, **{minutes}** minutes, **{seconds}** seconds\nHosted by: {ctx.author.mention}",
                            color = self.bot.aqua,
                            timestamp = ending
                        )
                        new_embed.set_footer(text=f"Winners: {winners} | Ends at ")

                        await gaw_msg.edit(embed=new_embed)

                    if int(minutes) and hours == 0:

                        new_embed = discord.Embed(
                            title=prize,
                            description=f"React with :tada: to enter! \nTime left: **{minutes}** minutes, **{seconds}** seconds\nHosted by: {ctx.author.mention}",
                            color=self.bot.aqua,
                            timestamp=ending
                        )
                        new_embed.set_footer(text=f"Winners: {winners} | Ends at ")

                        await gaw_msg.edit(embed=new_embed)

                    if int(seconds) and minutes == 0:

                        new_embed = discord.Embed(
                            title=prize,
                            description=f"React with :tada: to enter! \nTime left: **{seconds}** seconds\nHosted by: {ctx.author.mention}",
                            color=self.bot.aqua,
                            timestamp=ending
                        )
                        new_embed.set_footer(text=f"Winners: {winners} | Ends at ")

                        await gaw_msg.edit(embed=new_embed)

                    if time_left <= 0:
                        break


            if int(minutes) and hours == 0:

                embed = discord.Embed(
                    title=prize,
                    description=f"React with :tada: to enter! \nTime left: **{minutes}** minutes, **{seconds}** seconds \nHosted by: {ctx.author.mention}",
                    color=self.bot.aqua,
                    timestamp=ending
                )
                embed.set_footer(text=f"Winners: {winners} | Ends at ")

                gaw_msg = await ctx.send(":tada: **GIVEAWAY** :tada:", embed=embed)
                await gaw_msg.add_reaction("🎉")

                time_left = time

                while time_left > 0:
                    time_left -= 5
                    await asyncio.sleep(5)

                    minutes, seconds = divmod(time_left, 60)
                    hours, minutes = divmod(minutes, 60)


                    if int(minutes):
                        new_embed = discord.Embed(
                            title=prize,
                            description=f"React with :tada: to enter! \nTime left: **{minutes}** minutes, **{seconds}** seconds\nHosted by: {ctx.author.mention}",
                            color=self.bot.aqua,
                            timestamp=ending
                        )
                        new_embed.set_footer(text=f"Winners: {winners} | Ends at ")

                        await gaw_msg.edit(embed=new_embed)

                    if int(seconds) and minutes == 0:
                        new_embed = discord.Embed(
                            title=prize,
                            description=f"React with :tada: to enter! \nTime left: **{seconds}** seconds\nHosted by: {ctx.author.mention}",
                            color=self.bot.aqua,
                            timestamp=ending
                        )
                        new_embed.set_footer(text=f"Winners: {winners} | Ends at ")

                        await gaw_msg.edit(embed=new_embed)

                    if time_left <= 0:
                        break



            if int(seconds):
                embed = discord.Embed(
                    title=prize,
                    description=f"React with :tada: to enter! \nTime left: **{seconds}** seconds \nHosted by: {ctx.author.mention}",
                    color=self.bot.aqua,
                    timestamp=ending
                )
                embed.set_footer(text=f"Winners: {winners} | Ends at ")

                gaw_msg = await ctx.send(":tada: **GIVEAWAY** :tada:", embed=embed)
                await gaw_msg.add_reaction("🎉")

                time_left = time

                while time_left > 0:
                    time_left -= 5
                    await asyncio.sleep(5)

                    minutes, seconds = divmod(time_left, 60)
                    hours, minutes = divmod(minutes, 60)


                    if int(seconds):
                        new_embed = discord.Embed(
                            title=prize,
                            description=f"React with :tada: to enter! \nTime left: **{seconds}** seconds\nHosted by: {ctx.author.mention}",
                            color=self.bot.aqua,
                            timestamp=ending
                        )
                        new_embed.set_footer(text=f"Winners: {winners} | Ends at ")

                        await gaw_msg.edit(embed=new_embed)

                    if time_left <= 0:
                        break







        except Exception as error:
            await ctx.reply(f"An error occurred! It has been forwarded to the owner!\n\n Join our support server for details ``{ctx.prefix}support``")
            owner = self.bot.get_user(525843819850104842)
            await owner.send(f"An error occured in **{ctx.guild}**-``{ctx.guild.id}`` with the ``{ctx.prefix}g start`` command!")


















































def setup(bot):
    bot.add_cog(Giveaway(bot))