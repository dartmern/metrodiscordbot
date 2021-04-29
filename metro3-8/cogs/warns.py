import discord
from discord.ext import commands

from utils.util import Pag


class Tempban(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.__class__.__name__} Cog has been loaded\n-----")

    @commands.command(name="warn")
    @commands.has_guild_permissions(manage_messages=True)
    async def _warn(self, ctx, member : discord.Member, *  ,reason):

        if member.id in [ctx.author.id, self.bot.user.id]:
            await ctx.message.add_reaction(self.bot.cross)
            return await ctx.reply("You cannot warn yourself or the bot!",mention_author=False)

        guild = ctx.guild
        current_warn_count = len(
            await self.bot.warns.find_many_by_custom(
                {
                    "user_id": member.id,
                    "guild_id": member.guild.id
                }
            )
        ) + 1


        warn_filter = {"user_id": member.id, "guild_id": member.guild.id, "number": current_warn_count}
        warn_data = {"reason": reason, "timestamp": ctx.message.created_at, "warned_by": ctx.author.id}

        await self.bot.warns.upsert_custom(warn_filter, warn_data)

        embed = discord.Embed(
            title="Warned!",
            description=f"You were muted in {guild}! ``{guild.id}``\n\n**Responsible Moderator:** {ctx.author.mention}\n**Reason:** {reason}",
            color=self.bot.orange,
            timestamp=ctx.message.created_at)

        em = discord.Embed(
            title="Success!",
            description=f"You successfully warned {member.mention}\n\n**Responsible Moderator:** {ctx.author.mention}\n**Reason:** {reason}",
            color=self.bot.green,
            timestamp=ctx.message.created_at
        )

        try:
            await member.send(embed=embed)
            await ctx.message.add_reaction(self.bot.check)
            await ctx.reply(embed=em)

        except:
            em.set_footer(text="Note that I couldn't DM them because they were closed")
            await ctx.message.add_reaction(self.bot.check)
            await ctx.reply(embed=em)

    @commands.command()
    @commands.guild_only()
    async def warns(self, ctx, member: discord.Member):
        warn_filter = {"user_id": member.id, "guild_id": member.guild.id}
        warns = await self.bot.warns.find_many_by_custom(warn_filter)

        if not bool(warns):
            return await ctx.send(f"Couldn't find any warns for: `{member.display_name}`")

        warns = sorted(warns, key=lambda x: x["number"])
        totalwarns = warns


        pages = []
        for warn in warns:
            description = f"""
            Warn Number: `{warn['number']}`
            Warn Reason: `{warn['reason']}`
            Warned By: <@{warn['warned_by']}>
            """
            pages.append(description)

        await Pag(
            title=f"Warns for `{member.display_name}` ",
            colour=0xCE2029,
            entries=pages,
            length=4
        ).start(ctx)








def setup(bot):
    bot.add_cog(Tempban(bot))