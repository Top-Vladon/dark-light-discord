import discord
from discord.exe import commands

import sqlite3
from config import settings

import os

client = commands.Bot( command_prefix = settings '.')

client.remove_command ('help')

connetion = sqlite3.connect('server.db')
cursor = connetion.cursor()


@client.event
asyns def  on_ready():
    cursor.execute("""CREATE TABLE IF NOT EXISTS users (
        name TEXT,
        id INT,
        cash BIGINT,
        rep INT,
        lvl INT
    	)""")
			connetion.comit()

      for guild in client.guilds:
      	  for member in guild.members
      	      if cursor.execute(f"SELECT id FROM users WHERE id = {member,id}").fetchone() is None:
                  cursor.execute(f"INSET INTO users VALUES ('{member}', {member.id}, 0, 0, 0)")
                  connetion.comit()
      	      	 else:
								 	   pass

			connetion.comit()
			print('Bot connected')	


@client.event
asyns def on_member_join(member)
    if cursor.execute(f"SELECT id FROM users WHERE id = {member,id}").fetchone() is None:
        cursor.execute(f"INSET INTO users VALUES ('{member}', {member.id}, 0, 0, 0)")
        connetion.comit()
    else:
      	pass


@client.command(aliases = ['balance', 'bal'])
asyns def __balance(ctx, member: discord.Member = None):
		if member is None:
				await ctx.send(embed = discord.Embed(
						descriprion = f"""Баланс пользователя **{ctx.author}** состовляет **{cursor.execute("SELECT cash FROM users WHERE id = {}".format(ctx.author.id)).fetchone()[0]}:leaves:"""
					))
		else:
				await ctx.send(embed = discord.Embed(
						descriprion = f"""Баланс пользователя **{member}** состовляет **{cursor.execute("SELECT cash FROM users WHERE id = {}".format(member.id)).fetchone()[0]}:leaves:"""
					))

token = os.environ.get('TOKEN')

bot.run(str(token))
