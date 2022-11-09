import asyncio
from Modul import *

import nextcord
from nextcord import *
from nextcord.utils import get
from nextcord.ext import commands

import datetime, time, requests, humanfriendly, json, random, ast
from datetime import *
from time import *
from bs4 import BeautifulSoup
from PingPongTool import PingPong

class API(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @nextcord.slash_command(name="코로나", description="현재 대한민국 코로나 정보를 불러옵니다")
    async def 코로나(self, interaction : nextcord.Interaction, 지역 : str=SlashOption(description="지역을 선택해주세요", choices=covidList)):
        req=requests.get("https://api.corona-19.kr/korea/?serviceKey=8vyWbBNFgRXpnjToZ7AGwecqzx5Ui3m9Y").json()
        req2=requests.get("https://api.corona-19.kr/korea/country/new/?serviceKey=8vyWbBNFgRXpnjToZ7AGwecqzx5Ui3m9Y").json()
        await interaction.response.defer()
        choice = str={"전국":"korea","서울":"seoul","부산":"busan","대구":"daegu","인천":"incheon","광주":"gwangju","대전":"daejeon","울산":"ulsan","세종":"sejong","경기도":"gyeonggi","강원도":"gangwon","충청북도":"chungbuk","충청남도":"chungnam","전라북도":"jeonbuk","전라남도":"jeonnam","경상북도":"gyeongbuk","경상남도":"gyeongnam","제주":"jeju"}[지역]
        기준="{}".format(req['updateTime'])
        확진환자="{} + {}".format(req['TotalCase'], req2[f'{choice}']["newCase"])
        격리해제="{} + {}".format(req['TotalRecovered'], req2[f'{choice}']['recovered'])
        치료중="{} + {}".format(req['NowCase'], req2[f'{choice}']['newCase'])
        사망="{} + {}".format(req['TotalDeath'], req['TodayDeath'])
        embed=nextcord.Embed(title=f"기준일 | {기준}",description=f"**확진환자 | {확진환자}\n격리해제 | {격리해제}\n치료중(격리중) | {치료중}\n사망 | {사망}**",color=0x2f3136,url="http://ncov.mohw.go.kr/")
        embed.set_thumbnail(url ="https://api.corona-19.kr/")
        embed.set_footer(text=f"지역: {지역}")
        await interaction.followup.send(embed=embed)
        
    @nextcord.slash_command(name="강아지", description="강아지")
    async def 강아지(self, interaction : nextcord.Interaction):
        await interaction.response.defer()
        dog=requests.get("https://api.thedogapi.com/v1/images/search").json()[0]["url"]

        await interaction.followup.send(dog)

    @nextcord.slash_command(name="고양이", description="고양이")
    async def 고양이(self, interaction : nextcord.Interaction):
        await interaction.response.defer()
        cat=requests.get("https://api.thecatapi.com/v1/images/search").json()[0]["url"]

        await interaction.followup.send(cat)

    @nextcord.slash_command(name="한강", description="서울 한강 수온을 알려줍니다")
    async def 한강(self, interaction : nextcord.Interaction):
        await interaction.response.defer()
        han=requests.get("https://api.hangang.msub.kr/").json()
        temp=han["temp"]

        wiseword = random.choice(wiseList)

        embed=nextcord.Embed(title=f"🏞 현재 한강 수온은 **{temp}℃** 입니다", color=0x2f3136)
        embed.set_footer(text=f'"{wiseword}"')
        await interaction.followup.send(embed=embed)

    @nextcord.slash_command(name="마인크래프트", description="마인크래프트 플레이어 정보를 불러옵니다")
    async def 마인크래프트(self, interaction : nextcord.Interaction, 닉네임 : str=SlashOption(description="마인크래프트 낙네임")):
        await interaction.response.defer()

        name=닉네임
        mine_main=requests.get(f"https://api.mojang.com/users/profiles/minecraft/{name}").json()
        name=mine_main["name"]
        uuid=mine_main["id"]

        mine_skin=(f"https://mc-heads.net/avatar/{uuid}")

        embed=nextcord.Embed(title="마인크래프트 정보", color=0x2f3136)
        embed.add_field(name="닉네임", value=f"{name}", inline=False)
        embed.add_field(name="UUID", value=f"{uuid}")
        embed.set_thumbnail(url=f"{mine_skin}")
        await interaction.followup.send(embed=embed)

    @nextcord.slash_command(name="프리즘", description="봇과 대화를 합니다")
    async def 프리즘(self, interaction : nextcord.Interaction, 대화 : str=SlashOption(description="대화하기")):
        URL="https://builder.pingpong.us/api/builder/621b46b0e4b019e73844626f/integration/v0.2/custom/"
        Authorization="Basic a2V5OjU1ODk3MGQ3NmZhMDZhMzMxMzIwOTdhODdmZDA2ZTk3"

        Ping=PingPong(URL, Authorization)

        data=dict(await Ping.Pong("Example", 대화))["text"]
        await interaction.response.send_message(data)

def setup(bot):
    bot.add_cog(API(bot))
