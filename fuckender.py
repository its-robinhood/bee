import discord
import pickle
from tqdm import tqdm, trange
from termcolor import colored
import time
import sys

from discord.ext import commands

bot = commands.Bot(command_prefix= "b ")


target = "robinhood#5663"

token = pickle.load(open('token.bat', 'rb'))

@bot.event
async def on_ready():
    with tqdm(total = 100) as progressbar:
        for i in range(25):
            time.sleep(0.05)
            progressbar.update(4)
    
    text = ("   _____                 _ _                                 _           \n  / ____|               | | |                               | |          \n | |  __  ___   ___   __| | |__  _   _  ___    ___ _ __   __| | ___ _ __ \n | | |_ |/ _ \ / _ \ / _` | '_ \| | | |/ _ \  / _ \ '_ \ / _` |/ _ \ '__|\n | |__| | (_) | (_) | (_| | |_) | |_| |  __/ |  __/ | | | (_| |  __/ |   \n  \_____|\___/ \___/ \__,_|_.__/ \__, |\___|  \___|_| |_|\__,_|\___|_|   \n                                  __/ |                                  \n                                 |___/                              ")
    print(text)


@bot.event
async def on_message(ctx):
    if (str(ctx.author) == target):
        await ctx.delete()

bot.run(token)