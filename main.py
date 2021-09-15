from discord.ext import commands
from webserver import keep_alive
import os
import discord


bot = commands.Bot(command_prefix='.')


@bot.command()
async def load(ctx, extension):
    if ctx.author.id == 683289301290844165:
        bot.load_extension(f"cogs.{extension}")
        await ctx.send(f"{extension} loaded")
    else :
        await ctx.send("You do not have permission to use this")

@bot.command()
async def unload(ctx, extension):
    if ctx.author.id == 683289301290844165:
        bot.unload_extension(f"cogs.{extension}")
        await ctx.send(f"{extension} unloaded")
    else :
        await ctx.send("You do not have permission to use this")


@bot.command()
async def reload(ctx, extension):
    if ctx.author.id == 683289301290844165:
        bot.unload_extension(f"cogs.{extension}")
        bot.load_extension(f"cogs.{extension}")
        await ctx.send(f"{extension} reloaded")
    else :
        await ctx.send("You do not have permission to use this")

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")


keep_alive()

TOKEN = os.environ.get("DISCORD_BOT_SECRET")
bot.run(TOKEN)
