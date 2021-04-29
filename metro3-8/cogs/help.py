from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
from utils.util import Pag
import discord

class Help(commands.Cog, name="Help command"):
    def __init__(self, bot):
        self.bot = bot
        self.cmds_per_page = 3

    def get_command_signature(self, command: commands.Command, ctx: commands.Context):
        aliases = "|".join(command.aliases)
        cmd_invoke = f"{command.name}" if command.aliases else command.name

        full_invoke = command.qualified_name.replace(command.name, "")

        signature = f"{ctx.prefix}{full_invoke}{cmd_invoke} {command.signature}"
        return signature

    async def return_filtered_commands(self, walkable, ctx):
        filtered = []

        for c in walkable.walk_commands():
            try:
                if c.hidden:
                    continue

                elif c.parent:
                    continue

                await c.can_run(ctx)
                filtered.append(c)
            except commands.CommandError:
                continue

        return self.return_sorted_commands(filtered)

    def return_sorted_commands(self, commandList):
        return sorted(commandList, key=lambda x: x.name)


    async def setup_help_pag(self, ctx, entity=None, title=None):

        title = title or self.bot.description

        pages = []

        if isinstance(entity, commands.Group):

            commands_entry = ""


            cmd = self.bot.get_command(str(entity))

            if cmd.aliases:
                alias = ", ".join(cmd.aliases)
                sig = self.get_command_signature(cmd, ctx)
                var = (

                            f"```yaml\nCommand: {sig}\nAliases: {ctx.prefix}{alias}```\n**{cmd.description}**\n\nRun `{ctx.prefix}help [command]` for more info on a command\nStill stuck? [`Click Here`]({self.bot.support}) to join our support server\n\n**Sub commands for {cmd.name}:**"
                        )
            else:
                sig = self.get_command_signature(cmd, ctx)
                var = (

                            f"```yaml\nCommand: {sig}```\n**{cmd.description}**\n\nRun `{ctx.prefix}help [command]` for more info on a command\nStill stuck? [`Click Here`]({self.bot.support}) to join our support server\n\n**Sub commands for {cmd.name}:**"
                        )


            pages.append(commands_entry)
            pages.append(var)


            command = self.bot.get_command(str(entity))

            all_cmds = command.commands

            entry = ""

            for cmd in all_cmds:
                entry +=(

                    f"\n`{cmd.name}` - {cmd.description}"


                )




            pages.append(entry)





        else:

            try:
                filtered_commands = (
                list(set(entity.all_commands.values()))
                if hasattr(entity, "all_commands")
                else []
                )
                filtered_commands.insert(0, entity)

            except:
                filtered_commands = await self.return_filtered_commands(entity, ctx)

            for i in range(0, len(filtered_commands), self.cmds_per_page):
                next_commands = filtered_commands[i: i + self.cmds_per_page]

                for cmd in next_commands:
                    sig = self.get_command_signature(cmd, ctx)


                    if cmd.aliases:
                        alias = ", ".join(cmd.aliases)
                        var = (

                            f"```yaml\nCommand: {sig}\nAliases: {ctx.prefix}{alias}```\n**{cmd.description}**\n\nRun `{ctx.prefix}help [command]` for more info on a command\nStill stuck? [`Click Here`]({self.bot.support}) to join our support server"
                        )
                    else:
                        var = (

                            f"```yaml\nCommand: {sig}```\n**{cmd.description}**\n\nRun `{ctx.prefix}help [command]` for more info on a command\nStill stuck? [`Click Here`]({self.bot.support}) to join our support server"
                        )

            pages.append(var)






        await Pag(title=f"{cmd.name} help", color=self.bot.aqua, entries=pages, length=3).start(ctx)


    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.__class__.__name__} cog has been loaded\n-----")

    @commands.command(
        name="help", aliases=["h", "commands"], description="The help command!")
    async def help_command(self, ctx, *, entity=None):
        if not entity:
            em = discord.Embed(
                title="Metro's Help Center",
                description=f"Thanks for using and inviting Metro Discord Bot to your server!\nIf you want to see all my commands `{ctx.prefix}h all`\nIf you need help on a command run `{ctx.prefix}h [command]`\n\nSome information commands: `{ctx.prefix}info`, `{ctx.prefix}prefix`, `{ctx.prefix}support`\n\nStill need help? Join our [[`SUPPORT SERVER`]]({self.bot.support}) for additional support!",
                color=self.bot.aqua
            )
            await ctx.send(embed=em)

        else:
            cog = self.bot.get_cog(entity)
            if cog:
                await self.setup_help_pag(ctx, cog, f"{cog.qualified_name}'s commands")

            else:
                command = self.bot.get_command(entity)

                if command:
                    await self.setup_help_pag(ctx, command)

                else:
                    await ctx.reply(f"The help topic `{entity}` not found",mention_author=False)


def setup(bot):
    bot.add_cog(Help(bot))