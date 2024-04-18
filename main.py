import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

#Load do .env
load_dotenv()
TOKEN = os.getenv('TOKEN')

#configs iniciais
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix='.', intents=intents)


@bot.command()
async def ola(ctx:commands.Context):
    user = ctx.author
    await ctx.reply(f'Olá {user.display_name}!')
    

@bot.event
async def on_ready():
    print('Estou pronto!')




bot.run(TOKEN)
