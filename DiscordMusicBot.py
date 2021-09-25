import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='/')

@bot.command()
async def play2(ctx):
    await ctx.send('Estas escuchando:')()

print(' Bot se encendio')
bot.run("BotKey")