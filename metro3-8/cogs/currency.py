import discord
from discord.ext import commands
import random
from typing import Optional


class Currency(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.__class__.__name__} Cog has been loaded\n-----")

    @commands.command(aliases=["bal"])
    async def balance(self, ctx, member: discord.Member = None):

        if member is None:
            member = ctx.author

        try:
            await self.bot.profile.find(member.id)
        except:
            await ctx.message.add_reaction(self.bot.cross)
            return await ctx.reply(
                f"It seems like **{member}** doesn't have an account! Run `{ctx.prefix}register` to start one!",
                mention_author=False)

        data = await self.bot.profile.find(member.id)
        wallet = data["wallet"]
        bank = data["bank"]
        maxBank = data["maxBank"]
        percent = bank / maxBank

        em = discord.Embed(
            title=f"{member.name}'s balance",
            description=f"**Wallet:** `☢` {wallet} \n**Bank:** `☢` {bank} / {maxBank} `({percent}%)`",
            color=self.bot.black,
            timestamp=ctx.message.created_at

        )
        em.set_footer(text="😏")
        await ctx.reply(embed=em,mention_author=False)

    @commands.command()
    async def register(self, ctx):

        try:
            await self.bot.profile.find(ctx.author)
            await ctx.message.add_reaction(self.bot.cross)
            return ctx.reply(f"You already have an account!", mention_author=False)

        except:

            data = {"_id": ctx.author.id, "wallet": 0, "bank": 0, "maxBank": 1000}
            await self.bot.profile.upsert(data)

            await ctx.reply("I created an account for you!", mention_author=False)


    @commands.command(name="withdraw")
    async def _withdraw(self, ctx, amount : str):

        try:
            await self.bot.profile.find(ctx.author.id)
        except:
            await ctx.message.add_reaction(self.bot.cross)
            return await ctx.reply(
                f"It seems like **{ctx.author}** doesn't have an account! Run `{ctx.prefix}register` to start one!",
                mention_author=False)

        try:
            amount = int(amount)
        except:
            if str == "all":

                data = await self.bot.profile.find(ctx.author.id)
                amount = data["bank"]

                if amount is 0:
                    await ctx.message.add_reaction(self.bot.cross)
                    return await ctx.reply(f"You cannot withdraw anything because your bank is empty!",mention_author=False)

            if str == "max":

                data = await self.bot.profile.find(ctx.author.id)
                amount = data["bank"]

                if amount is 0:
                    await ctx.message.add_reaction(self.bot.cross)
                    return await ctx.reply(f"You cannot withdraw anything because your bank is empty!",
                                           mention_author=False)


            else:
                await ctx.message.add_reaction(self.bot.cross)
                return await ctx.reply(f"That is not a vaild amount! Please input an int or the string `all`, `max`",mention_author=False)

        data = await self.bot.profile.find(ctx.author.id)
        bank = data["bank"]
        wallet = data["wallet"]

        if amount > bank:
            await ctx.message.add_reaction(self.bot.cross)
            return await ctx.reply(f"You cannot withdraw `{amount}` coins, because your bank only has `{bank}` coins", mention_author=False)

        newBank = bank - amount
        newWallet = wallet + amount

        data = {"_id" : ctx.author.id, "bank" : newBank, "wallet" : newWallet}
        await self.bot.profile.update(data)

        return await ctx.reply(f"You have successfully withdrawn {amount} {self.bot.coin} from your bank account!",mention_author=False)


    @commands.command()
    @commands.is_owner()
    async def setmoney(self, ctx, amount : int):

        data = {"_id":ctx.author.id, "bank" : amount }
        await self.bot.profile.update(data)
        await ctx.reply(f"Made your bank account `{amount}`",mention_author=False)



def setup(bot):
    bot.add_cog(Currency(bot))
