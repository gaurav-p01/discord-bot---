import discord
from discord.ext import commands


class Hugs(commands.Cog):

    links = "https://tenor.com/view/anime-hug-sweet-love-gif-14246498 https://tenor.com/view/hug-anime-gif-15793126 https://tenor.com/view/hug-anime-gif-11074788 https://tenor.com/view/anime-cheeks-hugs-gif-14106856 https://tenor.com/view/sakura-quest-anime-animes-hug-hugging-gif-14721541 https://tenor.com/view/hugs-and-love-gif-19327081 https://tenor.com/view/anime-hug-sweet-anime-gif-13857539 https://tenor.com/view/hug-anime-gif-4898650 https://tenor.com/view/anime-couple-hug-cute-cuddle-gif-14898682 https://tenor.com/view/chiya-urara-meirochou-anime-saku-gif-8995974 https://tenor.com/view/hug-anime-love-sweet-tight-hug-gif-7324587 https://tenor.com/view/anime-anime-love-hug-love-sweet-gif-16131468 https://tenor.com/view/anime-hug-manga-cuddle-japan-gif-10522729 https://tenor.com/view/hug-anime-hug-cry-happy-anime-happy-gif-19679116 https://tenor.com/view/hug-couple-love-gif-14584871 https://tenor.com/view/anime-hug-love-gif-15900664 https://tenor.com/view/my-little-monster-anime-hug-love-gif-13221416 https://tenor.com/view/anime-hug-cuddle-love-care-gif-17265727 https://tenor.com/view/crying-anime-kyoukai-no-kanata-hug-hugging-anime-hug-tight-tight-hug-gif-17880570 https://tenor.com/view/kiss-anime-couple-shocked-blush-gif-17907349 https://tenor.com/view/kakegurui-yumeko-jabami-hug-anime-anime-hug-gif-17991101 https://tenor.com/view/abra%C3%A7o-hug-miss-you-gif-14903944 https://tenor.com/view/kiss-anime-cute-couples-gif-17252595 https://tenor.com/view/hug-anime-sweet-couple-gif-12668480 https://tenor.com/view/hug-anime-care-comfort-understanding-gif-15793129 https://tenor.com/view/teria-wang-kishuku-gakkou-no-juliet-hug-anime-gif-16509980 https://tenor.com/view/anime-hug-love-smile-gif-15942846 https://tenor.com/view/anime-hug-gif-13221036 https://tenor.com/view/anime-acchi-kocchi-anime-couple-neko-anime-rain-gif-16085531 https://tenor.com/view/cuddle-hug-anime-bunny-costumes-happy-gif-17956092 https://tenor.com/view/a-whisker-away-hug-love-anime-embrace-gif-17694740 https://tenor.com/view/hug-anime-clingy-gif-7552075 https://tenor.com/view/hug-anime-cartoon-japanese-fall-gif-7552093 https://tenor.com/view/toilet-bound-hanakokun-anime-anime-hug-gif-16831471 https://tenor.com/view/horimiya-izumi-miyamura-hori-kyoko-couple-hug-gif-14539121 https://tenor.com/view/anime-anime-hug-sweet-happy-in-love-gif-16103131 https://tenor.com/view/anime-bed-bedtime-sleep-night-gif-12375072 https://tenor.com/view/anime-hug-hearts-hug-bff-gif-13857541 https://tenor.com/view/hug-cat-cute-aww-anime-gif-9200935 https://tenor.com/view/anime-hug-love-hug-gif-13925386 https://tenor.com/view/blushing-anime-girl-couple-hug-gif-19423749 https://tenor.com/view/hug-anime-sweet-gif-10195705 https://tenor.com/view/anime-cute-girl-kotori-itsuka-date-a-live-gif-17438857 https://tenor.com/view/hug-k-on-anime-cuddle-gif-16095203 https://tenor.com/view/hug-anime-gif-19674705 https://tenor.com/view/loli-dragon-anime-cute-hug-gif-9920978 https://tenor.com/view/hug-anime-hug-anime-cute-uwu-gif-17264448 https://tenor.com/view/hug-love-kanna-cute-kanna-kamui-gif-17266781 https://tenor.com/view/anime-hug-cuddle-gif-19768597"


    def __init__(self, bot):
        self.bot = bot
    
    # Hug spam
    @commands.command()
    async def hugspam(self, ctx, user : discord.User):
        await ctx.send("done")
        for i in self.links.split(" "):
            await user.send(i)
                   

def setup(bot):
    bot.add_cog(Hugs(bot))