import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!")

print("starting up bee2")
print("test")
@bot.event
async def on_message(ctx):
    if ctx.content == "Hello there":
        await ctx.channel.send("General Kenobi")
    if ctx.content == "test":
        ctx.channel.send("test succesfull")
    if ctx.content == "hello":
	if ctx.message.author.name == "robinhood":
	    await ctx.channel.send("Hi darling")
bot.run("NzQ4MjAxNjAwNTM4OTAyNTk5.X0Z_Cg.0YJmWFemKd908qDbm9xvr85Qlcg")
