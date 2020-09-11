import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = "b ")

@bot.event
async def on_ready():
    print("done")

@bot.event
async def on_member_update(before, after):
    if str(before) == "robinhood#5663":
        n = after.nick
        if n:
            await after.edit(nick="try to change my name")



bot.run("NzQ4MjAxNjAwNTM4OTAyNTk5.X0Z_Cg.0YJmWFemKd908qDbm9xvr85Qlcg")