import os
from dotenv import load_dotenv
import discord
from discord import app_commands
from discord.ext import commands

#Load do .env
load_dotenv()
TOKEN = os.getenv('TOKEN')

#configs iniciais
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix='.', intents=intents)

@bot.event
async def on_ready():
    await bot.tree.sync()
    print('Estou pronto!')

@bot.tree.command(description='Te envia um olá de volta :)')
async def ola(interact:discord.Interaction):
    await interact.response.send_message(f'Olá {interact.user.name}')

@bot.tree.command(description='Te passa informações sobre um personagem')
async def sobre(interact:discord.Integration, personagem:str):
    ...







bot.run(TOKEN)
