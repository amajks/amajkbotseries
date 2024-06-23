# How to make a discord bot

# Importing Discord
import discord
from discord.ext import commands

# Making Bot Prefix
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

# Making the bot go online
@bot.event
async def on_ready():
    print('Bot is online and ready to use.')

# Making a bot command
@bot.command()
async def ping(ctx):
    await ctx.send(f'Client Latency: `{round(bot.latency * 1000)}ms.`')

# Making the code run
bot.run('insert bot token here')
