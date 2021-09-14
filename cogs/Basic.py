import discord
from discord.ext import commands


class Basic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.change_presence(status=discord.Status.online,
                              activity=discord.Game("with my pp"))
        print('Bot is ready')
    
    # Commands
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"{round(self.bot.latency*1000)}ms")

    @commands.command()
    async def say(self, ctx, *, message):
        await ctx.send(message)

    @commands.command()
    async def embed(self, ctx):
        em = discord.Embed(title = "Sample Embed", color = discord.Color.green())
        em.add_field(name = "Field Name", value = "Field Value")
        await ctx.send(embed = em)


def setup(bot):
    bot.add_cog(Basic(bot))