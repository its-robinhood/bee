import discord 
import pickle
import lavalink
import youtube_dl
from discord.ext import commands

token = pickle.load(open('token.bat', 'rb'))
bot = commands.Bot(command_prefix = 'b ')

players = {}

@bot.event
async def on_ready():
    print('voice bot online')

@bot.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()
@bot.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()


bot.run(token)