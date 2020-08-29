import discord
from discord.ext import commands
from random import randint
import mysql.connector
import random

bot = commands.Bot(command_prefix = "b ")

mydb = mysql.connector.connect(
    host="192.168.0.45",
    port="4444",
    user="robin",
    password="password",
    database="mydb"
)
cursor = mydb.cursor()


bot.players = []
bot.cards = [("ace heart", 1), ("ace clubs", 1), ("ace diamonds", 1), ("ace spades", 1),
             ("2 heart", 2), ("2 clubs", 2), ("2 diamonds", 2), ("2 spades", 2),
             ("3 heart", 3), ("3 clubs", 3), ("3 diamonds", 3), ("3 spades", 3),
             ("4 heart", 4), ("4 clubs", 4), ("4 diamonds", 4), ("4 spades", 4),
             ("5 heart", 5), ("5 clubs", 5), ("5 diamonds", 5), ("5 spades", 5),
             ("6 heart", 6), ("6 clubs", 6), ("6 diamonds", 6), ("6 spades", 6),
             ("7 heart", 7), ("7 clubs", 7), ("7 diamonds", 7), ("7 spades", 7),
             ("8 heart", 8), ("8 clubs", 8), ("8 diamonds", 8), ("8 spades", 8),
             ("9 heart", 9), ("9 clubs", 9), ("9 diamonds", 9), ("9 spades", 9),
             ("10 heart", 10), ("10 clubs", 10), ("10 diamonds", 10), ("10 spades", 10),
             ("jack heart", 11), ("jack clubs", 11), ("jack diamonds", 11), ("jack spades", 11), 
             ("queen heart", 11), ("queen clubs", 11), ("queen diamonds", 11), ("queen spades", 11), 
             ("king heart", 11), ("king clubs", 11), ("king diamonds", 11), ("king spades", 11),]

bot.started = False
@bot.event
async def on_ready():
    bot.players = []
    #channel = bot.get_channel(748239354580959406)#groupchat
    channel = bot.get_channel(748251645242114078)#bottester
    await channel.send("Use ``b join`` to join the game and use ``b chips`` to see how much currency you have, if everyone joined use ``b start`` to start the game.")
    random.shuffle(bot.cards)
    cursor.execute("UPDATE main SET score = 0")


    

@bot.command()
async def join(ctx):
    if bot.started:
        return
    else:
        bot.players.append((ctx.message.author.name, 0, ctx.message.author.id))
        currentPlayers = []
        for a_tuple in bot.players:
            currentPlayers.append(a_tuple[0])
        try:
            currentPlayers = '\n'.join(currentPlayers)
            await ctx.send("current players:\n" + currentPlayers)
        except IOError as error:
            print(error)
            return

@bot.command()
async def start(ctx):
    bot.ace = []
    if bot.started:
        return
    else:
        bot.started = True
        cardnumber = 0
        score = 0
        test = 1
        while test <= 2:

            for player in bot.players:
                user = bot.get_user(player[2])
                if bot.cards[cardnumber][1] == 1:
                    bot.ace.append(player)
                cursor.execute("SELECT score FROM main WHERE username = '%s'"%player[0], multi=False)
                currentscore = cursor.fetchall()
                score = currentscore[0][0] + bot.cards[cardnumber][1]
                cursor.execute("UPDATE main SET score = %s WHERE username = '%s'"%(score, player[0]), multi = False)
                mydb.commit()
                cursor.execute("SELECT score FROM main WHERE username = '%s'"%(player[0]), multi = False)
                result = cursor.fetchall()
                await user.send(bot.cards[cardnumber][0])
                cardnumber = cardnumber + 1
            test = test + 1
        for player in bot.players:
            user = bot.get_user(player[2])
            cursor.execute("SELECT score FROM main WHERE username = '%s'"%(player[0]), multi = False)
            result = cursor.fetchall()
            if player in bot.ace:
                await user.send("you currently have: %s or %s"%(str(result[0][0]), str(result[0][0]+ 10)))
            else:
                await user.send("you currently have: " + str(result[0][0]))
        
        random.shuffle(bot.players)
        playerOrder = []
        for player in bot.players:
            playerOrder.append(player[0]) 
        playerOrder = '\n'.join(playerOrder)
        await ctx.send("it's time to place your bets in this order:\n" + playerOrder)
        
bot.playernumber = 0
@bot.command()
async def hit(ctx, arg):
    
    name = ctx.message.author.name
    
    bot.highestBet = 0
    print(bot.players[bot.playernumber][0])
    if int(arg) > bot.highestBet: bot.highestBet = int(arg)
    if name == bot.players[bot.playernumber][0]:
        print(bot.highestBet)
        
        bot.playernumber = bot.playernumber + 1
        cursor.execute("SELECT currency FROM main WHERE username = '%s'"%name)
        oldCurrency = cursor.fetchall()
        try:
            newCurrency = oldCurrency[0][0] - int(arg)
            if newCurrency < 0:
                await ctx.send("I'm sorry but you don't have enough chips to afford that, contact robinhood to buy more.")
                return
            else:
                cursor.execute("UPDATE main SET currency = %s WHERE username = '%s'"%(newCurrency, name), multi=False)
                cursor.execute("UPDATE main SET bet = %s WHERE username = '%s'"%(arg, name), multi=False)
                mydb.commit()
        except IOError as error:
            print(error)
            await ctx.send("You have to provide the amount you want to bet like this ``b hit 420``.")

        try:
            print(bot.players[bot.playernumber][0] + " you're up next to place your bet or stop or leave.")
        except:
            print("everyone has bet")
            stillToBet = []
            for player in bot.players:
                cursor.execute("SELECT bet FROM main WHERE username = '%s'"%player[0], multi=False)
                playerBet = cursor.fetchall()
                print(playerBet)
                if playerBet[0][0] < bot.highestBet:
                    stillToBet.append(player, bot.highestBet - playerBet)
                    print(stillToBet)
                else:
                    print(stillToBet)
    else:
        print("not your turn")
                




    

bot.run("token")