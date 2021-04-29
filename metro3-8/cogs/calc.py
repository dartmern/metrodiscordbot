import discord
from discord.ext import commands
import time
from TagScriptEngine import Interpreter, adapter, block

class Calc(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        blocks = [
            block.MathBlock(),
            block.RandomBlock(),
            block.RangeBlock(),
        ]
        self.engine = Interpreter(blocks)

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.__class__.__name__} Cog has been loaded\n-----")

    async def red_delete_data_for_user(self, **kwargs):
        return

    @commands.command(aliases=["calc"])
    async def calculate(self, ctx, *, query):
        """Math"""

        query = query.replace(",", "")
        engine_input = "{m:" + query + "}"
        start = time.monotonic()
        output = self.engine.process(engine_input)
        end = time.monotonic()

        output_string = output.body.replace("{m:", "").replace("}", "")
        e = discord.Embed(
            color=self.bot.green,
            title=f"Input: `{query}`",
            description=f"Output: `{output_string}`",
        )
        e.set_footer(text=f"Calculated in {round((end - start) * 1000, 3)} ms")
        await ctx.reply(embed=e,mention_author=False)




def setup(bot):
	bot.add_cog(Calc(bot))
