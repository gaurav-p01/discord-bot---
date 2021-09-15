import discord
from discord.ext import commands
import random


class StupidGames(commands.Cog):
    GAMES = ["guess"]


    def __init__(self, bot):
        self.bot = bot


    # gamelist
    @commands.command()
    async def gamelist(self, ctx):
        em = discord.Embed(title = "Game List", color = discord.Color.green())
        em.add_field(name = "Games", value = "\n".join([str(_) for _ in self.GAMES]))
        await ctx.send(embed = em)


    # guess the number
    @commands.command()
    async def guess(self, ctx, message):
        if message == "start":
            await ctx.send("""I have chosen a number between 1 and 10 try to guess it
            \nType .guess *number* to guess""")
        elif message.isdigit():
            mynum = random.randint(1, 10)
            if int(message) == mynum:
                await ctx.send("Thats the number I chose :sparkles:")
            else:
                await ctx.send("Thats not the number I chose :turtle:")
        else:
            await ctx.send("try .guess *number*")
    # error handling
    @guess.error
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("try .guess **number**")
        else:
            print(error)


def setup(bot):
    bot.add_cog(StupidGames(bot))
