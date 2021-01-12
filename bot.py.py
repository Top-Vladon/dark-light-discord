import discord
from discord.ext import commands
from discord.ext.commands import Bot

Bot = commands.Bot(command_prefix='.')

@Bot.event
async def on_ready():
    print('Бот онлайн!')

@Bot.command(pass_context = True)
async def hello(ctx):
    await ctx.send("Hello!!!")

Bot.run("Nzk3ODU2NjY5Nzk4MjM2MTYx.X_sj7Q.zMj7yTXSnkVxX-bdzPeob8-T0-c")
