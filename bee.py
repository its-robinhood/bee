import discord

import os
import mysql.connector

from discord.ext import commands

mydb = mysql.connector.connect(
    host="localhost",
    user="robin",
    password="password",
    database="mydb"
)
cursor = mydb.cursor()

bot = commands.Bot(command_prefix= "b ")
bot.remove_command("help")

print("starting up bee ...")

@bot.event
async def on_ready():
    print("bee is ready!")

@bot.command()
async def hi(ctx):
    await ctx.send("hyellow")

@bot.command()
async def blackjack(ctx):
    await ctx.send("shuffling cards...")
    await ctx.send("go to <#748239354580959406> to play the game")
    os.system('python3 blackjack.py')

@bot.command()
async def stickbug(ctx):
    await ctx.send(file=discord.File('stickbug.gif'))






bot.run("NzQ4MjAxNjAwNTM4OTAyNTk5.X0Z_Cg.0YJmWFemKd908qDbm9xvr85Qlcg")
