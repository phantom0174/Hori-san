from discord.ext import commands
from core.classes import Cog_Extension
import discord


class Event(Cog_Extension):
    @commands.Cog.listener()  # bot.event
    async def on_ready(self):
        print('---> I\'m online! <---')

    @commands.command()  # bot.command()
    async def ping(self, ctx):
        await ctx.send(f':stopwatch: {round(self.bot.latency * 1000)} (ms)')

    @commands.command()
    async def say_hi(self, ctx):
        await ctx.send("おはよう、宮村くん。")
      

def setup(bot):
    bot.add_cog(Event(bot))