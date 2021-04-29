import discord
from discord.ext import commands
import asyncio
import re
from tabulate import tabulate
from fuzzywuzzy import process
from unidecode import unidecode
from utils.util import box, pagify, Context

from typing import Optional

from discord.ext.commands import RoleConverter, BadArgument

time_regex = re.compile("(?:(\d{1,5})(h|s|m|d))+?")
time_dict = {"h": 3600, "s": 1, "m": 60, "d": 86400}


def guild_roughly_chunked(guild: discord.Guild) -> bool:
    return len(guild.members) / guild.member_count > 0.9


class GoodRoles(commands.Converter):
    async def convert(self, ctx, argument):
        try:
            return await commands.RoleConverter().convert(ctx, argument)
        except commands.BadArgument:
            role_to_return = discord.utils.find(lambda x: x.name.lower() == argument.lower(), ctx.guild.roles)
            if role_to_return is not None:
                return role_to_return
            # This might be a bad idea, don't care
            name, ratio = process.extractOne(argument, [x.name for x in ctx.guild.roles])
            if ratio >= 75:
                role_to_return = discord.utils.get(ctx.guild.roles, name=name)
                return role_to_return

class BetterRoles(RoleConverter):
    """
    This will accept role ID's, mentions, and perform a fuzzy search for
    roles within the guild and return a list of role objects
    matching partial names
    Guidance code on how to do this from:
    https://github.com/Rapptz/discord.py/blob/rewrite/discord/ext/commands/converter.py#L85
    https://github.com/Cog-Creators/Red-DiscordBot/blob/V3/develop/redbot/cogs/mod/mod.py#L24
    """

    def __init__(self, response: bool = True):
        self.response = response
        super().__init__()

    async def convert(self, ctx: commands.Context, argument: str) -> discord.Role:
        try:
            basic_role = await super().convert(ctx, argument)
        except BadArgument:
            pass
        else:
            return basic_role
        guild = ctx.guild
        result = [
            (r[2], r[1])
            for r in process.extract(
                argument,
                {r: unidecode(r.name) for r in guild.roles},
                limit=None,

            )
        ]
        if not result:
            raise BadArgument(f'Role "{argument}" not found.' if self.response else None)

        sorted_result = sorted(result, key=lambda r: r[1], reverse=True)
        return sorted_result[0][0]


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


class Role(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.__class__.__name__} Cog has been loaded\n-----")

    @commands.command(aliases=["roleadd","roleremove","roletemp","temprole","rolelist","allroles","roles","roleinfo","roleall","rolehumans","rolebots","rolecreate","roledelete","rolecolor"],hidden=True)
    async def _roleAliases(self, ctx):
        e = discord.Embed(
            title="Commands have changed!",
            description=f"All role commands have been made into one big sub-command! \n\n Run ``{ctx.prefix}role`` for more details!",
            color=self.bot.red,
            timestamp=ctx.message.created_at
        )
        await ctx.reply(embed=e, mention_author=False)



    @commands.group(name="role",invoke_without_command=True,case_insensitive=True,aliases=["r"])
    @commands.has_guild_permissions(manage_roles=True)
    async def _role(self, ctx):

        em = discord.Embed(
            title="Metro Role Utils",
            description=f"```yaml\nCommand: {ctx.prefix}role``` \n\n**Very complex role utilities** \n\n**Sub-commands:**\n``add`` - add a role to a user \n``remove`` - remove a role from a user \n``temp`` - give a role to someone temporarily\n\n``list`` - list all the roles \n``detailedlist`` - get a list of roles very detailed\n``info`` - get information on a role\n``create`` - create a new role \n``delete`` - delete an exisiting role \n\n``all`` - give everyone a role\n``bots`` - give all bots a role\n``humans`` - give all non-bots a role",
            color=self.bot.aqua,
            timestamp=ctx.message.created_at)
        await ctx.reply(embed=em, mention_author=False)

    @_role.command(name="add")
    async def _add(self, ctx, member : discord.Member, role : BetterRoles, reason=None):


        if not ctx.author is ctx.guild.owner:
            if ctx.author.top_role < role:
                await ctx.message.add_reaction(self.bot.cross)
                em = discord.Embed(
                    title="An error occured!",
                    description=f"You cannot add this role because your top role is not higher than {role.mention} \n\n**Your top role:** {ctx.author.top_role.mention} - Position **{ctx.author.top_role.position}**\n**Role you want to add:** {role.mention} - Position **{role.position}**",
                    color=self.bot.red,
                    timestamp=ctx.message.created_at
                )
                return await ctx.reply(embed=em, mention_author=False)

        em = discord.Embed(
            title="Role added!",
            description=f"Added the role {role.mention} to {member.mention} -``{member.id}``\n**Reason:** {reason}",
            color=self.bot.green,
            timestamp=ctx.message.created_at
        )
        await ctx.message.add_reaction(self.bot.check)
        await member.add_roles(role, reason=reason)
        await ctx.reply(embed=em, mention_author=False)

    @_role.command(name="remove")
    async def _remove(self, ctx, member : discord.Member, role : BetterRoles, reason=None):

        if not ctx.author is ctx.guild.owner:
            if ctx.author.top_role < role:
                await ctx.message.add_reaction(self.bot.cross)
                em = discord.Embed(
                    title="An error occured!",
                    description=f"You cannot remove this role because your top role is not higher than {role.mention} \n\n**Your top role:** {ctx.author.top_role.mention} - Position **{ctx.author.top_role.position}**\n**Role you want to add:** {role.mention} - Position **{role.position}**",
                    color=self.bot.red,
                    timestamp=ctx.message.created_at
                )
                return await ctx.reply(embed=em, mention_author=False)

        em = discord.Embed(
            title="Role removed!",
            description=f"Removed the role {role.mention} to {member.mention} -``{member.id}``\n**Reason:** {reason}",
            color=self.bot.red,
            timestamp=ctx.message.created_at
        )
        await ctx.message.add_reaction(self.bot.check)
        await member.remove_roles(role, reason=reason)
        await ctx.reply(embed=em, mention_author=False)

    @_role.command(name="temp")
    async def _temp(self, ctx, member : discord.Member, role : BetterRoles, time : TimeConverter, * , reason=None):

        if not ctx.author is ctx.guild.owner:
            if ctx.author.top_role < role:
                await ctx.message.add_reaction(self.bot.cross)
                em = discord.Embed(
                    title="An error occured!",
                    description=f"You cannot add this role because your top role is not higher than {role.mention} \n\n**Your top role:** {ctx.author.top_role.mention} - Position **{ctx.author.top_role.position}**\n**Role you want to add:** {role.mention} - Position **{role.position}**",
                    color=self.bot.red,
                    timestamp=ctx.message.created_at
                )
                return await ctx.reply(embed=em, mention_author=False)

        if time < 3:
            await ctx.message.add_reaction(self.bot.cross)
            return await ctx.reply("You cannot give a role for less than 3 seconds!",mention_author=False)

        minutes, seconds = divmod(time, 60)
        hours, minutes = divmod(minutes, 60)
        days, hours = divmod(hours, 24)

        if int(days):
            time = f"**{days}** days, **{hours}** hours, **{minutes}** minutes, **{seconds}** seconds"
        if int(hours) and int(days) is 0:
            time = f"**{hours}** hours, **{minutes}** minutes, **{seconds}** seconds"
        if int(minutes) and int(hours) is 0:
            time = f"**{minutes}** minutes, **{seconds}** seconds"
        if int(seconds) and int(minutes) is 0:
            time = f"**{seconds}** seconds"

        em = discord.Embed(
            title="Temporal role added!",
            description=f"Added the role {role.mention} to {member.mention} -``{member.id}``\n**Reason:** {reason} \n**Time:** {time}",
            color=self.bot.aqua,
            timestamp=ctx.message.created_at
        )
        await ctx.message.add_reaction(self.bot.check)
        await member.add_roles(role, reason=reason)
        await ctx.reply(embed=em, mention_author=False)


    @_role.command(name="detailedlist",aliases=["dlist"])
    async def _detailedlist(self, ctx):
        """Very detailed list of roles!"""

        data = []
        description = f"Roles for {ctx.guild.name}"
        for r in sorted(list(ctx.guild.roles), key=lambda x: x.position, reverse=True):
            if r.name == "@everyone":
                continue
            name = r.name[:10] + "..." if len(r.name) > 13 else r.name
            data.append([name, str(r.id), f"{r.color} (0x{str(r.color).strip('#')})"])
        kwargs = {
            "tabular_data": data,
            "tablefmt": "simple",
            "headers": ["Role Name", "Role ID", "Color"],
        }
        data = tabulate(**kwargs)
        for page in pagify(data, page_length=1998):
            page = box(page, lang="cs")

            await ctx.message.add_reaction(self.bot.check)
            await ctx.send(
                    embed=discord.Embed(
                        description=page,
                        color=self.bot.aqua,
                    ),
                mention_author=False
                )


    @_role.command(name="list")
    async def _list(self, ctx):
        """List all roles in this guild."""

        data = []
        description = f"Roles for {ctx.guild.name}"
        for r in sorted(list(ctx.guild.roles), key=lambda x: x.position, reverse=True):
            if r.name == "@everyone":
                continue

            data.append([r.mention])
        kwargs = {
            "tabular_data": data,
            "tablefmt": "simple",
            "headers": ["Role Name", "Role ID", "Color"],
        }
        data = tabulate(**kwargs)
        for page in pagify(data, page_length=1998):
            await ctx.message.add_reaction(self.bot.check)
            await ctx.reply(
                    embed=discord.Embed(
                        description=page,
                        color=self.bot.aqua,
                    ),
                mention_author=False
                )


    @_role.command(name="info",aliases=["information"])
    async def _info(self, ctx, role : BetterRoles):
        await ctx.message.add_reaction(self.bot.check)
        await ctx.reply(embed=await self.get_info(role),mention_author=False)

    async def get_info(self, role: discord.Role) -> discord.Embed:
        if guild_roughly_chunked(role.guild) is False and self.bot.intents.members:
            await role.guild.chunk()
        description = [
            f"{role.mention} ``{role.id}``",
            f"Members: {len(role.members)} | Position: {role.position}",
            f"Color: {role.color}",
            f"Hoisted: {role.hoist}",
            f"Mentionable: {role.mentionable}",
        ]

        e = discord.Embed(
            color=role.color,
            title=role.name,
            description="\n".join(description),
            timestamp=role.created_at
        )
        e.set_footer(text="Created at ")

        return e

    @_role.command(name="create",aliases=["make"])
    async def _create(self, ctx, color: Optional[discord.Color] = discord.Color.default(), hoist: Optional[bool] = False, * , name : str ):

        if len(ctx.guild.roles) >= 250:
            await ctx.message.add_reaction(self.bot.cross)
            return await ctx.reply("This server has reached the maximum role limit (250)",mention_author=False)

        embed = discord.Embed(
            title="Confirmation",
            description=f"Are you sure you want to create this role? \n\nName: {name} \nHoist: {hoist}\nColor: {color}",
            color=self.bot.yellow,
            timestamp=ctx.message.created_at
        )
        m = await ctx.reply(embed=embed)
        await m.add_reaction(self.bot.check)
        await m.add_reaction(self.bot.cross)

        try:
            reaction, member = await self.bot.wait_for(
                "reaction_add",
                timeout=30,
                check=lambda reaction, user: user == ctx.author
                and reaction.message.channel == ctx.channel
            )
        except asyncio.TimeoutError:
            await ctx.reply("Confirmation Failure. Please try again",mention_author=False)
            return

        emojis = [self.bot.check, self.bot.cross]

        if str(reaction.emoji) not in emojis or str(reaction.emoji) == self.bot.cross:
            await ctx.message.add_reaction(self.bot.cross)
            await ctx.reply("Canceling create role task!",mention_author=False)
            return

        await m.delete()

        role = await ctx.guild.create_role(name=name, colour=color, hoist=hoist)
        await ctx.reply(f"**{role}** role created!",embed=await self.get_info(role))
        await ctx.message.add_reaction(self.bot.check)


    @_role.command(name="delete",aliases=["trash","del",])
    async def _delete(self, ctx, role : BetterRoles):

        embed = discord.Embed(
            title="Confirmation",
            description=f"Are you sure you want to delete {role.mention}",
            color=self.bot.orange,
            timestamp=ctx.message.created_at
        )
        m = await ctx.reply(embed=embed)
        await m.add_reaction(self.bot.check)
        await m.add_reaction(self.bot.cross)

        try:
            reaction, member = await self.bot.wait_for(
                "reaction_add",
                timeout=30,
                check=lambda reaction, user: user == ctx.author
                and reaction.message.channel == ctx.channel
            )
        except asyncio.TimeoutError:
            await ctx.reply("Confirmation Failure. Please try again",mention_author=False)
            return

        emojis = [self.bot.check, self.bot.cross]

        if str(reaction.emoji) not in emojis or str(reaction.emoji) == self.bot.cross:
            await m.delete()
            await ctx.message.add_reaction(self.bot.cross)
            await ctx.reply("Canceling delete role task!",mention_author=False)
            return

        await m.delete()

        await role.delete()
        await ctx.message.add_reaction(self.bot.check)
        e = discord.Embed(
            title="Success!",
            description=f"Successfully deleted **{role}**",
            color=self.bot.green
        )
        await ctx.reply(embed=e)









def setup(bot):
    bot.add_cog(Role(bot))