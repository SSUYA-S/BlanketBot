import discord, asyncio, os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv(verbose=True)
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

game = discord.Game("Priamry Bot")
bot = commands.Bot(command_prefix='!', status=discord.Status.online, activity=game)

bot.run(DISCORD_TOKEN)