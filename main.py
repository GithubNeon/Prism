import os
import asyncio
import platform
from Modul import *

import nextcord
from nextcord.ext import commands, tasks

import func
from func import emojis

intents=nextcord.Intents.all()

bot=commands.Bot(intents=intents)

for filename in os.listdir("./Server"):
    if filename.endswith(".py"):
        bot.load_extension(f"Server.{filename[:-3]}")
for filename in os.listdir("./Service"):
    if filename.endswith(".py"):
        bot.load_extension(f"Service.{filename[:-3]}")
for filename in os.listdir("./Util"):
    if filename.endswith(".py"):
        bot.load_extension(f"Util.{filename[:-3]}")

@bot.event
async def on_ready():
    os.system("cls")
    print("=============================")
    print("System Version\n")
    print(f"Python Version: {platform.python_version()}")
    print(f"Nextcord Version: {nextcord.__version__}")
    print("=============================")
    print("Discord Bot Info\n")
    print(f"Bot Name: {bot.user}")
    print(f"Bot ID: {bot.user.id}")
    print("=============================")
    print("Load was Successful")
    await bot.change_presence(activity=nextcord.Game(f"{len(bot.guilds)}개의 서버와 함께"))

bot.run(token)
