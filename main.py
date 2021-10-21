import discord

from discord.ext import commands

import os



intents = discord.Intents.default()

intents.members = True



testing = False



client = commands.Bot(command_prefix = "m!", case_insensitive = True, intents=intents)



client.remove_command('help')



@client.event

async def on_ready():

    print('Entramos como {0.user}'.format(client))



    await client.change_presence (activity=discord.Activity (type=discord.ActivityType.listening, name="Ouvindo Músicas"))



for filename in os.listdir('./cogs'):

    if filename.endswith('.py'):

        client.load_extension(f'cogs.{filename[:-3]}')



client.run('Coloque seu Token aqui')
