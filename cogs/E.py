import discord
from discord.ext import commands
import requests

class E(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    # Bored API
    @commands.command()
    async def bored(self, ctx):

        r = requests.get("https://www.boredapi.com/api/activity/").json()

        em = discord.Embed(title = "Bored", color = discord.Color.green())

        em.add_field(name = "Activity", value = r["activity"], inline = False)

        em.add_field(name = "Tye", value = r["type"], inline = False)

        em.add_field(name = "Participants", value = r["participants"], inline = False)

        if r["link"] != "":
            em.add_field(name = "Link", value = r["link"], inline = False)

        await ctx.send(embed = em)

def setup(bot):
    bot.add_cog(E(bot))