import discord
from discord.ext import commands

from utils.util import Pag


class EnableDisable(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.__class__.__name__} Cog has been loaded\n-----")


    @commands.command()
    @commands.is_owner()
    async def toggle(self, ctx, * , command):
        command = self.bot.get_command(command)

        if command is None:
            await ctx.send("I can't find a command with that name!")

        elif ctx.command == command:
            await ctx.send("You cannot disable this command.")

        else:
            command.enabled = not command.enabled
            ternary = "enabled" if command.enabled else "disabled"
            await ctx.send(f"I have **{ternary}** ``{command.qualified_name}`` for you!")


def setup(bot):
    bot.add_cog(EnableDisable(bot))