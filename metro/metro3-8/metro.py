# Standard libraries
import os
import json
import logging
import datetime
import asyncio
# Third party libraries
import discord
from pathlib import Path
import motor.motor_asyncio
from discord.ext import commands

# Local code
import utils.json_loader
from utils.mongo import Document

cwd = Path(__file__).parents[0]
cwd = str(cwd)
print(f"{cwd}\n-----")

intents = discord.Intents.default()
intents.members = True


async def get_prefix(bot, message):
    # If dm's
    if not message.guild:
        return commands.when_mentioned_or("-")(bot, message)

    try:
        data = await bot.config.find(message.guild.id)

        # Make sure we have a useable prefix
        if not data or "prefix" not in data:
            return commands.when_mentioned_or("-")(bot, message)
        return commands.when_mentioned_or(data["prefix"])(bot, message)
    except:
        return commands.when_mentioned_or("-")(bot, message)


# Defining a few things
secret_file = utils.json_loader.read_json('secrets')
bot = commands.Bot(
    command_prefix=get_prefix, case_insensitive=True, owner_id=525843819850104842,intents=intents)
bot.config_token = secret_file["token"]
bot.connection_url = secret_file["mongo"]
logging.basicConfig(level=logging.INFO)

bot.support = 'https://discord.gg/HgaGG9yAuH'

bot.cwd = cwd

bot.version = "0.8.7"

bot.remove_command('help')

bot.muted_users = {}
bot.timers = {}

bot.triangle = ":small_red_triangle:"

bot.nothing = '\u3164'
bot.aqua = int(0x11806A)
bot.colors = {
    "WHITE": 0xFFFFFF,
    "AQUA": 0x1ABC9C,
    "GREEN": 0x2ECC71,
    "BLUE": 0x3498DB,
    "PURPLE": 0x9B59B6,
    "LUMINOUS_VIVID_PINK": 0xE91E63,
    "GOLD": 0xF1C40F,
    "ORANGE": 0xE67E22,
    "RED": 0xE74C3C,
    "NAVY": 0x34495E,
    "DARK_AQUA": 0x11806A,
    "DARK_GREEN": 0x1F8B4C,
    "DARK_BLUE": 0x206694,
    "DARK_PURPLE": 0x71368A,
    "DARK_VIVID_PINK": 0xAD1457,
    "DARK_GOLD": 0xC27C0E,
    "DARK_ORANGE": 0xA84300,
    "DARK_RED": 0x992D22,
    "DARK_NAVY": 0x2C3E50,
}
bot.color_list = [c for c in bot.colors.values()]

bot.warns = {}


bot.check = '<:m_check:794749633305247785>'
bot.cross = '<:m_cross:794749633255571476>'

bot.loading = '<a:loading:794273757459775530>'


bot.blacklisted_users = []

@bot.event
async def on_ready():

    serverCount = len(bot.guilds)
    # On ready, print some details to standard out
    print(
        f"-----\nLogged in as: {bot.user.name} : {bot.user.id}\n-----\nMy current prefix is: -\n-----")


    bot.mongo = motor.motor_asyncio.AsyncIOMotorClient(str(bot.connection_url))
    bot.db = bot.mongo["bot_config"]
    bot.config = Document(bot.db, "config")
    bot.mutes = Document(bot.db, "mutes")
    bot.warns = Document(bot.db, "warns")

    bot.command_usage = Document(bot.db, "command_usage")

    bot.blacklist = Document(bot.db, "blacklist")
	
    bot.welcomeOn = Document(bot.db, "welcomeOn")

    bot.welcomeChannel = Document(bot.db, "welcomeChannel")
    bot.welcomeMsg = Document(bot.db, "welcomeMsg")
	
    bot.Bal = Document(bot.db, "botBal")
    bot.Bank = Document(bot.db, "botBank")
    bot.inv = Document(bot.db, "inv")
	
    bot.reactionroles = Document(bot.db, "reactionroles")
	
    bot.timer = Document(bot.db, "timer")
	
    bot.afk = Document(bot.db, "afk")

    bot.settings = Document(bot.db, "settings")
	
    currentMutes = await bot.mutes.get_all()
    

    for mute in currentMutes:
        bot.muted_users[mute["_id"]] = mute
		


    print(bot.timers)
    print(bot.muted_users)

    print("Initialized Database\n-----")


    memberCount = len(bot.users)
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{memberCount} users"))

@bot.event
async def on_guild_join(guild):

    await bot.config.upsert({"_id": guild.id, "prefix": "-"})
    general = guild.text_channels[0]

    for general in guild.text_channels:
        if general and general.permissions_for(guild.me).send_messages:
            em = discord.Embed(color=0x1ABC9C)
            em.add_field(name='Hi! Thanks for inviting me to your server!',value='To get started, send ``-help``. My prefix is ``-`` (example: -help) \n \n If you want to change your prefix run ``-prefix set <new prefix>`` \n \n',inline=False)
            em.add_field(name='**Important Links**',value='[Bot Support Server](https://dsc.gg/metrosupport) - Join this to ask questions and hangout \n[Bot Invite](https://dsc.gg/metro) - Invite the bot to another server\n[Twitter](https://twitter.com/MetroDiscordBot) - Follow us for updates ',inline=False)

            await general.send(embed=em)
            return

    data = {"_id" : guild.id, "muteDmMessage" : "You were muted in **$GUILD** for **$TIME** with the reason: **$REASON**", "muteAuthorMessage" : "You muted $MEMBER for $TIMER with the reason: $REASON"}
    await bot.settings.upsert(data)


@bot.event
async def on_command_error(ctx, error):

	if isinstance(error, commands.errors.CommandNotFound):
		return
		
	if isinstance(error, commands.errors.CommandOnCooldown):
	
		m, s = divmod(error.retry_after, 60)
		h, m = divmod(m, 60)

		if int(h) == 0 and int(m) == 0: 
			await ctx.send(f"You are on cooldown! Please try again in {int(s)} seconds")
			
		else:
			await ctx.send(f"You are on cooldown! Please try again in {int(h)} hours, {int(m)} minutes, {int(s)} seconds")
	
	if isinstance(error, commands.errors.MemberNotFound):
		return await ctx.send(f"Member Not Found! {bot.cross}")
		
	else:
		raise error

@bot.event
async def on_message(message):



    # Ignore messages sent by bot and other bots
    if message.author.bot:
        return
    

	

    # A way to blacklist users from the bot by not processing commands
    # if the author is in the blacklisted_users list
	
    blacklist = await bot.blacklist.get_by_id(message.author.id)
	
    try:
        theMember = blacklist["_id"]
        if message.author.id == theMember:
            return	
    except:
        p = 1
		


    # Whenever the bot is tagged, respond with its prefix
    if message.content.startswith(f"<@!{bot.user.id}>") and \
        len(message.content) == len(f"<@!{bot.user.id}>"):
        data = await bot.config.get_by_id(message.guild.id)
        prefix = data["prefix"]

        if not data or "prefix" not in data:
            prefix = "-"
        else:
            prefix = data["prefix"]
        prefixMsg = await message.channel.send(f"My prefix here is `{prefix}`! If you need more help run my help command: ``{prefix}help``")
        await prefixMsg.add_reaction('👀')


    
    await bot.process_commands(message)



if __name__ == "__main__":
    # When running this file, if it is the 'main' file
    # I.E its not being imported from another python file run this

    for file in os.listdir(cwd + "/cogs"):
        if file.endswith(".py") and not file.startswith("_"):
            bot.load_extension(f"cogs.{file[:-3]}")

    bot.run(bot.config_token)




