import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print('Bot is running.')
    await bot.change_presence(status=discord.Status.dnd, activity=discord.Game('Subscribe to amajkcodes!'))

# Making the bot go online
bot.run('insert token here')
