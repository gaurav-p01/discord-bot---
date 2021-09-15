import discord
from discord.ext import commands


class Basic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    

    # on ready event
    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.change_presence(status=discord.Status.online,
                              activity=discord.Game("with my pp"))
        print('Bot is ready')
    

    # ping command
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"{round(self.bot.latency*1000)}ms")


    # say command
    @commands.command()
    async def say(self, ctx, *, message):
        await ctx.send(message)
    # error handling
    @say.error
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("try .say **message to send**")
        else:
            print(error)


    # sample embed command
    @commands.command()
    async def embed(self, ctx): 
        em = discord.Embed(title = "Sample Embed", color = discord.Color.green(), url = "https://www.google.com")
        em.set_thumbnail(url = "https://img-9gag-fun.9cache.com/photo/a1oGrKY_460s.jpg" )
        em.set_image(url = "https://img.wattpad.com/cover/149189757-352-k950686.jpg")
        em.set_footer(icon_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRSBEL7SbdrnB8GOh1-24GYicD6u6INzKWVkQ&usqp=CAU", text = "Makoto Nijima")
        em.add_field(name = "Field Name", value = "Field Value")
        await ctx.send(embed = em)


def setup(bot):
    bot.add_cog(Basic(bot))