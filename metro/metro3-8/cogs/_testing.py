	@commands.command(pass_context=True, aliases=['ki','getout'])
	@commands.guild_only()
	@commands.cooldown(rate=1, per=3, type=commands.BucketType.user)
	@commands.has_guild_permissions(kick_members=True)
	async def kick(self, ctx, member: discord.Member, *, reason=None):

		if member.guild_permissions.manage_guild or member.guild_permissions.administrator or member.guild_permissions.kick_members or member.guild_permissions.ban_members:
			await ctx.send('This person is a mod/admin I cannot kick them!')
			return

		memberMSG  = discord.Embed(title='Kicked!',description=f'You were kicked from **{ctx.guild}**! \n**Reason:** {reason}',color=0xE74C3C, timestamp=ctx.message.created_at)
		memberMSG.set_footer(text=f"©Metro 2020 | {self.bot.user.name}")
		channelMSG = discord.Embed(title='Sucess!',description=f'I sucessfully kicked {member.mention} for you! \n**Reason:** {reason}',color=0x2ECC71, timestamp=ctx.message.created_at)
		channelMSG.set_footer(text=f"©Metro 2020 | {self.bot.user.name}")

		channelMSG2 = discord.Embed(title='Sucess!',description=f'I sucessfully kicked {member.mention} for you! \n**Reason:** {reason} \n**Note:** I could not DM them but they are indeed kicked',color=0x2ECC71, timestamp=ctx.message.created_at)
		channelMSG2.set_footer(text=f"©Metro 2020 | {self.bot.user.name}")

		try:
			await member.send(embed=memberMSG)
			await member.kick(reason=reason)

			await ctx.send(embed=channelMSG)

		except:
			await member.kick(reason=reason)

			await ctx.send(embed=channelMSG2)

	@kick.error
	async def kick_error(self, ctx, error):

		data = await self.bot.config.get_by_id(ctx.message.guild.id)
		prefix = data["prefix"]

		if isinstance(error, commands.MissingRequiredArgument):

			description = discord.Embed(title='Kick Command',description=f'**Aliases:** ki, getout \n**Cooldown:** 3 seconds \n**Description:** Kicks a member from the current guild \n**Usage:** {prefix}kick <member> (reason) \n**Examples:** \n{prefix}kick @dartmern Spamming and raiding server \n{prefix}kick 525843819850104842 \n{prefix}kick dartmern spamming memes in bot commands',color=0xE67E22)
			description.set_footer(text='Objects in <> are required and objects in () are optional')

			await ctx.send(embed=description)


		if isinstance(error, commands.CommandOnCooldown):
			m, s = divmod(error.retry_after, 60)
			h, m = divmod(m, 60)

			if int(h) == 0 and int(m) == 0: 

				em = discord.Embed(title='Command on Cooldown!',description=f'This command is on cooldown! Please try again in {int(s)} second(s)!',color=0xE74C3C)


				await ctx.send(f'{ctx.author.mention}',embed=em)

		if isinstance(error, commands.MissingPermissions):

			e = discord.Embed(title='Missing Permissions!',description=f'You do not have the ``Manage Messages`` permission to use this command',color=0xE74C3C,timestamp=ctx.message.created_at)
			e.set_footer(icon_url=ctx.author.avatar_url, text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}')
			await ctx.send(f"{ctx.author.mention}",embed=e)

		else:
			raise error

	@commands.command(pass_context=True, aliases=['ba'])
	@commands.guild_only()
	@commands.cooldown(rate=1, per=3, type=commands.BucketType.user)
	@commands.has_guild_permissions(ban_members=True)
	async def ban(self, ctx, member : discord.Member, *, reason=None):
		
		if member.guild_permissions.manage_guild or member.guild_permissions.administrator or member.guild_permissions.ban_members:
			await ctx.send('This person is a mod/admin I cannot kick them!')
			return	

		memberMSG = discord.Embed(title='Banned!',description=f'You were banned from **{ctx.guild}**! \n**Reason:** {reason}',color=0xE74C3C, timestamp=ctx.message.created_at)
		memberMSG.set_footer(text=f"©Metro 2020 | {self.bot.user.name}")

		channelMSG = discord.Embed(title='Sucess!',description=f'I sucessfully banned {member.mention} for you! \n**Reason:** {reason}',color=0x2ECC71, timestamp=ctx.message.created_at)
		channelMSG.set_footer(text=f"©Metro 2020 | {self.bot.user.name}")

		channelMSG2 = discord.Embed(title='Sucess!',description=f"I sucessfully banned {member.mention} for you! \n**Reason:** {reason} \n**Note:** I couldn't DM them but they are indeed banned",color=0x2ECC71, timestamp=ctx.message.created_at)
		channelMSG2.set_footer(text=f"©Metro 2020 | {self.bot.user.name}")

		try:
			await member.send(embed=memberMSG)
			await member.ban(reason=reason)

			await ctx.send(embed=channelMSG)

		except:
			await member.ban(reason=reason)

			await ctx.send(embed=channelMSG2)

	@ban.error
	async def ban_error(self, ctx, error):

		data = await self.bot.config.get_by_id(ctx.message.guild.id)
		prefix = data["prefix"]

		if isinstance(error, commands.MissingRequiredArgument):

			description = discord.Embed(title='Ban Command',description=f'**Aliases:** ba \n**Cooldown:** 3 seconds \n**Description:** Ban a member from the current guild \n**Usage:** {prefix}ban <member> (reason) \n**Examples:** \n{prefix}ban @dartmern Spamming and raiding server \n{prefix}ban 525843819850104842 \n{prefix}ban dartmern spamming memes in bot commands',color=0xE67E22)
			description.set_footer(text='Objects in <> are required and objects in () are optional')

			await ctx.send(embed=description)

		if isinstance(error, commands.CommandOnCooldown):
			m, s = divmod(error.retry_after, 60)
			h, m = divmod(m, 60)

			if int(h) == 0 and int(m) == 0: 

				em = discord.Embed(title='Command on Cooldown!',description=f'This command is on cooldown! Please try again in {int(s)} second(s)!',color=0xE74C3C)


				await ctx.send(f'{ctx.author.mention}',embed=em)

		if isinstance(error, commands.MissingPermissions):

			e = discord.Embed(title='Missing Permissions!',description=f'You do not have the ``Manage Messages`` permission to use this command',color=0xE74C3C,timestamp=ctx.message.created_at)
			e.set_footer(icon_url=ctx.author.avatar_url, text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}')
			await ctx.send(f"{ctx.author.mention}",embed=e)

		else:
			raise error

	@commands.command(aliases=['repeat','repeatthis','copyme'])
	@commands.cooldown(rate=1, per=3, type=commands.BucketType.user)
	@commands.has_guild_permissions(manage_messages=True) 
	async def echo(self, ctx, *, message):

		await ctx.message.delete()
		await ctx.send(message)

	@echo.error
	async def echo_error(self, ctx, error):

		data = await self.bot.config.get_by_id(ctx.message.guild.id)
		prefix = data["prefix"]

		if isinstance(error, commands.MissingRequiredArgument):

			description = discord.Embed(
            title='Echo Command',
            description=f'**Aliases:** repeat, repeatthis, copyme \n**Cooldown:** 3 seconds \n**Description:** Repeats any message you want \n**Usage:** {prefix}echo <message> \n**Examples:** \n{prefix}echo I am an idiot bot \n{prefix}echo Echo command is cool!',
            color=0xE67E22)

			description.set_footer(text='Objects in <> are required and objects in () are optional')

			await ctx.send(embed=description)

		if isinstance(error, commands.CommandOnCooldown):
			m, s = divmod(error.retry_after, 60)
			h, m = divmod(m, 60)

			if int(h) == 0 and int(m) == 0: 

				em = discord.Embed(title='Command on Cooldown!',description=f'This command is on cooldown! Please try again in {int(s)} second(s)!',color=0xE74C3C)


				await ctx.send(f'{ctx.author.mention}',embed=em)

		if isinstance(error, commands.MissingPermissions):

			e = discord.Embed(title='Missing Permissions!',description=f'You do not have the ``Manage Messages`` permission to use this command',color=0xE74C3C,timestamp=ctx.message.created_at)
			e.set_footer(icon_url=ctx.author.avatar_url, text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}')
			await ctx.send(f"{ctx.author.mention}",embed=e)

		else:
			raise error


	@commands.command(aliases=['clear', 'clearmessages'])
	@commands.guild_only()
	@commands.has_guild_permissions(manage_messages=True)
	async def purge(self, ctx, amount=0):

			if amount >= 1001:
				embed = discord.Embed(title='Error!',description=f'Too many messages! 1000 messages max - ({amount}/1000)',color=0xE74C3C)
				embed.set_footer(text='This message will delete in 3 seconds')
				
				message = await ctx.send(f'{ctx.author.mention}',embed=embed)

				await asyncio.sleep(3)
				await message.delete()

				return

			if amount >= 1:
				perfect = discord.Embed(title='Sucess!',description=f'I sucessfully deleted/purged {amount} message(s)',color=0x2ECC71)
				perfect.set_footer(text='This message will delete in 3 seconds')

				await ctx.channel.purge(limit=amount+1)

				message2 = await ctx.send(embed=perfect)

				await asyncio.sleep(3)
				await message2.delete()
				return

			else:
				data = await self.bot.config.get_by_id(ctx.message.guild.id)
				prefix = data["prefix"]

				description = discord.Embed(title='Purge Command',description=f'**Aliases:** clear, clearmessages \n**Cooldown:** 3 seconds \n**Description:** Deletes a set amount of messages \n**Usage:** {prefix}purge <amount> \n**Examples:** \n{prefix}purge 100 \n{prefix}clear 10 \n{prefix}clear 2',color=0xE67E22)
				description.set_footer(text='Objects in <> are required and objects in () are optional')

				await ctx.send(embed=description)












	@commands.command(pass_context=True,aliases=['silence', 'shutup', 'mu'])
	@commands.guild_only()
	@commands.has_guild_permissions(mute_members=True)	
	@commands.cooldown(rate=1, per=2, type=commands.BucketType.user)
	async def mute(self, ctx, member: discord.Member, time, *,reason=None):

		data = cogs._json.read_json('prefixes')
		prefix = data[str(ctx.message.guild.id)]

		member = member
		guild=ctx.guild

		role1 = discord.utils.get(member.guild.roles, name = "▼Muted▼")
		mutedRole = discord.utils.get(guild.roles, name="▼Muted▼")

		
		alr_muted = discord.Embed(title='User already Muted!',description=f'The user is already muted! Use ``{prefix}unmute <member>`` to unmute them',color=0xFFA500)

		error = discord.Embed(title='Error!',description='This member is a **mod/admin.** I cannot mute them.',color=0xFFA500)

		do_not = discord.Embed(title='Created Muted Role!',description='Please do **NOT** change the name of the Muted role I created or delete it',color=0xFFA500)

		timed_dm_yes_channel =  discord.Embed(title='Sucess!',description=f'You muted {member.mention} \n\n **Time:** {time}  \n**Reason:** {reason} \n**Note:** I could not DM them but they are indeed Muted', color=0x00FF00)
		
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

			for channel in guild.channels:
				await channel.set_permissions(mutedRole, speak=False, send_messages=False)
				
		await member.add_roles(mutedRole, reason=reason)

		after_mute	= discord.Embed(title='Unmuted!',description=f'You were unmuted in **{guild}** because your mute ended',color=0x00FF00)

		for channel in guild.channels:
			await channel.set_permissions(mutedRole, speak=False, send_messages=False)



		if time[-1].lower() == "h":

			msg_member = discord.Embed(title='Muted!',description=f'You were muted in **{guild}**! \n **Time:** {time}  \n**Reason:** {reason}', color=0xff0000)
			msg_channel= discord.Embed(title='Sucess!',description=f'You muted {member.mention} \n\n **Time:** {time}  \n**Reason:** {reason}', color=0x00FF00)
			msg_channel.set_footer(text=f'Use {prefix}unmute <member> to unmute someone')

			try:
				await member.send(embed=msg_member)
				await ctx.send(embed=msg_channel)
				
				await asyncio.sleep(int(time[:-1]) * 3600)
				await member.remove_roles(mutedRole)
				await member.send(embed=after_mute)
				return

			
			except:
				await ctx.send(embed=timed_dm_yes_channel)
				await asyncio.sleep(int(time[:-1]) * 3600)
				await member.remove_roles(mutedRole)
				return


		if time[-1].lower() == "m":
			msg_member = discord.Embed(title='Muted!',description=f'You were muted in **{guild}**! \n **Time:** {time}  \n**Reason:** {reason}', color=0xff0000)
			msg_channel= discord.Embed(title='Sucess!',description=f'You muted {member.mention} \n\n **Time:** {time} \n**Reason:** {reason}', color=0x00FF00)
			msg_channel.set_footer(text=f'Use {prefix}unmute <member> to unmute someone')

			try:
				await member.send(embed=msg_member)
				await ctx.send(embed=msg_channel)
				
				await asyncio.sleep(int(time[:-1]) * 60)
				await member.remove_roles(mutedRole)
				await member.send(embed=after_mute)
				return

			
			except:
				await ctx.send(embed=timed_dm_yes_channel) 
				await asyncio.sleep(int(time[:-1]) * 60)
				await member.remove_roles(mutedRole)
				return

		if time[-1].lower() == "d":
			msg_member = discord.Embed(title='Muted!',description=f'You were muted in **{guild}**! \n **Time:** {time}  \n**Reason:** {reason}', color=0xff0000)
			msg_channel= discord.Embed(title='Sucess!',description=f'You muted {member.mention} \n\n **Time:** {time} \n**Reason:** {reason}', color=0x00FF00)
			msg_channel.set_footer(text=f'Use {prefix}unmute <member> to unmute someone')

			try:
				await member.send(embed=msg_member)
				await ctx.send(embed=msg_channel)
				
				await asyncio.sleep(int(time[:-1]) * 86400)
				await member.remove_roles(mutedRole)
				await member.send(embed=after_mute)
				return

			
			except:
				await ctx.send(embed=timed_dm_yes_channel) 
				await asyncio.sleep(int(time[:-1]) * 86400)
				await member.remove_roles(mutedRole)
				return

		if time[-1].lower() == "s":
			msg_member = discord.Embed(title='Muted!',description=f'You were muted in **{guild}**! \n **Time:** {time} \n**Reason:** {reason}', color=0xff0000)
			msg_channel= discord.Embed(title='Sucess!',description=f'You muted {member.mention} \n\n **Time:** {time} \n**Reason:** {reason}', color=0x00FF00)
			msg_channel.set_footer(text=f'Use {prefix}unmute <member> to unmute someone')

			try:
				await member.send(embed=msg_member)
				await ctx.send(embed=msg_channel)
				
				await asyncio.sleep(int(time[:-1]) * 1)
				await member.remove_roles(mutedRole)
				await member.send(embed=after_mute)
				return

			
			except:
				await ctx.send(embed=timed_dm_yes_channel) 
				await asyncio.sleep(int(time[:-1]) * 1)
				await member.remove_roles(mutedRole)
				return


		msg_member = discord.Embed(title='Muted!',description=f"You were muted in **{guild}**! \n**Time:** None (the person who muted you didn't specify a time) \n**Reason:** {reason}", color=0xff0000)
		msg_channel= discord.Embed(title='Sucess!',description=f'You muted {member.mention}! \n\n**Time:** None (member is muted until someone unmutes him/her) \n**Reason:** {reason}', color=0x00FF00)

		msg_channel2= discord.Embed(title='Sucess!',description=f'You muted {member.mention}! \n\n**Time:** None (member is muted until someone unmutes him/her) \n**Reason:** {reason} \n**Note:** I could not DM them but they are indeed Muted', color=0x00FF00)

		try:
			await member.send(embed=msg_member)
			await ctx.send(embed=msg_channel)
			return

		except:
			await ctx.send(embed=msg_channel2)


	@mute.error
	async def mute_error(self, ctx, error):

		data = await self.bot.config.get_by_id(ctx.message.guild.id)
		prefix = data["prefix"]

		if isinstance(error, commands.MissingRequiredArgument):
			e = discord.Embed(title='Mute Command',description=f'**Aliases:** shutup, silence, mu \n**Cooldown:** 3 seconds \n**Description:** Prevents a member from talking \n**Usage:** {prefix}mute <member> (time) (reason) \n**Examples:** \n{prefix}mute @dartmern 10m Spamming \n{prefix}mute dartmern 1d breaking rule 4 \n{prefix}mute 525843819850104842 dm advertising',color=0xE67E22)
			e.set_footer(text='Objects in <> are required and objects in () are optional')
			await ctx.send(embed=e)

		if isinstance(error, commands.CommandOnCooldown):
			m, s = divmod(error.retry_after, 60)
			h, m = divmod(m, 60)

			if int(h) == 0 and int(m) == 0: 

				em = discord.Embed(title='Command on Cooldown!',description=f'This command is on cooldown! Please try again in {int(s)} second(s)!',color=0xE74C3C)


				await ctx.send(f'{ctx.author.mention}',embed=em)

		if isinstance(error, commands.MissingPermissions):

			e = discord.Embed(title='Missing Permissions!',description=f'You do not have the ``Manage Messages`` permission to use this command',color=0xE74C3C,timestamp=ctx.message.created_at)
			e.set_footer(icon_url=ctx.author.avatar_url, text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}')
			await ctx.send(f"{ctx.author.mention}",embed=e)

		else:
			raise error