import asyncio
from Modul import *

import nextcord
from nextcord import *
from nextcord.utils import get
from nextcord.ext import commands

import func
from func import emojis

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @nextcord.slash_command(name="명령어", description="프리즘 명령어 목록입니다")
    async def 명령어(self, interaction : nextcord.Interaction, 명령어 : str=SlashOption(description="프리즘 명령어 목록입니다", choices=commandList)): 
        await interaction.response.defer()   
        if 명령어=="서버관리":
            embed=nextcord.Embed(title="서버관리 카테고리", color=0x2f3136)
            embed.add_field(name="• 서버관리 명령어 목록", value="""
```md
# 유저관리

- /추방 <멤버 선택>
> 사용방법 : /추방 네오니

- /차단 <멤버 선택>
> 사용방법 : /차단 네오니

- /타임아웃 <멤버 선택> <시간>
> 사용방법 : /타임아웃 네오니 1시간

- /역할 <유저> <방법> <역할>
> 사용방법 : /역할 네오니 추가 verify
``````md
# 채널관리

- /청소 <삭제할 메세지 갯수>
> 사용방법 : /청소 10

- /슬로우 <시간>
> 사용방법 : /슬로우 10
```""", inline=False)
            await interaction.followup.send(embed=embed, ephemeral=True)
        elif 명령어=="게임":
            embed=nextcord.Embed(title="게임 카테고리", color=0x2f3136)
            embed.add_field(name="• 게임 명령어 목록", value="""
```md
# /주사위
> 사용방법 : /주사위

# /매치주사위 <숫자>
> 사용방법 : /매치주사위 7

# /가위바위보 <가위바위보>
> 사용방법 : /가위바위보 바위

# /니트로선물하기 <멤버>
> 사용방법 : /니트로선물하기 네오니
```""", inline=False)
            await interaction.followup.send(embed=embed, ephemeral=True)
        elif 명령어=="유틸리티":
            embed=nextcord.Embed(title="유틸리티 카테고리", color=0x2f3136)
            embed.add_field(name="• 유틸리티 명령어 목록", value="""
```md
# 정보

- /서버정보
> 사용방법 : /서버정보

- /유저정보 <유저>
> 사용방법 : /유저정보 네오니
``````md
# 투표

- /투표 <투표주제> <항목1> <항목2>...<항목5>
> 사용방법 : /투표 네오니는? 천재다 바보다 겁나쩐다

- /찬반투표 <투표주제>
> 사용방법 : /찬반투표 네오니천재
``````md
# 계산

- /계산기
> 사용방법 : /계산기

- /타이머 <시간> <단위>
> 사용방법 : /타이머 10초, /타이머 10분, /타이머 10시간
``````md
# 버튼

- /버튼 <이름> <색상> <답장> <답장보이기>
> 사용방법 : /버튼 테스트 파란색 이건파란색 아니요
```""", inline=False)
            await interaction.followup.send(embed=embed, ephemeral=True)
        elif 명령어=="API":
            embed=nextcord.Embed(title="API 카테고리", color=0x2f3136)
            embed.add_field(name="• API 명령어 목록", value="""
```md
# /코로나 <지역>
> 사용방법 : /코로나 광주

# /한강
> 사용방법 : /한강

# /마인크래프트 <닉네임>
> 사용방법 : /마인크래프트 mojang

# /강아지
> 사용방법 : /강아지

# /고양이
> 사용방법 : /고양이

# /프리즘 <하고싶은말>
> 사용방법 : /프리즘 여친있어?
```""", inline=False)
            await interaction.followup.send(embed=embed, ephemeral=True)
        elif 명령어=="개발자":
            embed=nextcord.Embed(title="개발자 카테고리", color=0x2f3136)
            embed.add_field(name="• 개발자 명령어 목록", value="""
```md
# 봇

- /개발자
> 사용방법 : /개발자

- /봇정보
> 사용방법 : /봇정보

- /핑
> 사용방법 : /핑
``````md
# DataBase

- /저장하기 <단어> <내용>
> 사용방법 : /저장하기 네오니 천재

- /불러오기 <단어>
> 사용방법 : /불러오기 네오니
```""", inline=False)
            await interaction.followup.send(embed=embed, ephemeral=True)
        elif 명령어=="도움말":
            embed=nextcord.Embed(title="도움말 카테고리", color=0x2f3136)
            embed.add_field(name="• 도움말 명령어 목록", value="""
```md
# /명령어 <카테고리 선택>
> 사용방법 : /명령어 도움말
```""", inline=False)
            await interaction.followup.send(embed=embed, ephemeral=True)

def setup(bot):
    bot.add_cog(Help(bot))