import discord, shutil, requests, random, time
from discord.ext import commands

class pokemon_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.TYPE = {'normal': 1, 'fighting': 2, 'flying': 3, 'poison': 4, 'ground': 5, 'rock': 6, 'bug': 7, 'ghost': 8, 'steel': 9, 'fire': 10, 'water': 11, 'grass': 12, 'electric': 13, 'psychic': 14, 'ice': 15, 'dragon': 16, 'dark': 17, 'fairy': 18}
        self.RACE = False

    def get_sprite(self,pokemon):
        ''' Get Pokemon sprite by name:str or id:int '''
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}")
        pokemon_name = response.json()['name']
        pokemon_img_url = response.json()['sprites']['front_default']
        return pokemon_name, pokemon_img_url

    @commands.command(name="pokemon", help="Returns a random pokemon sprite.")
    async def pokemon(self, ctx, *args):
        if len(args)==0:
            # Get a random pokemon if the type was not specified
            random_number = random.randint(1, 898)
            name, img_url = self.get_sprite(random_number)
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
                name, img_url = self.get_sprite(random_pokemon)
                await ctx.send(img_url)
            else:
                await ctx.send("Could not get pokemon type!")

    @commands.command(name="pokerace", help="Returns a random pokemon sprite for participants to guess.")
    async def race(self, ctx, max_number):
        # Get random Pokemon
        random_number = random.randint(1, int(max_number))
        name, img_url = self.get_sprite(random_number)

        # Send image
        self.RACE = name
        await ctx.send(img_url)

    @commands.command(name="pokeguess", help="For participants to submit answers to the pokemon race.")
    async def guess(self, ctx, guess, member: discord.Member = None):
        if self.RACE:
            if guess.lower()==self.RACE:
                self.RACE = False
                member = member or ctx.author
                await ctx.send('{0.name} won!'.format(member))
