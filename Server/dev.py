from asyncio import events
import asyncio
from Modul import *

import nextcord
from nextcord import *
from nextcord.embeds import Embed
from nextcord.ext.commands.core import check
from nextcord.shard import EventType
from nextcord.utils import get
from nextcord.abc import GuildChannel
from nextcord.ext import commands,tasks
from nextcord.http import Route

import datetime, time, json, random, func
from datetime import *
from time import *
from func import emojis
from random import randrange

class Dev(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @nextcord.slash_command(name="핑", description="현재 핑을 알 수 있습니다")
    async def 핑(self, interaction : nextcord.Interaction):
        gcolor=0x336bff
        ecolor=0x00ff56
        ncolor=0xd9ea33
        bedcolor=0xc70039
        omgcolor=0xff0000
        errorcolor=0x8b111e
        pings=round(self.bot.latency * 1000)
        if pings <= 100: 
            pinglevel="🔵 아주 좋음"
            color=gcolor
        elif pings <= 200:
            pinglevel="🟢 좋음"
            color=ecolor
        elif pings <= 300:
            pinglevel="🟡 보통"
            color=ncolor
        elif pings <= 500:
            pinglevel="🔴 나쁨"
            color=bedcolor
        elif pings <= 600:
            pinglevel="🔴 매우 나쁨"
            color=omgcolor
        else:
            pinglevel="🚫 불안정"
            color=errorcolor
        await interaction.response.defer()
        embed=nextcord.Embed(title="🏓 퐁!", description=f"{pings}ms\n{pinglevel}", color=color)
        await interaction.followup.send(embed=embed)

    @nextcord.slash_command(name="봇정보", description="봇 정보를 보여줍니다")
    async def 봇정보(self, interaction : nextcord.Interaction):
        await interaction.response.defer()
        pings=round(self.bot.latency * 1000)
        embed=nextcord.Embed(title="봇정보", description="", color=0x2f3136)
        embed.add_field(name="• 봇 이름", value=self.user.bot, inline=True)
        embed.add_field(name="• 봇 접두사", value=f"Slash Command 지원", inline=True)
        embed.add_field(name="• 봇 핑", value=f"{pings}m/s")
        embed.set_thumbnail(url=botprofile)
        await interaction.followup.send(embed=embed)
    
    @nextcord.slash_command(name="저장하기", description="단어를 기억합니다")
    async def 저장하기(self, interaction : nextcord.Interaction, 단어 : str=SlashOption(description="단어"), 내용 : str=SlashOption(description="내용")):
        await interaction.response.defer()
        if 단어 is None or 내용 is None or (단어 is None and 내용 is None):
            await interaction.followup.send("단어 또는 내용을 입력해주세요")
        else:
            with open("data.json", "r", encoding="UTF-8") as f:
                data=json.load(f)
                for i in data["remember"]:
                    if str(단어) in i:
                        await interaction.followup.send(f"{단어}은 이미 있는 단어입니다")
                        return False
            data["remember"][f"{단어}"]=str(내용)
            with open("data.json", "w", encoding="UTF-8") as ff:
                json.dump(data, ff, ensure_ascii=False, indent="\t")
            await interaction.followup.send(f"{단어}는(은) {내용}이라고 저장했습니다")

    @nextcord.slash_command(name="불러오기", description="저장한 내용을 불러옵니다")
    async def 불러오기(self, interaction : nextcord.Interaction, 단어 : str=SlashOption(description="단어")):
        await interaction.response.defer()
        try:
            with open("data.json", "r", encoding="UTF-8") as f:
                data=json.load(f)
                await interaction.followup.send(f"{단어}는(은) " + data["remember"][str(단어)])
        except KeyError:
            await interaction.followup.send(f"{단어}는 저장되지않은 단어입니다")

def setup(bot):
    bot.add_cog(Dev(bot))