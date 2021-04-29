import discord
from discord.ext import commands
import random
from typing import Optional

class Choose(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.__class__.__name__} Cog has been loaded\n-----")


    @commands.command(name="roll")
    async def _roll(self, ctx, option1 : int=None, option2: int=None):

        if option2 is None and option1 is None:
            return await ctx.reply(f"Please use the following format: `{ctx.prefix}roll [option]`",mention_author=False)

        if option2 is None:
            nu = random.randint(1, option1)
            return await ctx.reply(f"**{ctx.author.name}** rolls **{nu}** (1-{option1})",mention_author=False)

        if int(option1) and int(option2):
            nu = random.randint(option1, option2)
            return await ctx.reply(f"**{ctx.author.name}** rolls **{nu}** ({option1}-{option2})",mention_author=False)

        else:

            nu = random.randint(1, 100)
            return ctx.reply(f"**{ctx.author.name}** rolls **{nu}** (1-100)", mention_author=False)


def setup(bot):
    bot.add_cog(Choose(bot))



