import discord
from discord.ext import commands
import requests

class Waifu(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    waifu = ['waifu', 'neko', 'shinobu', 'megumin', 'bully', 'cuddle', 'cry', 'hug', 'awoo', 'kiss', 'lick', 'pat', 'smug', 'bonk', 'yeet', 'blush', 'smile', 'wave', 'highfive', 'handhold', 'nom', 'bite', 'glomp', 'slap', 'kill', 'kick', 'happy', 'wink', 'poke', 'dance', 'cringe']

    @commands.command()
    async def waifulist(self, ctx):
        
        em = discord.Embed(title = "Waifu list", color = discord.Color.green()) 

        em.add_field(name = "Categories", value = "\n".join(self.waifu), inline = False)
    
        await ctx.send(embed = em)


    @commands.command()
    async def waifudm(self, ctx, user : discord.User, message, number):
        if message.lower() in self.waifu:
            if number.isdigit():
                for i in range (int(number)):
                    r = requests.get(f"https://api.waifu.pics/sfw/{message.lower()}").json()
                    em = discord.Embed()
                    em.set_image(url = r["url"])
                    await user.send(embed = em)
            else :
                await ctx.send("Invalid number")
        else :
            await ctx.send("Invalid waifu category")
        await ctx.send("Done")    

def setup(bot):
    bot.add_cog(Waifu(bot))