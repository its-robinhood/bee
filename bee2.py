import discord
from discord.ext import commands
import pickle

bot = commands.Bot(command_prefix="!")

token = pickle.load(open('token.bat', 'rb'))

print("starting up bee2")

@bot.event
async def on_message(ctx):
    if ctx.content == "Hello there":
        await ctx.channel.send("General Kenobi")
    if ctx.content == "test":
        ctx.channel.send("test succesfull")
    if ctx.content == "hello":
        if ctx.author.name == "robinhood":
            await ctx.channel.send("Hi darling")
@bot.event
async def on_member_update(before, after):
    if before.nick == "robinhood":
        await after.edit(nick="try to change my nickname CHARLI")

bot.run(token)
