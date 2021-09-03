import discord
from discord.ext import commands

class meme_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="agiv", help="Exclusive Garrett and Akiv dance meme")
    async def agiv(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/750670860951486536/882534813020590090/ezgif-7-2747816f261f.gif")
