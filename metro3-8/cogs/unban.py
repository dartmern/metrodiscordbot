import discord
from discord.ext import commands


class Unban(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.__class__.__name__} Cog has been loaded\n-----")



    @commands.command()
    @commands.has_guild_permissions(ban_members=True)
    async def unban(self, ctx, member : int, *, reason=None):

        try:
            member = await self.bot.fetch_user(int(member))
            await ctx.guild.unban(member, reason=reason)

            em = discord.Embed(
                title="Success!",
                description=f"You successfully unbanned **{member}**! \n\n**Responsible Moderator:** {ctx.author.mention}\n**Reason:** {reason}",
                color=self.bot.green,
                timestamp=ctx.message.created_at
            )
            msg = discord.Embed(
                title="Unbanned!",
                description=f"You were unbanned from **{ctx.guild}**! ``{ctx.guild.id}`` \n\n**Responsible Moderator:** {ctx.author.mention}\n**Reason:** {reason}",
                color=self.bot.green,
                timestamp=ctx.message.created_at
            )
            try:
                await member.send(embed=msg)
                await ctx.message.add_reaction(self.bot.check)
                await ctx.reply(embed=em, mention_author=False)
            except:
                await ctx.message.add_reaction(self.bot.check)
                await ctx.reply(embed=em, mention_author=False)

            info = await self.bot.logs.find(ctx.message.guild.id)

            log = info["ban"]
            if not log is None:
                logs = self.bot.get_channel(log)
                embed = discord.Embed(
                    title="unban",
                    description=f"**Offender:** {member} - {member.mention} -``{member.id}`` \n**Reason:** {reason}\n**Responsible Moderator:** {ctx.author} - {ctx.author.mention} -``{ctx.author.id}``",
                    color=self.bot.aqua,
                    timestamp=ctx.message.created_at)
                await logs.send(embed=embed)

        except:
            await ctx.message.add_reaction(self.bot.cross)
            return await ctx.reply("Invaild user! Please input a user id!",mention_author=False)

















def setup(bot):
    bot.add_cog(Unban(bot))