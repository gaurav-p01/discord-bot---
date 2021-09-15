import discord
from discord.ext import commands
import requests


class Waifu(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    WAIFU_CATEGORIES = ['waifu', 'neko', 'shinobu', 'megumin', 'bully', 'cuddle', 'cry', 'hug', 'awoo', 'kiss', 'lick', 'pat', 'smug', 'bonk', 'yeet', 'blush', 'smile', 'wave', 'highfive', 'handhold', 'nom', 'bite', 'glomp', 'slap', 'kill', 'kick', 'happy', 'wink', 'poke', 'dance', 'cringe']


    # waifu list command
    @commands.command()
    async def waifulist(self, ctx):
        em = discord.Embed(title = "Waifu list", color = discord.Color.green()) 
        em.add_field(name = "Categories", value = "\n".join(self.WAIFU_CATEGORIES), inline = False)
        await ctx.send(embed = em)


    # waifu dm command
    @commands.command()
    async def waifudm(self, ctx, user : discord.User, message : None, number : None):
        await ctx.send("Done") 
        if message == None:
            message = "waifu"
        if number == None:
            number = 1
        if message.lower() in self.WAIFU_CATEGORY:
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
    # error handling
    @waifudm.error
    async def waifudm_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("try .waifudm **mention_user** **waifu_category** **number**")
        else:
            await ctx.send("Invalid input")


def setup(bot):
    bot.add_cog(Waifu(bot))