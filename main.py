from discord.ext import commands
import discord
import os
import keep_alive

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='+', intents=intents)

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

keep_alive.keep_alive()

bot.run(os.environ.get("TOKEN"))