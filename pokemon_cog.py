import discord, shutil, requests, random
from discord.ext import commands

class pokemon_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.TYPE = {'normal': 1, 'fighting': 2, 'flying': 3, 'poison': 4, 'ground': 5, 'rock': 6, 'bug': 7, 'ghost': 8, 'steel': 9, 'fire': 10, 'water': 11, 'grass': 12, 'electric': 13, 'psychic': 14, 'ice': 15, 'dragon': 16, 'dark': 17, 'fairy': 18}

    def get_sprite(self,pokemon):
        ''' Get Pokemon sprite by name:str or id:int '''
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}")
        pokemon_name = response.json()['name']
        return response.json()['sprites']['front_default']

    @commands.command(name="pokemon", help="Returns a random pokemon sprite.")
    async def pokemon(self, ctx, *args):
        if len(args)==0:
            # Get a random pokemon if the type was not specified
            random_number = random.randint(1, 898)
            img_url = self.get_sprite(random_number)
            await ctx.send(img_url)
        if len(args)==1:
            # Random by Type
            type=args[0].lower()
            try:
                type_id=self.TYPE[type]
            except Exception as e:
                await ctx.send(f'Invalid Type. Valid types are {list(self.TYPE.keys())}')
                raise e
            response = requests.get(f"https://pokeapi.co/api/v2/type/{type_id}")
            if response.status_code == 200:
                poke_list = response.json()['pokemon']
                random_number = random.randint(0,len(poke_list)-1)
                random_pokemon = poke_list[random_number]['pokemon']['name']
                img_url = self.get_sprite(random_pokemon)
                await ctx.send(img_url)
            else:
                await ctx.send("Could not get pokemon type!")
