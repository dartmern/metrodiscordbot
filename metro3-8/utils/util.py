import asyncio

import discord
from discord.ext.buttons import Paginator
from discord.ext import commands

from typing import Iterator, Sequence


async def super_massrole(
        self,
        ctx: commands.Context,
        members: list,
        role: discord.Role,
        fail_message: str = "Everyone in the server has this role.",
        adding: bool = True,
):
    if guild_roughly_chunked(ctx.guild) is False and self.bot.intents.members:
        await ctx.guild.chunk()
    member_list = self.get_member_list(members, role, adding)
    if not member_list:
        await ctx.send(fail_message)
        return
    verb = "add" if adding else "remove"
    word = "to" if adding else "from"
    await ctx.send(
        f"Beginning to {verb} **{role.name}** {word} **{len(member_list)}** members."
    )
    async with ctx.typing():
        result = await self.massrole(member_list, [role], get_audit_reason(ctx.author), adding)
        result_text = f"{verb.title()[:5]}ed **{role.name}** {word} **{len(result['completed'])}** members."
        if result["skipped"]:
            result_text += (
                f"\nSkipped {verb[:5]}ing roles for **{len(result['skipped'])}** members."
            )
        if result["failed"]:
            result_text += (
                f"\nFailed {verb[:5]}ing roles for **{len(result['failed'])}** members."
            )
    await ctx.send(result_text)


class Pag(Paginator):
    async def teardown(self):
        try:
            await self.page.clear_reactions()
        except discord.HTTPException:
            pass




class Context(commands.Context):

    @property
    def embed_color(self):
        # Rather than double awaiting.
        return self.embed_colour

    async def embed_requested(self):
        """
        Simple helper to call bot.embed_requested
        with logic around if embed permissions are available

        Returns
        -------
        bool:
            :code:`True` if an embed is requested
        """
        if self.guild and not self.channel.permissions_for(self.guild.me).embed_links:
            return False
        return await self.bot.embed_requested(self.channel, self.author, command=self.command)


async def GetMessage(
        bot, ctx, contentOne="Default Message", contentTwo="\uFEFF", timeout=100
):
    """
    This function sends an embed containing the params and then waits for a message to return
    Params:
     - bot (commands.Bot object) :
     - ctx (context object) : Used for sending msgs n stuff
     - Optional Params:
        - contentOne (string) : Embed title
        - contentTwo (string) : Embed description
        - timeout (int) : Timeout for wait_for
    Returns:
     - msg.content (string) : If a message is detected, the content will be returned
    or
     - False (bool) : If a timeout occurs
    """
    embed = discord.Embed(
        title=f"{contentOne}",
        description=f"{contentTwo}",
    )
    sent = await ctx.send(embed=embed)
    try:
        msg = await bot.wait_for(
            "message",
            timeout=timeout,
            check=lambda message: message.author == ctx.author
                                  and message.channel == ctx.channel,
        )
        if msg:
            return msg.content
    except asyncio.TimeoutError:
        return False

    async def super_massrole(
            self,
            ctx: commands.Context,
            members: list,
            role: discord.Role,
            fail_message: str = "Everyone in the server has this role.",
            adding: bool = True,
    ):
        if guild_roughly_chunked(ctx.guild) is False and self.bot.intents.members:
            await ctx.guild.chunk()
        member_list = self.get_member_list(members, role, adding)
        if not member_list:
            await ctx.send(fail_message)
            return
        verb = "add" if adding else "remove"
        word = "to" if adding else "from"
        await ctx.send(
            f"Beginning to {verb} **{role.name}** {word} **{len(member_list)}** members."
        )
        async with ctx.typing():
            result = await self.massrole(member_list, [role], get_audit_reason(ctx.author), adding)
            result_text = f"{verb.title()[:5]}ed **{role.name}** {word} **{len(result['completed'])}** members."
            if result["skipped"]:
                result_text += (
                    f"\nSkipped {verb[:5]}ing roles for **{len(result['skipped'])}** members."
                )
            if result["failed"]:
                result_text += (
                    f"\nFailed {verb[:5]}ing roles for **{len(result['failed'])}** members."
                )
        await ctx.send(result_text)


def clean_code(content):
    if content.startswith("```") and content.endswith("```"):
        return "\n".join(content.split("\n")[1:])[:-3]
    if content.startswith("```py") and content.endswith("```"):
        return "\n".join(content.split("\n")[1:])[:-3]
    else:
        return content


def box(text: str, lang: str = "") -> str:
    """Get the given text in a code block.
    Parameters
    ----------
    text : str
        The text to be marked up.
    lang : `str`, optional
        The syntax highlighting language for the codeblock.
    Returns
    -------
    str
        The marked up text.
    """
    ret = "```{}\n{}\n```".format(lang, text)
    return ret


def escape(text: str, *, mass_mentions: bool = False, formatting: bool = False) -> str:
    """Get text with all mass mentions or markdown escaped.
    Parameters
    ----------
    text : str
        The text to be escaped.
    mass_mentions : `bool`, optional
        Set to :code:`True` to escape mass mentions in the text.
    formatting : `bool`, optional
        Set to :code:`True` to escape any markdown formatting in the text.
    Returns
    -------
    str
        The escaped text.
    """
    if mass_mentions:
        text = text.replace("@everyone", "@\u200beveryone")
        text = text.replace("@here", "@\u200bhere")
    if formatting:
        text = discord.utils.escape_markdown(text)
    return text


def pagify(
        text: str,
        delims: Sequence[str] = ["\n"],
        *,
        priority: bool = False,
        escape_mass_mentions: bool = True,
        shorten_by: int = 8,
        page_length: int = 2000,
) -> Iterator[str]:
    """Generate multiple pages from the given text.
    Note
    ----
    This does not respect code blocks or inline code.
    Parameters
    ----------
    text : str
        The content to pagify and send.
    delims : `sequence` of `str`, optional
        Characters where page breaks will occur. If no delimiters are found
        in a page, the page will break after ``page_length`` characters.
        By default this only contains the newline.
    Other Parameters
    ----------------
    priority : `bool`
        Set to :code:`True` to choose the page break delimiter based on the
        order of ``delims``. Otherwise, the page will always break at the
        last possible delimiter.
    escape_mass_mentions : `bool`
        If :code:`True`, any mass mentions (here or everyone) will be
        silenced.
    shorten_by : `int`
        How much to shorten each page by. Defaults to 8.
    page_length : `int`
        The maximum length of each page. Defaults to 2000.
    Yields
    ------
    `str`
        Pages of the given text.
    """
    in_text = text
    page_length -= shorten_by
    while len(in_text) > page_length:
        this_page_len = page_length
        if escape_mass_mentions:
            this_page_len -= in_text.count("@here", 0, page_length) + in_text.count(
                "@everyone", 0, page_length
            )
        closest_delim = (in_text.rfind(d, 1, this_page_len) for d in delims)
        if priority:
            closest_delim = next((x for x in closest_delim if x > 0), -1)
        else:
            closest_delim = max(closest_delim)
        closest_delim = closest_delim if closest_delim != -1 else this_page_len
        if escape_mass_mentions:
            to_send = escape(in_text[:closest_delim], mass_mentions=True)
        else:
            to_send = in_text[:closest_delim]
        if len(to_send.strip()) > 0:
            yield to_send
        in_text = in_text[closest_delim:]

    if len(in_text.strip()) > 0:
        if escape_mass_mentions:
            yield escape(in_text, mass_mentions=True)
        else:
            yield in_text


def guild_roughly_chunked(guild: discord.Guild) -> bool:
    return len(guild.members) / guild.member_count > 0.9
