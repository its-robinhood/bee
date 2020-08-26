import discord
import pickle
from discord.ext import commands

bot = commands.Bot(command_prefix = "b ")

channel = bot.get_channel(748251645242114078)

@bot.event
async def on_ready():
    await bot.channel.send("Use ``b join`` to join the game and use ``b chips`` to see how much currency you have")

@bot.command()
async def join(ctx):
    print("joined")
    

bot.run("NzQ4MjAxNjAwNTM4OTAyNTk5.X0Z_Cg.0YJmWFemKd908qDbm9xvr85Qlcg")