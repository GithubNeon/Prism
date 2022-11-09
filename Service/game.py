import asyncio
from Modul import *

import nextcord
from nextcord import *
from nextcord.utils import get
from nextcord.ext import commands

from random import randrange
import random

class Game(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @nextcord.slash_command(name="주사위", description="1부터 6까지의 숫자들중 랜덤하게 뽑혀서 봇과 이기면 되는 게임입니다")
    async def 주사위(self, interaction : nextcord.Interaction):
        await interaction.response.defer()
        await interaction.followup.send("🎲 주사위를 굴립니다.")
        a=random.randrange(1,6)
        b=random.randrange(1,6)
        if a < b:
            await asyncio.sleep(2)
            embed=nextcord.Embed(title="🎲 주사위 게임 결과", color=0x00FF56)
            embed.add_field(name=f"프리즘의 숫자", value="🎲 " + str(a))
            embed.add_field(name=f"{interaction.user.name}님의 숫자", value="🎲 " + str(b))
            embed.set_footer(text="결과 : 승리")
            await interaction.followup.send(embed=embed)
        elif a==b:
            await asyncio.sleep(2)
            embed=nextcord.Embed(title="🎲 주사위 게임 결과", color=0xFAFA00)
            embed.add_field(name=f"프리즘의 숫자", value="🎲 " + str(a))
            embed.add_field(name=f"{interaction.user.name}님의 숫자", value="🎲 " + str(b))
            embed.set_footer(text="결과 : 무승부")
            await interaction.followup.send(embed=embed)
        elif a > b:
            await asyncio.sleep(2)
            embed=nextcord.Embed(title="🎲 주사위 게임 결과", color=0xFF0000)
            embed.add_field(name=f"프리즘의 숫자", value="🎲 " + str(a))
            embed.add_field(name=f"{interaction.user.name}님의 숫자", value="🎲 " + str(b))
            embed.set_footer(text="결과 : 패배")
            await interaction.followup.send(embed=embed)

    @nextcord.slash_command(name="매치주사위", description="1부터 6까지의 숫자들중 랜덤하게 뽑혀서 두 숫자가 같은 숫자면 이기는 게임입니다")
    async def 매치주사위(self, interaction : nextcord.Interaction):
        await interaction.response.defer()
        await interaction.followup.send("🎲 주사위를 굴립니다.")
        a=random.randrange(1,6)
        b=random.randrange(1,6)
        if a < b:
            await asyncio.sleep(2)
            embed=nextcord.Embed(title="🎲 매치주사위 게임 결과", color=0xFF0000)
            embed.add_field(name=f"숫자 1", value="🎲 " + str(a))
            embed.add_field(name=f"숫자 2", value="🎲 " + str(b))
            embed.set_footer(text="결과 : 실패")
            await interaction.followup.send(embed=embed)
        elif a==b:
            await asyncio.sleep(2)
            embed=nextcord.Embed(title="🎲 매치주사위 게임 결과", color=0x00FF56)
            embed.add_field(name=f"숫자 1", value="🎲 " + str(a))
            embed.add_field(name=f"숫자 2", value="🎲 " + str(b))
            embed.set_footer(text="결과 : 성공")
            await interaction.followup.send(embed=embed)
        elif a > b:
            await asyncio.sleep(2)
            embed=nextcord.Embed(title="🎲 매치주사위 게임 결과", color=0xFF0000)
            embed.add_field(name=f"숫자 1", value="🎲 " + str(a))
            embed.add_field(name=f"숫자 2", value="🎲 " + str(b))
            embed.set_footer(text="결과 : 실패")
            await interaction.followup.send(embed=embed)

    @nextcord.slash_command(name="가위바위보", description="프리즘과 가위바위보를 합니다")
    async def 가위바위보(self, interaction : nextcord.Interaction, 가위바위보 : str=SlashOption(description="가위, 바위, 보 중에서 골라주세요", choices=rspList)):
        await interaction.response.defer()
        await interaction.followup.send("가위바위보!")
        bot_rsp=str(random.choice(rspList))
        if bot_rsp==가위바위보:
            await asyncio.sleep(2)
            embed=nextcord.Embed(title="가위바위보 게임 결과", color=0xFAFA00)
            embed.add_field(name=f"프리즘이 낸 가위바위보", value=f"{bot_rsp}")
            embed.add_field(name=f"{interaction.user.name}님이 낸 가위바위보", value=f"{가위바위보}")
            embed.set_footer(text="결과 : 무승부")
            await interaction.followup.send(embed=embed)
        elif (bot_rsp=="가위" and 가위바위보=="바위") or (bot_rsp=="보" and 가위바위보=="가위") or (bot_rsp=="바위" and 가위바위보=="보"):
            await asyncio.sleep(2)
            embed=nextcord.Embed(title="가위바위보 게임 결과", color=0x00FF56)
            embed.add_field(name=f"프리즘이 낸 가위바위보", value=f"{bot_rsp}")
            embed.add_field(name=f"{interaction.user.name}님이 낸 가위바위보", value=f"{가위바위보}")
            embed.set_footer(text="결과 : 승리")
            await interaction.followup.send(embed=embed)
        elif (bot_rsp=="바위" and 가위바위보=="가위") or (bot_rsp=="가위" and 가위바위보=="보") or (bot_rsp=="보" and 가위바위보=="바위"):
            await asyncio.sleep(2)
            embed=nextcord.Embed(title="가위바위보 게임 결과", color=0xFF0000)
            embed.add_field(name=f"프리즘이 낸 가위바위보", value=f"{bot_rsp}")
            embed.add_field(name=f"{interaction.user.name}님이 낸 가위바위보", value=f"{가위바위보}")
            embed.set_footer(text="결과 : 패배")
            await interaction.followup.send(embed=embed)

    @nextcord.slash_command(name="니트로선물하기", description="ㅋㅋ")
    async def 니트로선물하기(self, interaction : nextcord.Interaction, 유저 : nextcord.Member=SlashOption(description="놀릴 유저를 선택하세요")):
        await interaction.response.defer()
        await interaction.followup.send(f"{멤버.mention}", embed=nextcord.Embed(title="니트로 선물!", description=f"{interaction.user.mention}님이 {멤버.mention}님에게 니트로를 선물해주셨어요", color=0x2f3136), view=joke(jokeuser=멤버))

class joke(nextcord.ui.View):
    def __init__(self, jokeuser : nextcord.Member=None):
        super().__init__(timeout=None)
        self.jokeuser=jokeuser

    @nextcord.ui.button(label="받기", style=nextcord.ButtonStyle.primary)
    async def 받기(self, button : nextcord.ui.button, interaction : nextcord.Interaction):
        if interaction.user==self.jokeuser:
            await interaction.response.send_message(embed=nextcord.Embed(title="니트로 선물!", description="여친또는 남친부터 만들고 오세요!!", color=0x2f3136), ephemeral=True)
        else:
            await interaction.response.send_message(f"{interaction.user.name}님은 니트로 선물 대상이 아닙니다!", ephemeral=True)

def setup(bot):
    bot.add_cog(Game(bot))
