import discord
import pickle
import time
import sys

from discord.ext import commands
from discord.utils import get

bot = commands.Bot(command_prefix= "b ")

token = pickle.load(open('token.bat', 'rb'))


@bot.command()
async def remove(ctx, role: discord.Role, user: discord.Member):
    await user.remove_roles(role)
bot.run(token)