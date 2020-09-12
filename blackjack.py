import discord
from discord.ext import commands
from random import randint
import mysql.connector
import random
import pickle

bot = commands.Bot(command_prefix = "b ")

mydb = mysql.connector.connect(
    host="192.168.0.45",
    port="4444",
    user="robin",
    password="password",
    database="mydb"
)
cursor = mydb.cursor()

token = pickle.load(open('token.bat', 'rb'))

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



bot.busted = []
bot.standing = []
bot.cardnumber = 0
bot.pot = 0


async def deal_card():
    print("test")

bot.started = False
@bot.event
async def on_ready():
    bot.players = []
    #channel = bot.get_channel(748239354580959406)#groupchat
    channel = bot.get_channel(748251645242114078)#bottester
    await channel.send("Use ``b join`` to join the game and use ``b chips`` to see how much currency you have, if everyone joined use ``b start`` to start the game.")
    random.shuffle(bot.cards)
    cursor.execute("UPDATE main SET score = 0")
    cursor.execute("UPDATE main SET bet = 0")
    mydb.commit()


    

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
        score = 0
        test = 1
        while test <= 2:

            for player in bot.players:
                user = bot.get_user(player[2])
                if bot.cards[bot.cardnumber][1] == 1:
                    bot.ace.append(player)
                cursor.execute("SELECT score FROM main WHERE username = '%s'"%player[0], multi=False)
                currentscore = cursor.fetchall()
                score = currentscore[0][0] + bot.cards[bot.cardnumber][1]
                cursor.execute("UPDATE main SET score = %s WHERE username = '%s'"%(score, player[0]), multi = False)
                mydb.commit()
                cursor.execute("SELECT score FROM main WHERE username = '%s'"%(player[0]), multi = False)
                result = cursor.fetchall()
                await user.send(bot.cards[bot.cardnumber][0])
                bot.cardnumber = bot.cardnumber + 1
            test = test + 1
        for player in bot.players:
            user = bot.get_user(player[2])
            cursor.execute("SELECT score FROM main WHERE username = '%s'"%(player[0]), multi = False)
            result = cursor.fetchall()
            if player in bot.ace and result[0][0] + 10 < 21:
                await user.send("you currently have: %s or %s"%(str(result[0][0]), str(result[0][0]+ 10)))
            else:
                await user.send("you currently have: " + str(result[0][0]))
                
        
        random.shuffle(bot.players)
        playerOrder = []
        for player in bot.players:
            playerOrder.append(player[0]) 
        playerOrder = '\n'.join(playerOrder)
        await ctx.send("it's time to place your bets in this order:\n" + playerOrder)
    for player in bot.players:
        cursor.execute("SELECT score FROM main WHERE username = '%s'"%player[0], multi=False)
        result = cursor.fetchall()
        if result[0][0] > 21:
            bot.busted.append(player[0])
            channel = bot.get_channel(748251645242114078)
            await channel.send(player[0] + " is busted")
        
bot.playernumber = 0
bot.stillToBet = []
@bot.command()
async def hit(ctx, arg):
    name = ctx.message.author.name
    if name in bot.standing:
        await ctx.send("You can't get another card anymore, you're standing")
    
    bot.highestBet = 0
    if int(arg) > bot.highestBet: bot.highestBet = int(arg)
    if int(arg) < bot.highestBet:
        await ctx.send("you're not betting enough")
        return
    try:
        if name == bot.players[bot.playernumber][0]:
            bot.playernumber = bot.playernumber + 1
            cursor.execute("SELECT currency FROM main WHERE username = '%s'"%name, multi=False)
            oldCurrency = cursor.fetchall()
            try:
                newCurrency = oldCurrency[0][0] - int(arg)
                if newCurrency < 0:
                    await ctx.send("I'm sorry but you don't have enough chips to afford that, contact robinhood to buy more.")
                    playernumber = playernumber - 1
                    return
                else:
                    cursor.execute("SELECT bet FROM main WHERE username = '%s'"%name, multi=False)
                    result = cursor.fetchall()
                    oldBet = result[0]
                    totalBet = oldBet[0] + int(arg)
                    cursor.execute("UPDATE main SET currency = %s WHERE username = '%s'"%(newCurrency, name), multi=False)
                    cursor.execute("UPDATE main SET bet = %s WHERE username = '%s'"%(totalBet, name), multi=False)
                    mydb.commit()
                    bot.pot = bot.pot + arg
            except IOError as error:
                print(error)
                await ctx.send("You have to provide the amount you want to bet like this ``b hit 420``.")

            try:
                await ctx.send(bot.players[bot.playernumber][0] + " you're up next to place your bet, stand or leave.")
            except:
                for player in bot.players:
                    cursor.execute("SELECT bet FROM main WHERE username = '%s'"%player[0], multi=False)
                    playerBet = cursor.fetchall()
                    if playerBet[0][0] < bot.highestBet:
                        bot.stillToBet.append((player[0], bot.highestBet - playerBet[0][0]))
                    else:
                        continue
                if bot.stillToBet:
                    await ctx.send("these people still have to bet")
                    for x in bot.stillToBet:
                        await ctx.send("%s: %d"%(x[0],x[1]))
                else:
                    await ctx.send("Ok bets are placed the next card will be dealt")
                    bot.cardnumber = 0
                    for player in bot.players:
                        user = bot.get_user(player[2])
                        if bot.cards[bot.cardnumber][1] == 1:
                            bot.ace.append(player)
                        cursor.execute("SELECT score FROM main WHERE username = '%s'"%player[0], multi=False)
                        currentscore = cursor.fetchall()
                        score = currentscore[0][0] + bot.cards[bot.cardnumber][1]
                        cursor.execute("UPDATE main SET score = %s WHERE username = '%s'"%(score, player[0]), multi = False)
                        mydb.commit()
                        cursor.execute("SELECT score FROM main WHERE username = '%s'"%(player[0]), multi = False)
                        result = cursor.fetchall()
                        await user.send(bot.cards[bot.cardnumber][0])
                        bot.cardnumber = bot.cardnumber + 1  
                    for player in bot.players:
                        user = bot.get_user(player[2])
                        cursor.execute("SELECT score FROM main WHERE username = '%s'"%(player[0]), multi = False)
                        result = cursor.fetchall()
                        if player in bot.ace and result[0][0] + 10 < 21:
                            await user.send("you currently have: %s or %s"%(str(result[0][0]), str(result[0][0]+ 10)))
                        else:
                            await user.send("you currently have: " + str(result[0][0]))
            
        else:
            print("not your turn")
    except:
        names = []
        for a_tuple in bot.stillToBet:
            names.append(a_tuple[0])
        if name in names:
            test = dict(bot.stillToBet)
            print(bot.stillToBet)
            print(bot.stillToBet.index((name, int(arg))))
            if int(arg) == test[name]:
                assert bot.stillToBet[bot.stillToBet.index((name, int(arg)))]
                print(bot.stillToBet)
            else:
                print("that's not the right amount")
            cursor.execute("SELECT currency FROM main WHERE username = '%s'"%name, multi=False)
            oldCurrency = cursor.fetchall()
            try:
                newCurrency = oldCurrency[0][0] - int(arg)
                if newCurrency < 0:
                    await ctx.send("I'm sorry but you don't have enough chips to afford that, contact robinhood to buy more.")
                    return
                else:
                    cursor.execute("SELECT bet FROM main WHERE username = '%s'"%name, multi=False)
                    result = cursor.fetchall()
                    oldBet = result[0]
                    totalBet = oldBet[0] + int(arg)
                    cursor.execute("UPDATE main SET currency = %s WHERE username = '%s'"%(newCurrency, name), multi=False)
                    cursor.execute("UPDATE main SET bet = %s WHERE username = '%s'"%(totalBet, name), multi=False)
                mydb.commit()
            except IOError as error:
                await ctx.send("You have to provide the amount you want to bet like this ``b hit 420``.")

            try:
                await ctx.send(bot.players[bot.playernumber][0] + " you're up next to place your bet, stand or leave.")
            except:
                bot.stillToBet = []
                for player in bot.players:
                    cursor.execute("SELECT bet FROM main WHERE username = '%s'"%player[0], multi=False)
                    playerBet = cursor.fetchall()
                    if playerBet[0][0] < bot.highestBet:
                        bot.stillToBet.append((player[0], bot.highestBet - playerBet[0][0]))
                    else:
                        continue
            if bot.stillToBet:
                await ctx.send("these people still have to bet")
                for x in bot.stillToBet:
                    await ctx.send("%s: %d"%(x[0],x[1]))
            else:
                await ctx.send("Ok bets are placed the next card will be dealt")  


                for player in bot.players:
                    user = bot.get_user(player[2])
                    if bot.cards[bot.cardnumber][1] == 1:
                        bot.ace.append(player)
                    cursor.execute("SELECT score FROM main WHERE username = '%s'"%player[0], multi=False)
                    currentscore = cursor.fetchall()
                    score = currentscore[0][0] + bot.cards[bot.cardnumber][1]
                    cursor.execute("UPDATE main SET score = %s WHERE username = '%s'"%(score, player[0]), multi = False)
                    mydb.commit()
                    cursor.execute("SELECT score FROM main WHERE username = '%s'"%(player[0]), multi = False)
                    result = cursor.fetchall()
                    await user.send(bot.cards[bot.cardnumber][0])
                    bot.cardnumber = bot.cardnumber + 1  
                for player in bot.players:
                    user = bot.get_user(player[2])
                    cursor.execute("SELECT score FROM main WHERE username = '%s'"%(player[0]), multi = False)
                    result = cursor.fetchall()
                    if player in bot.ace and str(result[0][0] + 10) < 21:
                        await user.send("you currently have: %s or %s"%(str(result[0][0]), str(result[0][0]+ 10)))
                    else:
                        await user.send("you currently have: " + str(result[0][0]))
    for player in bot.players:
        cursor.execute("SELECT score FROM main WHERE username = '%s'"%player[0], multi=False)
        result = cursor.fetchall()
        if result[0][0] > 21:
            bot.busted.append(player[0])
            channel = bot.get_channel(748251645242114078)
            await channel.send(player[0] + " is busted")
            for player in bot.players:
                if player in bot.standing or player in bot.busted:
                    print("game ended these are the scores")
                
            #print("these people still have to bet: ")
bot.end = False                    
@bot.command()
async def stand(ctx):
    name = ctx.message.author.name
    bot.standing.append(name)
    
    if name in bot.ace:
        cursor.execute("SELECT score FROM main WHERE username = '%s'"%name, multi=False)
        result = cursor.fetchall()
        if result[0][0] + 10 <= 21:
            score = result[0][0] + 10
            cursor.execute("UPATE main SET score WHERE username = '%s'"%name)
    for player in bot.players:
        print("test")
        print(player[0], bot.standing, bot.busted, bot.end)
        print(bot.standing)
        if player[0] in bot.standing or player[0] in bot.busted:
            print("test1")
            bot.end = True
        else: 
            bot.end = False
            break
    if bot.end:
        print("game ended these are the scores")
        cursor.execute("SELECT * FROM main WHERE score > 0 ORDER BY score ASC")
        result = cursor.fetchall()
        print(result)


    

bot.run(token)