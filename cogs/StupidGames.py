import discord
from discord.ext import commands
import random


class StupidGames(commands.Cog):
    GAMES = ["guess"]

    def __init__(self, bot):
        self.bot = bot

    # Gamelist
    @commands.command()
    async def gamelist(self, ctx):
        await ctx.send(" ".join([str(_) for _ in self.GAMES]) +
                       "\n\nType **.gamename start** to start a game")

    # Guess the number
    @commands.command()
    async def guess(self, ctx, message):
        if message == "start":
            await ctx.send(
                """I have chosen a number between 1 and 10 try to guess it
            \nType .guess *number* to guess""")
        elif message.isdigit():
            mynum = random.randint(1, 10)
            if int(message) == mynum:
                await ctx.send("Thats the number I chose :sparkles:")
            else:
                await ctx.send("Thats not the number I chose :turtle:")
        else:
            await ctx.send("Invalid input")


def setup(bot):
    bot.add_cog(StupidGames(bot))
