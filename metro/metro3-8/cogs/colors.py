import discord
from discord.ext import commands

class Colors(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_ready(self):
		print(f"{self.__class__.__name__} Cog has been loaded\n-----")


	@commands.group(invoke_without_command=True,aliases=['color'],case_insensitive=True)
	async def colors(self, ctx):

		data = await self.bot.config.get_by_id(ctx.message.guild.id)
		prefix = data["prefix"]	

		e = discord.Embed(title='Colors',description=f'Nothing more. Nothing less. \n \n **How to look at colors:** \n {prefix}color <color> \n\n **Colors we have:** Red, Orange, Yellow, Green, Aqua, Blue, Navy, Purple, Brown, Black, White',color= 0x808080)
		await ctx.send(embed=e)



























def setup(bot):
	bot.add_cog(Colors(bot))

