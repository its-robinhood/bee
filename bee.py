import discord
import random
import os
import mysql.connector
import pickle

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

bot.robin = []
#pickle.dump(bot.robin, open("robin.bat", "wb"))
bot.robin = pickle.load(open('robin.bat', 'rb'))
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name='bzzzzzzzzzzzzzzzzz'))
    print("bee is ready!")

@bot.command()
async def hi(ctx):

    ender = ["hi ender, bee thinks you're really smart <:ghosthugright:748209219714547764>", "hyellow ender, make sure to feed your rabbits", 
            "Hey mr.rabbit, do neutrinos have mass?"]
    charli = ["hi charli bee, mama bee believes you can do anything <:ghosthugright:748209219714547764>",
                 "hyellow charli, did momma bee tell you she loves you to the moon and back?, well she does!", 
                 "hyellow charli smart bee thinks you are very smart but you should give yourself a break sometimes because you already achieved great things and will keep doing that and bee thinks youre awesome"]

    fries = ["hyellow fries a bee here thinks youre really funny and smart and youre a great friend but you must also stop smoking and forcing yourself to go to the gym every day but for the rest youre a really nice guy",
                 "hyellow fries, mama bee and charli bee beelieve you can do anything", "hi fries, you're such a nice guy and hacker bee looks up to you!"]
    seer = ["hi seer, bee just wants to say she loves you.", "Hi seer. Don't forget to take a shit on your cousins car today!", "Hey Seer. Big bee doesn't want you to leave again"]

    if ctx.message.author.name == "heyimlu":
        await ctx.send("hi lu, you get two hugs because you're awesome <:ghosthugright:748209219714547764> <:ghosthugright:748209219714547764>")
        return
    if ctx.message.author.name == "Charli":
        await ctx.send(random.choice(charli))
        return
    if ctx.message.author.name == "THE SEER":
        await ctx.send(random.choice(seer))
        return
    if ctx.message.author.name == "KermisKlant":
        await ctx.send(random.choice(fries))
        return
    if ctx.message.author.name == "Cavemaker":
        await ctx.send("hi plop, have a plop cookie 🍪")
        return
    if ctx.message.author.name == "endergamer0134":
        await ctx.send(random.choice(ender))
        return
    if ctx.message.author.name == "robinhood":
        await ctx.send(random.choice(bot.robin))
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
@bot.command()
async def himessage(ctx, arg):
    bot.robin.append(arg)
    pickle.dump(bot.robin, open("robin.bat", "wb"))






bot.run("NzQ4MjAxNjAwNTM4OTAyNTk5.X0Z_Cg.0YJmWFemKd908qDbm9xvr85Qlcg")
