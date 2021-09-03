from discord.ext import commands
from variables import TOKEN


#import all of the cogs
from music_cog import music_cog
from pokemon_cog import pokemon_cog
from meme_cog import meme_cog

bot = commands.Bot(command_prefix='?')

#register the class with the bot
bot.add_cog(music_cog(bot))
bot.add_cog(pokemon_cog(bot))
bot.add_cog(meme_cog(bot))

#start the bot with our token
bot.run(TOKEN)
