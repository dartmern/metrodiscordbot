import discord
from discord.ext import commands
import datetime
import asyncio 
import random
import json
import re


def get_prefix(client,message):

	with open("prefixes.json", 'r') as f:
		prefixes = json.load(f)

	return prefixes[str(message.guild.id)]

client = commands.Bot(command_prefix= get_prefix, case_insensitive=True,owner_id=525843819850104842)

client.remove_command("help")

@client.event
async def on_guild_join(guild):

	with open("prefixes.json", "r") as f:
		prefixes = json.load(f)

	prefixes[str(guild.id)] = "="

	with open("prefixes.json", "w") as f:
		json.dump(prefixes,f)

	general = guild.text_channels[0]

	for general in guild.text_channels:
		if general and general.permissions_for(guild.me).send_messages:

			embed = discord.Embed(title='Thank you for inviting me to your server!',description=f'Metro is a multi-purpose bot that is currenlty under development. It has fun, moderation, economy, and more features! Run the defult prefix is **=** and run =help for commands! \n\nCurrenly you are using the **plus** version of Metro. You already have maxed out the bot! Thank you for buying Metro Plus',color=0xfffffd)
			await general.send(embed=embed)
			return

@client.command()
@commands.has_guild_permissions(administrator= True)
async def prefix(ctx, prefix):

	with open("prefixes.json", "r") as f:
		prefixes = json.load(f)

	prefixes[str(ctx.guild.id)] = prefix 

	with open("prefixes.json", "w") as f:
		json.dump(prefixes,f, indent=4)

	with open("prefixes.json", "r") as f:
		prefixes = json.load(f)

	changed_prefix = prefixes[str(ctx.guild.id)]

	embed1=discord.Embed(title=f'Prefix Changed for {ctx.guild.name}!',description=f"You changed it to:   **{changed_prefix}** \n Keep this DM open or save this so you don't forget!",color=0xfffffd)
	embed2=discord.Embed(title=f'Prefix Changed for {ctx.guild.name}!',description=f"You changed it to:   **{changed_prefix}** \n \n Remember this and don't forget! \n \n Run {prefix}prefix <new-prefix> to change it again!",color=0xfffffd)

	await ctx.channel.send(embed=embed2)
	await ctx.author.send(embed=embed1)

@prefix.error
async def prefix_error(ctx, error):


	with open("prefixes.json", "r") as f:
		prefixes = json.load(f)

	prefix = prefixes[str(ctx.guild.id)]

	if isinstance(error, commands.MissingRequiredArgument):
		embed1 = discord.Embed(title= "Prefix Command", description=f"**Description:** Changes the bot's prefix for the current guild. Current prefix:  **{prefix}**\n**Cooldown:**  0 seconds \n**Usage:** {prefix}prefix <new-prefix> \n**Examples:** \n{prefix}prefix + \n{prefix}prefix /", color=0xFFA500)
		embed1.set_footer(text="Objects in <> are required and objects in () are optional")

		await ctx.send(embed=embed1)
		return

	if isinstance(error, commands.CommandOnCooldown):
		embed2 = discord.Embed(title='Command on Cooldown!',description=f'Command used: **{prefix}prefix <new-prefix>** \n Cooldown: **3 seconds** \n \n Try again later!',color=0xff0000)
		embed2.set_footer(text=f'Want no cooldowns? Upgrade to Metro Plus! Run {prefix}upgrade')

		await ctx.send(embed=embed2)
		return

	if isinstance(error, commands.MissingPermissions):
		embed3 = discord.Embed(title='Missing Permission!',description='You do not have the permissions to run this command \n **Command ran:** {prefix}prefix <new-prefix>',color=0xff0000)

		await ctx.send(embed=embed3)
		return


messages = joined = 0

async def update_stats():
	await client.wait_until_ready()

















@client.command(aliases=['inviteme','joinmyserver'])
@commands.guild_only()
async def invite(ctx):
	embed = discord.Embed(title= 'Invite Metro to your server!',color=0xfffffd)
	embed.add_field(name='Invite Metro',value='Click [here](https://discord.com/api/oauth2/authorize?client_id=788543184082698252&permissions=8&scope=bot) to invite Metro',inline=True)
	embed.add_field(name='Invite Metro Plus',value='Metro Plus is a **paid** plan. To buy join our [support server](https://discord.gg/Pmavu9DV2J)',inline=False)
	embed.add_field(name='Permissions',value='Metro needs **Administrator** permission to run \n You need **Manage Server** to invite Metro',inline=False)
	embed.set_footer(text='Thank you for inviting Metro!')

	await ctx.send(embed=embed)

@client.command(aliases=['supportserver','supportserverinvite'])
@commands.guild_only()
async def support(ctx):

	with open("prefixes.json", "r") as f:
		prefixes = json.load(f)

	prefix = prefixes[str(ctx.guild.id)]

	em = discord.Embed(title='Support for Metro',description='If you have a question, want to give a suggestion, or upgrade to Metro Plus \n join the support server by clicking [here](https://discord.gg/Pmavu9DV2J)',color=0xfffffd)

	em.set_footer(text=f'If you need help with a specifc command run {prefix}help <command>')

	await ctx.send(embed=em)












@client.group(invoke_without_command=True,aliases=['commands','help!'])
async def help(ctx):

	with open("prefixes.json", "r") as f:
		prefixes = json.load(f)

	prefix = prefixes[str(ctx.guild.id)]

	em = discord.Embed(title= "Help for Metro Bot",description=f'Use {prefix}help <command> for extended information on a command.',color=0xFFFF00)
	em.add_field(name='Moderation',value='kick, ban, unban, mute, unmute, lock, unlock, clear, slowmode',inline=True)
	em.add_field(name='Settings',value='prefix, invite',inline=False)
	em.add_field(name='Fun',value='8ball, echo, embed',inline=True)
	em.add_field(name='Server',value='delete, new, rename',inline=True)

	

	await ctx.send(embed=em)


@help.command()
@commands.guild_only()

async def ban(ctx):

	with open("prefixes.json", "r") as f:
		prefixes = json.load(f)

	prefix = prefixes[str(ctx.guild.id)]

	em = discord.Embed(title='Ban Command', description=f'**Description:** Bans a member from the current server \n**Cooldown:** 0 seconds\n**Usage:** {prefix}ban <member> (reason) \n**Examples:** \n{prefix}ban @Gamerkid Ad Spamming \n{prefix}ban @Gamerkid', color=0xFFA500)
	em.set_footer(text="Objects in <> are required and objects in () are optional")
	await ctx.send(embed=em)

@help.command()
@commands.guild_only()

async def unban(ctx):

	with open("prefixes.json", "r") as f:
		prefixes = json.load(f)

	prefix = prefixes[str(ctx.guild.id)]

	em = discord.Embed(title='Unban Command',description=f'**Description:** Unbans a member from the current server \n**Cooldown:** 0 seconds \n**Usage:** {prefix}unban <member> \n**Example:** \n{prefix}unban Gamerkid#1234', color=0xFFA500)
	em.set_footer(text="Objects in <> are required and objects in () are optional")
	await ctx.send(embed=em)

@help.command()
@commands.guild_only()

async def kick(ctx):

	with open("prefixes.json", "r") as f:
		prefixes = json.load(f)

	prefix = prefixes[str(ctx.guild.id)]

	em = discord.Embed(title='Kick Command', description=f'**Description:** Kicks a member from the current server \n**Cooldown:** 0 seconds \n**Usage:** {prefix}kick <member> (reason) \n**Example:** \n{prefix}kick @Gamerkid Stop Spamming \n{prefix}kick @Gamerkid', color=0xFFA500)
	em.set_footer(text="Objects in <> are required and objects in () are optional")
	await ctx.send(embed=em)

@help.command()
@commands.guild_only()

async def mute(ctx):

	with open("prefixes.json", "r") as f:
		prefixes = json.load(f)

	prefix = prefixes[str(ctx.guild.id)]

	em = discord.Embed(title= "Mute Command", description=f'**Description:** Prevents a member from talking in text and voice channels \n**Cooldown:**  0 seconds \n**Usage:** {prefix}mute <member> <time> (reason) \n**Examples:** \n{prefix}mute @Gamerkid 10m Spamming in chat \n{prefix}mute @Noobkid45', color=0xFFA500)
	em.set_footer(text="Objects in <> are required and objects in () are optional")
	await ctx.send(embed=em)

@help.command()
@commands.guild_only()

async def unmute(ctx):

	with open("prefixes.json", "r") as f:
		prefixes = json.load(f)

	prefix = prefixes[str(ctx.guild.id)]

	em = discord.Embed(title='Unmute Command', description=f'**Description:** Unmutes a member that is currently muted \n**Cooldown:** 0 seconds \n**Usage:** {prefix}unmute <member> (reason) \n**Example:** \n{prefix}unmute @Gamerkid Enjoy! \n{prefix}unmute @Gamerkid', color=0xFFA500)
	em.set_footer(text="Objects in <> are required and objects in () are optional")
	await ctx.send(embed=em)


@help.command()
@commands.guild_only()

async def prefix(ctx):

	with open("prefixes.json", "r") as f:
		prefixes = json.load(f)

	prefix = prefixes[str(ctx.guild.id)]

	em = discord.Embed(title= "Prefix Command", description=f"**Description:** Changes the bot's prefix for the current guild. Current prefix:  **{prefix}**\n**Cooldown:**  0 seconds \n**Usage:** {prefix}prefix <new-prefix> \n**Examples:** \n{prefix}prefix + \n{prefix}prefix /", color=0xFFA500)
	em.set_footer(text="Objects in <> are required and objects in () are optional")
	await ctx.send(embed=em)

@help.command()
@commands.guild_only()

async def invite(ctx):

	with open("prefixes.json", "r") as f:
		prefixes = json.load(f)

	prefix = prefixes[str(ctx.guild.id)]

	em = discord.Embed(title= "Invite Command", description=f"**Description:** Invite the bot to your server! \n**Cooldown:**  0 seconds \n**Usage:** {prefix}invite", color=0xFFA500)
	em.set_footer(text="Objects in <> are required and objects in () are optional")
	await ctx.send(embed=em)


@help.command(aliases=['8ball'])
@commands.guild_only()

async def _8ball(ctx):

	with open("prefixes.json", "r") as f:
		prefixes = json.load(f)

	prefix = prefixes[str(ctx.guild.id)]

	em = discord.Embed(title= "8ball Command", description=f"**Description:** Gives you a random answer to your question! \n**Cooldown:**  0 seconds \n**Usage:** {prefix}8ball <question>", color=0xFFA500)
	em.set_footer(text="Objects in <> are required and objects in () are optional")
	await ctx.send(embed=em)

@help.command(aliases=['repeat'])
@commands.guild_only()

async def echo(ctx):

	with open("prefixes.json", "r") as f:
		prefixes = json.load(f)

	prefix = prefixes[str(ctx.guild.id)]

	em = discord.Embed(title= "Echo/Repeat Command", description=f"**Description:** Repeats what you just said \n**Cooldown:**  0 seconds \n**Usage:** {prefix}echo <text>", color=0xFFA500)
	em.set_footer(text="Objects in <> are required and objects in () are optional")
	await ctx.send(embed=em)


@help.command()
@commands.guild_only()

async def embed(ctx):

	with open("prefixes.json", "r") as f:
		prefixes = json.load(f)

	prefix = prefixes[str(ctx.guild.id)]

	em = discord.Embed(title= "Embed Command", description=f'**Description:** Embeds a  message you want\n**Cooldown:**  0 seconds \n**Usage:** {prefix}embed <title> <text>\n**Examples:** \n{prefix}embed red "This is so cool!" "This is also so cool!" \n{prefix}embed green "Quick Embed" "Happy Birthday!"', color=0xFFA500)
	em.set_footer(text="Objects in <> are required and objects in () are optional. Make sure to put title and text in quotes if more than 1 word!")
	await ctx.send(embed=em)


@help.command()
@commands.guild_only()

async def delete(ctx):

	with open("prefixes.json", "r") as f:
		prefixes = json.load(f)

	prefix = prefixes[str(ctx.guild.id)]

	em = discord.Embed(title='Delete Channel Command', description=f'**Description:** Deletes the current channel \n**Cooldown:** 0 seconds\n**Usage:** {prefix}delete ', color=0xFFA500)
	em.set_footer(text="Objects in <> are required and objects in () are optional")
	await ctx.send(embed=em)


@help.command()
@commands.guild_only()

async def rename(ctx):

	with open("prefixes.json", "r") as f:
		prefixes = json.load(f)

	prefix = prefixes[str(ctx.guild.id)]

	em = discord.Embed(title='Rename Channel Command', description=f'**Description:** Renames the current channel \n**Cooldown:** 0 seconds\n**Usage:** {prefix}rename <new-channel-name> \n**Examples:** \n{prefix}rename general-chat \n{prefix}rename bot-commands ', color=0xFFA500)
	em.set_footer(text="Objects in <> are required and objects in () are optional")
	await ctx.send(embed=em)

@help.command()
@commands.guild_only()
async def new(ctx):

	with open("prefixes.json", "r") as f:
		prefixes = json.load(f)

	prefix = prefixes[str(ctx.guild.id)]

	em = discord.Embed(title='New Channel Command', description=f'**Description:** Creates a new channel \n**Cooldown:** 0 seconds\n**Usage:** {prefix}new <channel-name>  \n**Examples:** \n{prefix}new general-chat \n{prefix}new bot-commands-2 ', color=0xFFA500)
	em.set_footer(text="Objects in <> are required and objects in () are optional")
	await ctx.send(embed=em)

@help.command()
@commands.guild_only()
async def lock(ctx):

	with open("prefixes.json", "r") as f:
		prefixes = json.load(f)

	prefix = prefixes[str(ctx.guild.id)]

	em = discord.Embed(title='Lock Channel Command', description=f'**Description:** Locks the current channel or specified channel \n**Cooldown:** 0 seconds\n**Aliases:** lockdown, lockchannel\n**Usage:** {prefix}lock (channel) \n**Examples:** \n{prefix}lock \n{prefix}lock #general-chat ', color=0xFFA500)
	em.set_footer(text="Objects in <> are required and objects in () are optional")
	await ctx.send(embed=em)

@help.command()
@commands.guild_only()
async def unlock(ctx):

	with open("prefixes.json", "r") as f:
		prefixes = json.load(f)

	prefix = prefixes[str(ctx.guild.id)]

	em = discord.Embed(title='Unlock Channel Command', description=f'**Description:** Unlocks the current channel or specified channel \n**Cooldown:** 0 seconds\n**Aliases:** unlockchannel\n**Usage:** {prefix}unlock (channel) \n**Examples:** \n{prefix}unlock \n{prefix}unlock #general-chat ', color=0xFFA500)
	em.set_footer(text="Objects in <> are required and objects in () are optional")
	await ctx.send(embed=em)


@help.command()
@commands.guild_only()

async def clear(ctx):

	with open("prefixes.json", "r") as f:
		prefixes = json.load(f)

	prefix = prefixes[str(ctx.guild.id)]

	em = discord.Embed(title='Clear Messages Command', description=f'**Description:** Clears a set amount of messages \n**Cooldown:** 0 seconds\n**Aliases:** purge, clean\n**Usage:** {prefix}clear (amount) \n**Examples:** \n{prefix}clear 69 \n{prefix}clear 10 ', color=0xFFA500)
	em.set_footer(text="Objects in <> are required and objects in () are optional")
	await ctx.send(embed=em)

@help.command()
@commands.guild_only()
async def upgrade(ctx):

	with open("prefixes.json", "r") as f:
		prefixes = json.load(f)

	prefix = prefixes[str(ctx.guild.id)]

	em = discord.Embed(title='Upgrade Messages Command', description=f'**Description:** Upgrades your Metro bot to the Plus version \n**Cooldown:** 0 seconds\n**Usage:** {prefix}upgrade ', color=0xFFA500)
	em.set_footer(text="Objects in <> are required and objects in () are optional")
	await ctx.send(embed=em)


@help.command()
@commands.guild_only()
async def slowmode(ctx):

	with open("prefixes.json", "r") as f:
		prefixes = json.load(f)

	prefix = prefixes[str(ctx.guild.id)]

	em = discord.Embed(title='Clear Messages Command', description=f'**Description:** Sets the slowmode for the current channel \n**Cooldown:** 3 seconds\n**Aliases:** delay\n**Usage:** {prefix}slowmode <seconds> \n**Examples:** \n{prefix}slowmode 69 \n{prefix}slowmode 2 ', color=0xFFA500)
	em.set_footer(text="Objects in <> are required and objects in () are optional")
	await ctx.send(embed=em)


































@client.command(pass_context=True)
@commands.guild_only()
@commands.has_guild_permissions(mute_members=True)	
async def mute(ctx, user: discord.Member, time, reason=None):

	with open("prefixes.json", "r") as f:
		prefixes = json.load(f)

	prefix = prefixes[str(ctx.guild.id)]

	member = member
	guild=ctx.guild

	role1 = discord.utils.get(member.guild.roles, name = "▼Muted▼")
	mutedRole = discord.utils.get(guild.roles, name="▼Muted▼")

	
	msg_member = discord.Embed(title='Muted!',description=f'You were muted in **{guild}** for **{reason}**', color=0xff0000)
	msg_channel= discord.Embed(title='Sucess!',description=f'You muted {member.mention} for **{reason}**', color=0x00FF00)

	alr_muted = discord.Embed(title='User already Muted!',description=f'The user is already muted! Use ``{prefix}unmute <member>`` to unmute them',color=0xFFA500)

	error = discord.Embed(title='Error!',description='This member is a **mod/admin.** I cannot mute them.',color=0xFFA500)

	do_not = discord.Embed(title='Created Muted Role!',description='Please do **NOT** change the name of the Muted role I created or delete it',color=0xFFA500)

	#If statements
	if role1 in member.roles:
		await ctx.send(embed=alr_muted)
		return

	if member.guild_permissions.manage_guild or member.guild_permissions.administrator:
		await ctx.send(embed=error)
		return

	if not mutedRole:
		mutedRole = await guild.create_role(name = "▼Muted▼")
		await ctx.send(embed=do_not)

		for  channel in guild.channels:
			await channel.set_permissions(mutedRole, speak=False, send_messages=False)
			
	await member.add_roles(mutedRole, reason=reason)

	after_mute	= discord.Embed(title='Unmuted!',description=f'You were unmuted in **{guild}** because your mute ended',color=0x00FF00)


	


	if time[-1].lower() == "h":
		msg_member = discord.Embed(title='Muted!',description=f'You were muted in **{guild}**! \n **Time:** {time}  \n**Reason:** {reason}', color=0xff0000)
		msg_channel= discord.Embed(title='Sucess!',description=f'You muted {member.mention} \n\n **Time:** {time}  \n**Reason:** {reason}', color=0x00FF00)
		msg_channel.set_footer(text=f'Use {prefix}unmute <member> to unmute someone')

		await ctx.send(embed=msg_channel)
		await member.send(embed=msg_member)
		await asyncio.sleep(int(time[:-1]) * 3600)
		await member.remove_roles(mutedRole)
		await ctx.send(embed=after_mute)
		return

	if time[-1].lower() == "m":
		msg_member = discord.Embed(title='Muted!',description=f'You were muted in **{guild}**! \n **Time:** {time}  \n**Reason:** {reason}', color=0xff0000)
		msg_channel= discord.Embed(title='Sucess!',description=f'You muted {member.mention} \n\n **Time:** {time} \n**Reason:** {reason}', color=0x00FF00)
		msg_channel.set_footer(text=f'Use {prefix}unmute <member> to unmute someone')

		await ctx.send(embed=msg_channel)
		await member.send(embed=msg_member)
		await asyncio.sleep(int(time[:-1]) * 60)
		await member.remove_roles(mutedRole)
		await ctx.send(embed=after_mute)
		return

	if time[-1].lower() == "d":
		msg_member = discord.Embed(title='Muted!',description=f'You were muted in **{guild}**! \n **Time:** {time}  \n**Reason:** {reason}', color=0xff0000)
		msg_channel= discord.Embed(title='Sucess!',description=f'You muted {member.mention} \n\n **Time:** {time} \n**Reason:** {reason}', color=0x00FF00)
		msg_channel.set_footer(text=f'Use {prefix}unmute <member> to unmute someone')

		await ctx.send(embed=msg_channel)
		await member.send(embed=msg_member)
		await asyncio.sleep(int(time[:-1]) * 86400)
		await member.remove_roles(mutedRole)
		await ctx.send(embed=after_mute)
		return
		

	if time[-1].lower() == "s":
		msg_member = discord.Embed(title='Muted!',description=f'You were muted in **{guild}**! \n **Time:** {time} \n**Reason:** {reason}', color=0xff0000)
		msg_channel= discord.Embed(title='Sucess!',description=f'You muted {member.mention} \n\n **Time:** {time} \n**Reason:** {reason}', color=0x00FF00)
		msg_channel.set_footer(text=f'Use {prefix}unmute <member> to unmute someone')

		await ctx.send(embed=msg_channel)
		await member.send(embed=msg_member)
		await asyncio.sleep(int(time[:-1]) * 1)
		await member.remove_roles(mutedRole)
		await ctx.send(embed=after_mute)
		return


	msg_member = discord.Embed(title='Muted!',description=f"You were muted in **{guild}**! \n**Time:** None (the person who muted you didn't specify a time) \n**Reason:** {reason}", color=0xff0000)
	msg_channel= discord.Embed(title='Sucess!',description=f'You muted {member.mention}! \n\n**Time:** None (member is muted until someone unmutes him/her) \n**Reason:** {reason}', color=0x00FF00)

	await member.send(embed=msg_member)
	await ctx.send(embed=msg_channel)
	return







@mute.error
async def mute_error(ctx, error):

	with open("prefixes.json", "r") as f:
		prefixes = json.load(f)

	prefix = prefixes[str(ctx.guild.id)]

	if isinstance(error, commands.MissingRequiredArgument):
		embed1 = discord.Embed(title= "Mute Command", description=f'**Description:** Prevents a member from talking in text and voice channels \n**Cooldown:**  0 seconds \n**Usage:** {prefix}mute <member> <time> (reason) \n**Examples:** \n{prefix}mute @Gamerkid Spamming in chat \n{prefix}mute @Noobkid45 1d dm advertising', color=0xFFA500)
		embed1.set_footer(text="Objects in <> are required and objects in () are optional")

		await ctx.send(embed=embed1)
		return

	if isinstance(error, commands.CommandOnCooldown):
		embed2 = discord.Embed(title='Command on Cooldown!',description=f'Command used: **{prefix}mute <member> <time> (reason)** \n Cooldown: **3 seconds** \n \n Try again later!',color=0xff0000)
		embed2.set_footer(text=f'Want no cooldowns? Upgrade to Metro Plus! Run {prefix}upgrade')

		await ctx.send(embed=embed2)
		return

	if isinstance(error, commands.MissingPermissions):
		embed3 = discord.Embed(title='Missing Permission!',description=f'You do not have the permissions to run this command \n **Command ran:** {prefix}mute <member> <time> (reason)',color=0xff0000)

		await ctx.send(embed=embed3)
		return

	else:
		raise error


@client.command()
@commands.guild_only()
@commands.has_guild_permissions(mute_members=True)
async def unmute(ctx, member : discord.Member, *, reason=None):

	with open("prefixes.json", "r") as f:
		prefixes = json.load(f)

	prefix = prefixes[str(ctx.guild.id)]

	guild=ctx.guild

	mutedRole = discord.utils.get(guild.roles, name="▼Muted▼")
	has_mutedRole = discord.utils.get(member.roles, name="▼Muted▼")

	#Embeds sent to Channel
	not_muted = discord.Embed(title='Error!', description=f"This person isn't even muted! Use ``{prefix}mute <member> (reason)`` to muted someone!",color=0xFFA500)
	not_setup = discord.Embed(title='No Muted Role detected!',description='Please do **not** change the name of the role. Run ``{prefix}mute <member> (reason)`` to mute this person again and setup a Muted Role!',color=0xFFA500)

	msg_channel = discord.Embed(title='Sucess!',description=f'You unmuted {member.mention} for **{reason}**',color=0x00FF00)
	msg_member	= discord.Embed(title='Unmuted!',description=f'You were unmuted in **{guild}** for **{reason}**',color=0x00FF00)

	if not mutedRole:
		await ctx.send(embed=not_setup)
		return

	if not has_mutedRole:
		await ctx.send(embed=not_muted)
		return

	await member.remove_roles(mutedRole)
	await ctx.send(embed=msg_channel)
	await member.send(embed=msg_member)

@unmute.error
async def unmute_error(ctx, error):

	with open("prefixes.json", "r") as f:
		prefixes = json.load(f)

	prefix = prefixes[str(ctx.guild.id)]

	if isinstance(error, commands.MissingRequiredArgument):
		embed1 = discord.Embed(title='Unmute Command', description=f'**Description:** Unmutes a member that is currently muted \n**Cooldown:** 0 seconds \n**Usage:** {prefix}unmute <member> (reason) \n**Example:** \n{prefix}unmute @Gamerkid Enjoy! \n{prefix}unmute @Gamerkid', color=0xFFA500)
		embed1.set_footer(text="Objects in <> are required and objects in () are optional")
	
		await ctx.send(embed=embed1)
		return

	if isinstance(error, commands.CommandOnCooldown):
		embed2 = discord.Embed(title='Command on Cooldown!',description=f'Command used: **{prefix}unmute <member> (reason)** \n Cooldown: **3 seconds** \n \n Try again later!',color=0xff0000)
		embed2.set_footer(text=f'Want no cooldowns? Upgrade to Metro Plus! Run {prefix}upgrade')

		await ctx.send(embed=embed2)
		return

	if isinstance(error, commands.MissingPermissions):
		embed3 = discord.Embed(title='Missing Permission!',description=f'You do not have the permissions to run this command \n **Command ran:** {prefix}unmute <member> (reason)',color=0xff0000)

		await ctx.send(embed=embed3)
		return



@client.command()
@commands.guild_only()
@commands.has_guild_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):

	guild=ctx.guild

	msg_member = discord.Embed(title='Banned!',description=f'You were banned from **{guild}** for **{reason}**',color=0xff0000)
	msg_channel= discord.Embed(title='Sucess!',description=f'You banned {member.mention} for **{reason}**', color=0x00FF00)

	await ctx.send(embed=msg_channel)
	await member.send(embed=msg_member)
	await member.ban(reason=reason)

@ban.error

async def ban_error(ctx, error):

	with open("prefixes.json", "r") as f:
		prefixes = json.load(f)

	prefix = prefixes[str(ctx.guild.id)]

	if isinstance(error, commands.MissingRequiredArgument):
		embed1 = discord.Embed(title='Ban Command', description=f'**Description:** Bans a member from the current server \n**Cooldown:** 0 seconds\n**Usage:** {prefix}ban <member> (reason) \n**Examples:** \n{prefix}ban @Gamerkid Ad Spamming \n{prefix}ban @Gamerkid', color=0xFFA500)
		embed1.set_footer(text="Objects in <> are required and objects in () are optional")
	
		await ctx.send(embed=embed1)
		return

	if isinstance(error, commands.CommandOnCooldown):
		embed2 = discord.Embed(title='Command on Cooldown!',description=f'Command used: **{prefix}ban <member> (reason)** \n Cooldown: **3 seconds** \n \n Try again later!',color=0xff0000)
		embed2.set_footer(text=f'Want no cooldowns? Upgrade to Metro Plus! Run {prefix}upgrade')

		await ctx.send(embed=embed2)
		return

	if isinstance(error, commands.MissingPermissions):
		embed3 = discord.Embed(title='Missing Permission!',description=f'You do not have the permissions to run this command \n **Command ran:** {prefix}ban <member> (reason)',color=0xff0000)

		await ctx.send(embed=embed3)
		return




@client.command()
@commands.guild_only()
@commands.has_guild_permissions(ban_members=True)
async def unban(ctx, *, member):

	banned_users = await ctx.guild.bans()
	member_name, member_disc = member.split('#')

	for banned_entry in banned_users:
		user = banned_entry.user

		if(user.name, user.discriminator)==(member_name, member_disc):

			msg_channel = discord.Embed(title='Sucess!',description=f'You unbanned {member}',color=0x00FF00)

			await ctx.guild.unban(user)
			await ctx.send(embed=msg_channel)
			return

	msg_error = discord.Embed(title='Member Not Found!',description=f'**{member}** was not found! Please check for any spaces or errors',color=0xFFFF00)

	await ctx.send(embed=msg_error)

@unban.error
async def unban_error(ctx, error):

	with open("prefixes.json", "r") as f:
		prefixes = json.load(f)

	prefix = prefixes[str(ctx.guild.id)]

	if isinstance(error, commands.MissingRequiredArgument):
		embed1 = discord.Embed(title='Unban Command',description=f'**Description:** Unbans a member from the current server \n**Cooldown:** 0 seconds \n**Usage:** {prefix}unban <member> \n**Example:** \n{prefix}unban Gamerkid#1234', color=0xFFA500)
		embed1.set_footer(text="Objects in <> are required and objects in () are optional")

		await ctx.send(embed=embed1)
		return

	if isinstance(error, commands.CommandOnCooldown):
		embed2 = discord.Embed(title='Command on Cooldown!',description=f'Command used: **{prefix}unban <member> (reason)** \n Cooldown: **3 seconds** \n \n Try again later!',color=0xff0000)
		embed2.set_footer(text=f'Want no cooldowns? Upgrade to Metro Plus! Run {prefix}upgrade')

		await ctx.send(embed=embed2)
		return

	if isinstance(error, commands.MissingPermissions):
		embed3 = discord.Embed(title='Missing Permission!',description=f'You do not have the permissions to run this command \n **Command ran:** {prefix}unban <member> (reason)',color=0xff0000)

		await ctx.send(embed=embed3)
		return



@client.command()
@commands.guild_only()
@commands.has_guild_permissions(kick_members=True)
async def kick(ctx, user : discord.Member, *, reason=None):
	
	guild = ctx.guild

	msg_member = discord.Embed(title='Kicked!',description=f'You were kicked from **{guild}** for **{reason}**', color=0xff0000)
	msg_channel= discord.Embed(title='Sucess!',description=f'You kicked {member.mention} for **{reason}**', color=0x00FF00)

	await ctx.send(embed=msg_channel)
	await member.send(embed=msg_member)

	await member.kick(reason=reason)

@kick.error
async def kick_error(ctx, error):

	with open("prefixes.json", "r") as f:
		prefixes = json.load(f)

	prefix = prefixes[str(ctx.guild.id)]

	if isinstance(error, commands.MissingRequiredArgument):
		embed1 = discord.Embed(title='Kick Command', description=f'**Description:** Kicks a member from the current server \n**Cooldown:** 0 seconds \n**Usage:** {prefix}kick <member> (reason) \n**Example:** \n{prefix}kick @Gamerkid Stop Spamming \n{prefix}kick @Gamerkid', color=0xFFA500)
		embed1.set_footer(text="Objects in <> are required and objects in () are optional")
		
		await ctx.send(embed=embed1)
		return

	if isinstance(error, commands.CommandOnCooldown):
		embed2 = discord.Embed(title='Command on Cooldown!',description=f'Command used: **{prefix}kick <member> (reason)** \n Cooldown: **3 seconds** \n \n Try again later!',color=0xff0000)
		embed2.set_footer(text=f'Want no cooldowns? Upgrade to Metro Plus! Run {prefix}upgrade')

		await ctx.send(embed=embed2)
		return

	if isinstance(error, commands.MissingPermissions):
		embed3 = discord.Embed(title='Missing Permission!',description=f'You do not have the permissions to run this command \n **Command ran:** {prefix}kick <member> (reason)',color=0xff0000)

		await ctx.send(embed=embed3)
		return




@client.command(aliases=['lockdown','lockchannel','lockdownchannel'],pass_context=True)
@commands.guild_only()
@commands.has_guild_permissions(manage_channels=True)
async def lock(ctx, channel : discord.TextChannel):

	

	embed = discord.Embed(title='Locked!',description=f'You sucessfully locked {channel.mention}',color=0x00FF00)
	embed2= discord.Embed(title='Locked!',description=f'This channel was locked by {ctx.author.mention}',color=0xff0000)

	await channel.set_permissions(ctx.guild.default_role, send_messages=False)
	await channel.send(embed=embed2)
	await ctx.send(embed=embed)


@client.command(aliases=['unlockchannel'])
@commands.guild_only()
@commands.has_guild_permissions(manage_channels=True)
async def unlock(ctx, channel : discord.TextChannel):

	embed = discord.Embed(title='Unlocked!',description=f'You sucessfully unlocked {channel.mention}',color=0x00FF00)
	embed2= discord.Embed(title='Unlocked!',description=f'This channel was unlocked by {ctx.author.mention}',color=0x00FF00)

	await channel.set_permissions(ctx.guild.default_role, send_messages=True)
	await channel.send(embed=embed2)
	await ctx.send(embed=embed)




@lock.error

async def lock_error(ctx, error):

	channel = ctx.channel

	with open("prefixes.json", "r") as f:
		prefixes = json.load(f)

	prefix = prefixes[str(ctx.guild.id)]

	if isinstance(error, commands.MissingRequiredArgument):

		embed = discord.Embed(title='Locked!',description=f'You sucessfully locked {channel.mention}',color=0x00FF00)


		await channel.set_permissions(ctx.guild.default_role, send_messages=False)
		await ctx.send(embed=embed)
		return

	if isinstance(error, commands.CommandOnCooldown):

		embed2 = discord.Embed(title='Command on Cooldown!',description=f'Command used: **{prefix}lock (channel)** \n Cooldown: **2 seconds** \n \n Try again later!',color=0xff0000)
		embed2.set_footer(text=f'Want no cooldowns? Upgrade to Metro Plus! Run {prefix}upgrade')

		await ctx.send(embed=embed2)
		return

	if isinstance(error, commands.MissingPermissions):
		embed3 = discord.Embed(title='Missing Permission!',description=f'You do not have the permissions to run this command \n **Command ran:** {prefix}lock (channel)',color=0xff0000)

		await ctx.send(embed=embed3)


@unlock.error

async def unlock_error(ctx, error):

	channel = ctx.channel 

	with open("prefixes.json", "r") as f:
		prefixes = json.load(f)

	prefix = prefixes[str(ctx.guild.id)]

	if isinstance(error, commands.MissingRequiredArgument):

		embed = discord.Embed(title='Unlocked!',description=f'You sucessfully unlocked {channel.mention}',color=0x00FF00)


		await channel.set_permissions(ctx.guild.default_role, send_messages=True)
		await ctx.send(embed=embed)
		return

	if isinstance(error, commands.CommandOnCooldown):

		embed2 = discord.Embed(title='Command on Cooldown!',description=f'Command used: **{prefix}unlock (channel)** \n Cooldown: **2 seconds** \n \n Try again later!',color=0xff0000)
		embed2.set_footer(text=f'Want no cooldowns? Upgrade to Metro Plus! Run {prefix}upgrade')

		await ctx.send(embed=embed2)
		return

	if isinstance(error, commands.MissingPermissions):
		embed3 = discord.Embed(title='Missing Permission!',description=f'You do not have the permissions to run this command \n **Command ran:** {prefix}unlock (channel)',color=0xff0000)

		await ctx.send(embed=embed3)

@client.command(aliases=['purge','clean'])
@commands.guild_only()
@commands.has_guild_permissions(manage_messages=True)
async def clear(ctx, amount=0):

	with open("prefixes.json", "r") as f:
		prefixes = json.load(f)

	prefix = prefixes[str(ctx.guild.id)]

	message = ctx.message
	
	if amount >= 5001:
		embed = discord.Embed(title='Too many messages!',description='The maximum amount of messages I can delete is 5000! \nSince you have Metro Plus you have no cooldowns just run this command again to delete more messages',color=0xff0000)
		
		await ctx.send(embed=embed)
		return


	if amount >= 1:
		await ctx.channel.purge(limit=amount+1)
		return


@clear.error
async def clear_error(ctx, error):

	channel = ctx.channel 

	with open("prefixes.json", "r") as f:
		prefixes = json.load(f)

	prefix = prefixes[str(ctx.guild.id)]


	if isinstance(error, commands.CommandOnCooldown):

		embed2 = discord.Embed(title='Command on Cooldown!',description=f'Command used: **{prefix}clear <amount>** \n Cooldown: **2 seconds** \n \n Try again later!',color=0xff0000)
		embed2.set_footer(text=f'Want no cooldowns? Upgrade to Metro Plus! Run {prefix}upgrade')
		await ctx.send(embed=embed2)
		return


	if isinstance(error, commands.MissingPermissions):

		embed3 = discord.Embed(title='Missing Permission!',description=f'You do not have the permissions to run this command \n **Command ran:** {prefix}clear <amount>',color=0xff0000)

		await ctx.send(embed=embed3)
		return

	if isinstance(error, commands.MissingRequiredArgument):

		em = discord.Embed(title='Clear Messages Command', description=f'**Description:** Clears a set amount of messages \n**Cooldown:** 2 seconds\n**Aliases:** purge, clean\n**Usage:** {prefix}clear (amount) \n**Examples:** \n{prefix}clear 69 \n{prefix}clear 10 ', color=0xFFA500)
		em.set_footer(text="Objects in <> are required and objects in () are optional")

		await ctx.send(embed=em)
		return

	else:
		return error

	



	
@client.command(aliases=['setdelay','cooldown','delay'])
@commands.guild_only()
@commands.has_guild_permissions(manage_channels=True)
async def slowmode(ctx, seconds):

	em = discord.Embed(title='Changed Slowmode!',description=f'I successfully changed the slowmode to **{seconds} seconds**!',color=0xfffffd)

	await ctx.channel.edit(slowmode_delay=seconds)
	await ctx.send(embed=em)
	return


@slowmode.error
async def slowmode_error(ctx, error):

	channel = ctx.channel 

	with open("prefixes.json", "r") as f:
		prefixes = json.load(f)

	prefix = prefixes[str(ctx.guild.id)]


	if isinstance(error, commands.CommandOnCooldown):

		embed2 = discord.Embed(title='Command on Cooldown!',description=f'Command used: **{prefix}slowmode <seconds>** \n Cooldown: **3 seconds** \n \n Try again later!',color=0xff0000)
		embed2.set_footer(text=f'Want no cooldowns? Upgrade to Metro Plus! Run {prefix}upgrade')
		await ctx.send(embed=embed2)
		return


	if isinstance(error, commands.MissingPermissions):

		embed3 = discord.Embed(title='Missing Permission!',description=f'You do not have the permissions to run this command \n **Command ran:** {prefix}slowmode <seconds>',color=0xff0000)

		await ctx.send(embed=embed3)
		return

	if isinstance(error, commands.MissingRequiredArgument):

		em = discord.Embed(title='Clear Messages Command', description=f'**Description:** Sets the slowmode for the current channel \n**Cooldown:** 3 seconds\n**Aliases:** delay\n**Usage:** {prefix}slowmode <seconds> \n**Examples:** \n{prefix}slowmode 69 \n{prefix}slowmode 2 ', color=0xFFA500)
		em.set_footer(text="Objects in <> are required and objects in () are optional")

		await ctx.send(embed=em)
		return


        





	





















































@client.command(aliases=['8ball'])
@commands.guild_only()

async def _8ball(ctx, *, question):
  responses = [
  discord.Embed(title='It is certain.',color=0x00FF00),
  discord.Embed(title='It is decidedly so.',color=0x00FF00),
  discord.Embed(title='Without a doubt.',color=0x00FF00),
  discord.Embed(title='Yes - definitely.',color=0x00FF00),
  discord.Embed(title='You may rely on it.',color=0x00FF00),
  discord.Embed(title='Most likely.',color=0x00FF00),
  discord.Embed(title='Outlook good.',color=0x00FF00),
  discord.Embed(title='Yes.',color=0x00FF00),
  discord.Embed(title='Signs point to yes.',color=0x00FF00),
  discord.Embed(title='Reply hazy, try again.',color=0x00FF00),
  discord.Embed(title='Ask again later.',color=0x00FF00),
  discord.Embed(title='Better not tell you now.',color=0x00FF00),
  discord.Embed(title='Cannot predict now.',color=0x00FF00),
  discord.Embed(title='Concentrate and ask again.',color=0x00FF00),
  discord.Embed(title="Don't count on it.",color=0x00FF00),
  discord.Embed(title='My reply is no.',color=0x00FF00),
  discord.Embed(title='My sources say no.',color=0x00FF00),
  discord.Embed(title='Outlook not very good.',color=0x00FF00),
  discord.Embed(title='Very doubtful.',color=0x00FF00)
    ]
  responses = random.choice(responses)
  await ctx.send(f'Question: {question}\nAnswer:', embed=responses)

@_8ball.error

async def _8ball_error(ctx, error):

	with open("prefixes.json", "r") as f:
		prefixes = json.load(f)

	prefix = prefixes[str(ctx.guild.id)]

	if isinstance(error, commands.MissingRequiredArgument):
		em = discord.Embed(title= "8ball Command", description=f"**Description:** Gives you a random answer to your question! \n**Cooldown:**  0 seconds \n**Usage:** {prefix}8ball <question>", color=0xFFA500)
		em.set_footer(text="Objects in <> are required and objects in () are optional")

		await ctx.send(embed=em)
		return

	if isinstance(error, commands.CommandOnCooldown):
		embed2 = discord.Embed(title='Command on Cooldown!',description=f'Command used: **{prefix}8ball <question> ** \n Cooldown: **3 seconds** \n \n Try again later!',color=0xff0000)
		embed2.set_footer(text=f'Want no cooldowns? Upgrade to Metro Plus! Run {prefix}upgrade')

		await ctx.send(embed=embed2)
		return

	return



@client.command(aliases=['repeat'])
@commands.guild_only()
@commands.has_guild_permissions(manage_messages=True)
async def echo(ctx, *, message):

	await ctx.send(message)

@echo.error

async def echo_error(ctx, error):

	with open("prefixes.json", "r") as f:
		prefixes = json.load(f)

	prefix = prefixes[str(ctx.guild.id)]

	if isinstance(error, commands.MissingRequiredArgument):
		em = discord.Embed(title= "Echo/Repeat Command", description=f"**Description:** Repeats what you just said \n**Cooldown:**  0 seconds \n**Usage:** {prefix}echo <text>", color=0xFFA500)
		em.set_footer(text="Objects in <> are required and objects in () are optional")

		await ctx.send(embed=em)
		return

	if isinstance(error, commands.CommandOnCooldown):
		embed2 = discord.Embed(title='Command on Cooldown!',description=f'Command used: **{prefix}echo <text> ** \n Cooldown: **3 seconds** \n \n Try again later!',color=0xff0000)
		embed2.set_footer(text=f'Want no cooldowns? Upgrade to Metro Plus! Run {prefix}upgrade')

		await ctx.send(embed=embed2)
		return

	if isinstance(error, commands.MissingPermissions):
		embed3 = discord.Embed(title='Missing Permission!',description=f'You do not have the permissions to run this command \n **Command ran:** {prefix}echo <text>',color=0xff0000)
		await ctx.send(embed=embed3)
		return


@client.command()
@commands.guild_only()
@commands.has_guild_permissions(manage_messages=True)
async def embed(ctx, arg1, arg2):

	embed = discord.Embed(title=arg1, description=arg2, color=0xfffffd)
	await ctx.send(embed=embed)

@embed.error

async def embed_error(ctx, error):

	with open("prefixes.json", "r") as f:
		prefixes = json.load(f)

	prefix = prefixes[str(ctx.guild.id)]

	if isinstance(error, commands.MissingRequiredArgument):
		em = discord.Embed(title= "Embed Command", description=f'**Description:** Embeds a  message you want\n**Cooldown:**  0 seconds \n**Usage:** {prefix}embed <title> <text>\n**Examples:** \n{prefix}embed red "This is so cool!" "This is also so cool!" \n{prefix}embed green "Quick Embed" "Happy Birthday!"', color=0xFFA500)
		em.set_footer(text="Objects in <> are required and objects in () are optional. Make sure to put title and text in quotes if more than 1 word!")

		await ctx.send(embed=em)
		return

	if isinstance(error, commands.CommandOnCooldown):
		embed2 = discord.Embed(title='Command on Cooldown!',description=f'Command used: **{prefix}embed <title> <text> ** \n Cooldown: **3 seconds** \n \n Try again later!',color=0xff0000)
		embed2.set_footer(text=f'Want no cooldowns? Upgrade to Metro Plus! Run {prefix}upgrade')

		await ctx.send(embed=embed2)
		return

	if isinstance(error, commands.MissingPermissions):
		embed3 = discord.Embed(title='Missing Permission!',description=f'You do not have the permissions to run this command \n **Command ran:** {prefix}embed <title> <text>',color=0xff0000)
		await ctx.send(embed=embed3)
		return














































@client.command()
@commands.guild_only()
@commands.has_guild_permissions(manage_channels=True)

async def delete(ctx):

	em = discord.Embed(title="Confirmation", description="Are you sure you want to delete this channel? Reply with `delete` if you are sure.", color=0xff0000)

	def check(message):
		return message.author == ctx.author and message.channel == ctx.channel and message.content.lower() == "delete"

	await ctx.send(embed=em)
	await client.wait_for('message', check=check, timeout=60)
	await ctx.channel.delete()




@client.command(aliases=['newchannel','createchannel','create'])
@commands.guild_only()
@commands.has_guild_permissions(manage_channels=True)
async def new(ctx, name):
	
	channel = await ctx.guild.create_text_channel(f'{name}', category=None)

	em = discord.Embed(title='Channel Created!',description=f'I created a channel at {channel.mention}',color=0x00FF00)

	await ctx.send(embed=em)

@new.error
async def new_error(ctx, error):

	with open("prefixes.json", "r") as f:
		prefixes = json.load(f)

	prefix = prefixes[str(ctx.guild.id)]

	if isinstance(error, commands.MissingRequiredArgument):
		em = discord.Embed(title='New Channel Command', description=f'**Description:** Creates a new channel \n**Cooldown:** 0 seconds\n**Usage:** {prefix}new <channel-name>  \n**Examples:** \n{prefix}new general-chat \n{prefix}new bot-commands-2 ', color=0xFFA500)
		em.set_footer(text="Objects in <> are required and objects in () are optional")

		await ctx.send(embed=em)
		return

	if isinstance(error, commands.CommandOnCooldown):
		embed2 = discord.Embed(title='Command on Cooldown!',description=f'Command used: **{prefix}new <channel-name> ** \n Cooldown: **3 seconds** \n \n Try again later!',color=0xff0000)
		embed2.set_footer(text=f'Want no cooldowns? Upgrade to Metro Plus! Run {prefix}upgrade')

		await ctx.send(embed=embed2)
		return

	if isinstance(error, commands.MissingPermissions):
		embed3 = discord.Embed(title='Missing Permission!',description=f'You do not have the permissions to run this command \n **Command ran:** {prefix}new <channel-name> ',color=0xff0000)
		await ctx.send(embed=embed3)
		return



@client.command()
@commands.guild_only()
@commands.has_guild_permissions(manage_channels=True)
async def rename(ctx, name):

	channel = ctx.channel

	em = discord.Embed(title='Renamed Channel!',description=f'This channel is now renamed to {channel.mention}',color=0x00FF00)

	await channel.edit(name=name)
	await ctx.send(embed=em)


@rename.error
async def rename_error(ctx, error):

	with open("prefixes.json", "r") as f:
		prefixes = json.load(f)

	prefix = prefixes[str(ctx.guild.id)]

	if isinstance(error, commands.MissingRequiredArgument):
		em = discord.Embed(title='Rename Channel Command', description=f'**Description:** Renames the current channel \n**Cooldown:** 0 seconds\n**Usage:** {prefix}rename <new-channel-name> \n**Examples:** \n{prefix}rename general-chat \n{prefix}rename bot-commands ', color=0xFFA500)
		em.set_footer(text="Objects in <> are required and objects in () are optional")

		await ctx.send(embed=em)
		return

	if isinstance(error, commands.CommandOnCooldown):
		embed2 = discord.Embed(title='Command on Cooldown!',description=f'Command used: **{prefix}rename <new-channel-name>** \n Cooldown: **3 seconds** \n \n Try again later!',color=0xff0000)
		embed2.set_footer(text=f'Want no cooldowns? Upgrade to Metro Plus! Run {prefix}upgrade')

		await ctx.send(embed=embed2)
		return

	if isinstance(error, commands.MissingPermissions):
		embed3 = discord.Embed(title='Missing Permission!',description=f'You do not have the permissions to run this command \n **Command ran:** {prefix}rename <new-channel-name>',color=0xff0000)
		await ctx.send(embed=embed3)
		return
































@client.command(aliases=['disconnect', 'close', 'stopbot'])
@commands.is_owner()
async def logout(ctx):

	time = 5

	def check(message):
		return message.author == ctx.author and message.channel == ctx.channel and message.content.lower() == "yes"

	em = discord.Embed(title='Logout of Metro!',description='Are you sure you want to logout of Metro? Type ``yes`` to confirm.',color=0xff0000)

	pickle = discord.Embed(title='Sucessfully logged out of Metro!',description='The bot is currently displayed as online but all guilds the bot is in will not work.',color=0xfffffd)

	await ctx.send(embed=em)
	await client.wait_for('message', check=check, timeout=15)
	await asyncio.sleep(5)

	await ctx.send(embed=pickle)
	await client.logout()
	return





	



@logout.error
async def logout_error(ctx, error):
    """
    Whenever the logout command has an error this will be tripped.
    """
    if isinstance(error, commands.CheckFailure):
        await ctx.send("Hey! Only Metro delelopers can use this command! It's nice you found out how to use this command tho ;)")
    else:
        raise error









@client.command(aliases=['metroplus'])
@commands.guild_only()

async def upgrade(ctx):	

	upgrade = discord.Embed(title='Already Upgraded!',description='You already upgraded to Metro Plus!',color=0x00FF00)


	await ctx.send(embed=upgrade)





@client.command()
@commands.guild_only()
@commands.is_owner()
async def status(ctx, arg, arg2):

	w = discord.Embed(title='Status Changed!',description=f'You changed my status to **Watching {arg2}**',color=0x00FF00)

	p = discord.Embed(title='Status Changed!',description=f'You changed my status to **Playing {arg2}**',color=0x00FF00)

	l = discord.Embed(title='Status Changed!',description=f'You changed my status to **Listening to {arg2}**',color=0x00FF00)
	
	if arg == "w":
		await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=arg2))
		await ctx.send(embed=w)
		return


	if arg == "p":
		await client.change_presence(activity=discord.Game(name=arg2))
		await ctx.send(embed=p)
		return
		

	if arg == "l":
		await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="a song"))
		await ctx.send(embed=l)
		return

	return

@client.command()
@commands.guild_only()
@commands.is_owner()
async def reset(ctx):

	em = discord.Embed(title='Status Changed!',description='I changed my status back to **Watching =help | =upgrade**',color=0x00FF00)
	await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="=help | =upgrade"))

	await ctx.send(embed=em)





@client.event 
async def on_ready():
	
	await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="=help | =upgrade"))

	print('Bot is ready and online!')
	print("Bot running with:")
	print("Username: ", client.user.name)
	print("User ID: ", client.user.id)

	





client.run('Nzg4ODc4NDg0NjU0NjUzNDYw.X9p6Vw.TpsDK8oaXL3-X4Z90sA6eMuiqMc')