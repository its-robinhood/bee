import discord
import random
import os
import mysql.connector

from discord.ext import commands

mydb = mysql.connector.connect(
    host="192.168.0.45",
    port='4444',
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
    await bot.change_presence(activity=discord.Game(name='bzzzzzzzzzzzzzzzzz'))
    print("bee is ready!")

@bot.command()
async def hi(ctx):
    charli = ["hi charli bee, mama bee believes you can do anything <:ghosthugright:748209219714547764>", "hyellow charli, did momma bee tell you she loves you to the moon and back?, well she does!"]
    if ctx.message.author.name == "heyimlu":
        await ctx.send(random.choice(charli))
        return
    if ctx.message.author.name == "Charli":
        await ctx.send()
        return
    if ctx.message.author.name == "THE SEER":
        await ctx.send("hi seer, bee just wants to say she loves you.")
        return
    if ctx.message.author.name == "KermisKlant":
        await ctx.send("hyellow fries, mama bee and charli bee beelieve you can do anything")
        return
    if ctx.message.author.name == "Cavemaker":
        await ctx.send("hi plop, have a plop cookie 🍪")
        return
    await ctx.send("hyellow <:ghosthugright:748209219714547764>")


@bot.command()
async def blackjack(ctx):
    await ctx.send("shuffling cards...")
    await ctx.send("go to <#748239354580959406> to play the game")
    os.system('python3 blackjack.py')

@bot.command()
async def stickbug(ctx):
    await ctx.send(file=discord.File('stickbug.gif'))
@bot.command()
async def cookie(ctx):
    await ctx.send("🍪")
@bot.command()
async def cookies(ctx, *arg):
    cookies = 3
    test = 1
    while test <= cookies:
        await ctx.send("🍪")
        test = test + 1
    if arg[0] == "infinite":
        while True:
            await ctx.send("🍪")
@bot.command()
async def inject(ctx, arg):
    if ctx.message.author.name == "robinhood":
        cursor.execute(arg, multi=False)
        result = cursor.fetchall()
        await ctx.send(result)
@bot.command()
async def ping(ctx, arg):
    if True:
        print(arg)
        while True:
            await ctx.send(arg)
    else:
        await ctx.send("that function is temporarily disabled because too powerfull")






bot.run("NzQ4MjAxNjAwNTM4OTAyNTk5.X0Z_Cg.0YJmWFemKd908qDbm9xvr85Qlcg")
