import discord
import random
import os
#import mysql.connector
import pickle

from discord.ext import commands

#mydb = mysql.connector.connect(
    #host="localhost",
    #host="192.168.0.45",
    #port='4444',
    #user="robin",
    #password="password",
    #database="mydb"
#)
#cursor = mydb.cursor()

bot = commands.Bot(command_prefix= "b ")
bot.remove_command("help")

print("starting up bee ...")

bot.spam = False
pickle.dump("token", open('token.bat', 'wb'))
token = pickle.load(open('token.bat', 'rb'))

bot.robin = []
#pickle.dump(bot.robin, open("robin.bat", "wb"))
bot.robin = pickle.load(open('robin.bat', 'rb'))
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name='bzzzzzzzzzzzzzzzzz'))
    print("bee is ready!")
bot.fries = 0
bot.ender = 0
bot.charli = 0
bot.seer = 0
bot.plop = 0
bot.electro = 0
bot.lu = 0
bot.jerry = 0
@bot.command()
async def hi(ctx):

    ender = ["hi ender, bee thinks you're really smart <:ghosthugright:748209219714547764>", "hyellow ender, make sure to feed your rabbits", 
            "Hey mr.rabbit, do neutrinos have mass?", "wouldnt you like to know rabbit boy", "hyellowowowowowow make sure to go to bed at 10:30pm you have to stay smart and feed your rabbits yes you must achieve something in life and not be a complete failure like charli is"]
    charli = ["hi charli bee, mama bee believes you can do anything <:ghosthugright:748209219714547764>",
                 "hyellow charli, did momma bee tell you she loves you to the moon and back?, well she does!", 
                 "hyellow charli smart bee thinks you are very smart but you should give yourself a break sometimes because you already achieved great things and will keep doing that and bee thinks youre awesome"]

    fries = ["hyellow you are very nice person", "i", "appreciate", "you", "alot", "hyellow you are my bestest frend", "hyellow fries a bee here thinks youre really funny and smart and youre a great friend but you must also stop smoking and forcing yourself to go to the gym every day but for the rest youre a really nice guy",
                 "hyellow fries, mama bee and charli bee beelieve you can do anything",
                  "hi fries, you're such a nice guy and hacker bee looks up to you!", "buzz buzz buzz buzz buzz buzz buzz buzz buzz buzz buzz. buzz buzz buzz? buzz!", 
                  "hyellow i love you as frend"]
    seer = ["hi seer, bee just wants to say she loves you.", "Hi seer. Don't forget to take a shit on your cousins car today!",
             "Hey Seer. Big bee doesn't want you to leave again", "hi youre the best fish there is, and electro too, keep it up #fishgang."]
    plop = ["hyellow, would you like a bee cookie? its a plop cookie but instead of having the word plop and plops hat, its a bee!", "buzzzzbzuzuzuuzuzuzbuzzzbuzzbuzzbuzzbuzz buzzzzzz"]
    lu = ["Bee does not want Lu to steal more coastlines",
                 "bee thinks you are a very nice and smart person and don't say you're dumb",
		 "hi lu, you get two hugs because you're awesome <:ghosthugright:748209219714547764> <:ghosthugrithugright:748209219714547764>","Bee needs to tell you that you are really loved, she heard that from a person that really loves you"]
    
    electro = ["hi you're the best fish there is, and Seer is too, keep it up #fishgang"]
    jerry = ["you're doing great, i'm proud of you <:ghosthugright:748209219714547764>", "remember to eat regularly!", "take care of yourself <3"]

    if ctx.message.author.name == "heyimlu":
        await ctx.send(lu[bot.lu])
        bot.lu = bot.lu + 1
        if bot.lu == len(lu):
	        bot.lu = 0
        return
    if ctx.message.author.name == "Charli":
        await ctx.send(charli[bot.charli])
        bot.charli = bot.charli + 1
        if bot.charli == len(charli):
            bot.charli = 0
        return
    if ctx.message.author.name == "THE SEER":
        await ctx.send(seer[bot.seer])
        bot.seer = bot.seer + 1
        if bot.seer == len(seer):
            bot.seer = 0
        return
    if ctx.message.author.name == "KermisKlant":
        await ctx.send(fries[bot.fries])
        bot.fries = bot.fries + 1
        if bot.fries == len(fries):
            bot.fries = 0
        return
    if ctx.message.author.name == "Cavemaker":
        await ctx.send(plop[bot.plop])
        bot.plop = bot.plop + 1
        if bot.plop == len(plop):
            bot.plop = 0
        return
    if ctx.message.author.name == "endergamer0134":
        await ctx.send(ender[bot.ender])
        bot.ender = bot.ender + 1
        if bot.ender == len(ender):
            bot.ender = 0
        return
    if ctx.message.author.name == "robinhood":
        await ctx.send(random.choice(bot.robin))
        return

    if ctx.message.author.name == "Jerry":
	    await ctx.send(jerry[bot.jerry])
	    bot.jerry = bot.jerry + 1
	    if bot.jerry == len(jerry):
	        bot.jerry = 0
    if ctx.message.author.name == "ElectroYT":
        await ctx.send(electro[bot.electro])
        bot.electro = bot.electro + 1
        if bot.electro == len(electro):
            bot.electro = 0
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
    bot.spam = True
    cookies = 3
    test = 1
    while test <= cookies:
        await ctx.send("🍪")
        test6 = test + 1
    #if arg[0] == "infinite":
        #while bot.spam:            
            #await ctx.send("🍪")
@bot.command()
async def inject(ctx, arg):
    if ctx.message.author.name == "robinhood":
        cursor.execute(arg, multi=False)
        result = cursor.fetchall()
        await ctx.send(result)
@bot.command()
async def ping(ctx, arg):
    bot.spam = True
    if False:
        print(arg)
        while True:
            await ctx.send(arg)
    else:
        await ctx.send("that function is temporarily disabled because too powerfull")
@bot.command()
async def himessage(ctx, arg):
    bot.robin.append(arg)
    pickle.dump(bot.robin, open("robin.bat", "wb"))

@bot.command()
async def hug(ctx, *arg):
    await ctx.send("<:ghosthugright:748209219714547764>")
   # if arg[0] == "infinite":
       # bot.spam = True
       # while bot.spam:
           # await ctx.send("<:ghosthugright:748209219714547764>")


@bot.command()
async def stop(ctx):
    bot.spam = False
@bot.command()
async def script(ctx):
    server = ctx.message.server
    voice_bot = bot.voice_client_in(server)





bot.run(token)
