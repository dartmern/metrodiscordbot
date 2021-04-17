import discord
from discord.ext import commands


class Ban(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.__class__.__name__} Cog has been loaded\n-----")

    @commands.command()
    @commands.has_guild_permissions(ban_members=True)
    async def ban(self, ctx, member : discord.Member, delete_days=None, * , reason=None):
        """Permanently ban a member from the server!"""

        if member is ctx.author:
            await ctx.message.add_reaction(self.bot.cross)
            return await ctx.reply("You cannot tempban yourself!", mention_author=False)

        if member is ctx.guild.owner:
            await ctx.message.add_reaction(self.bot.cross)
            return await ctx.reply("You cannot tempban the owner of this server!", mention_author=False)

        if member.id is 788543184082698252:
            await ctx.message.add_reaction(self.bot.cross)
            return await ctx.reply("I cannot ban myself!", mention_author=False)

        if not ctx.author is ctx.guild.owner:
            if ctx.author.top_role < member.top_role:
                await ctx.message.add_reaction(self.bot.cross)
                em = discord.Embed(
                    title="An error occured!",
                    description=f"Your highest role ({ctx.author.top_role.mention} - position {ctx.author.top_role.position}) is not higher than \n**{member}**'s highest role ({member.top_role.mention} - position {member.top_role.position}) therefore you cannot ban them!",
                    color=self.bot.red,
                    timestamp=ctx.message.created_at
                )
                return await ctx.reply(embed=em, mention_author=False)


        try:
            int(delete_days)
            if int(delete_days) > 7:
                await ctx.message.add_reaction(self.bot.cross)
                return await ctx.reply(f"You can only delete a user's messages of 7 days or less!",
                                       mention_author=False)
        except:
            delete_days = 0



        info = await self.bot.logs.find(ctx.message.guild.id)

        log = info["ban"]
        if not log is None:
            logs = self.bot.get_channel(log)
            embed = discord.Embed(
                title="ban",
                description=f"**Offender:** {member} - {member.mention} -``{member.id}`` \n**Reason:** {reason}\n**Responsible Moderator:** {ctx.author} - {ctx.author.mention} -``{ctx.author.id}``",
                color=self.bot.red,
                timestamp=ctx.message.created_at)
            await logs.send(embed=embed)


        em = discord.Embed(
            title="Success!",
            description=f"You successfully banned {member.mention}! \n\n**Responsible Moderator:** {ctx.author.mention}\n**Reason:** {reason}\n**Deleted Message Days:** {delete_days}",
            color=self.bot.green,
            timestamp=ctx.message.created_at
        )

        msg = discord.Embed(
            title="Banned!",
            description=f"You were banned from **{ctx.guild}**! ``{ctx.guild.id}`` \n\n**Responsible Moderator:** {ctx.author.mention}\n**Reason:** {reason}\n**Deleted Message Days:** {delete_days}",
            color=self.bot.red,
            timestamp=ctx.message.created_at
        )
        try:
            await member.send(embed=msg)
            await ctx.message.add_reaction(self.bot.check)
            await ctx.reply(embed=em, mention_author=False)
        except:
            await ctx.message.add_reaction(self.bot.check)
            em.set_footer(text="Note that I couldn't DM them because they were closed")
            await ctx.reply(embed=em, mention_author=False)

        await member.ban(reason=reason, delete_message_days=delete_days)

def setup(bot):
    bot.add_cog(Ban(bot))