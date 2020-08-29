import discord
import pickle
import os
import mysql.connector

from discord.ext import commands

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Jakerick174",
    database="mydb"
)

bot = commands.Bot(command_prefix= "b ")
bot.remove_command("help")

print("starting up bee ...")

@bot.event
async def on_ready():
    print("bot is ready!")

@bot.command()
async def hi(ctx):
    await ctx.send("hello")

@bot.command()
async def blackjack(ctx):
    await ctx.send("starting up the game...")
    os.system('python3 blackjack.py')




bot.run("NzQ4MjAxNjAwNTM4OTAyNTk5.X0Z_Cg.0YJmWFemKd908qDbm9xvr85Qlcg")