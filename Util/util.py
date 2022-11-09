import asyncio
from Modul import *

import nextcord
from nextcord import *
from nextcord.utils import get
from nextcord.ext import commands

import datetime, time, pytz, humanfriendly, func
from time import *
from datetime import *
from func import emojis

class Util(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @nextcord.slash_command(name="타이머", description="타이머 기능입니다")
    async def 타이머(self, interaction : nextcord.Interaction, 시간 : int=SlashOption(description="시간을 써주세요"), 단위 : str=SlashOption(description="초, 분, 시간 중에 선택해주세요", choices=["초", "분", "시간"])):
        choice : int={"초" : 1, "분" : 60, "시간" : 3600}[단위]
        await interaction.response.defer()
        await interaction.response.send_message(f"{시간}{단위}뒤에 알람이 울립니다")
        await asyncio.sleep(시간 * choice)
        await interaction.followup.send(f"{interaction.user.mention} 시간이 다 됐습니다")

    @nextcord.slash_command(name="서버정보", description="해당 서버의 정보를 보여줍니다")
    async def 서버정보(self, interaction : nextcord.Interaction):
        await interaction.response.defer()
        bot=0
        for i in range(interaction.guild.member_count):
            if interaction.guild.members[i].bot:
                bot += 1
        embed=nextcord.Embed(title=f"{interaction.guild.name} 서버 정보입니다", color=0x2f3136)
        embed.add_field(name=f"{emojis.owner()} 서버장", value=f"• {interaction.guild.owner.mention}", inline=True)
        embed.add_field(name=f"{emojis.postplus()} 서버 생성일", value="• "+interaction.guild.created_at.strftime(f"20%y년 %m월 %d일"), inline=True)
        embed.add_field(name=f"{emojis.verify()} 서버 인증 단계", value=(str(interaction.guild.verification_level)+" ").replace("none","• 없음").replace("low","• 낮음").replace("medium","• 중간").replace("high","• 높음".replace("highest","• 매우 높음")), inline=True)
        embed.add_field(name=f"{emojis.channel()} 채널 갯수", value=f"• 채팅채널: {len(interaction.guild.text_channels)}개\n• 음성채널: {len(interaction.guild.voice_channels)}개\n• 카테고리: {len(interaction.guild.categories)}개")
        embed.add_field(name=f"{emojis.group()} 서버 인원수", value=f"• 총 인원수: {interaction.guild.member_count}명\n• 봇 인원수: {bot}명\n• 서버 순 인원: {interaction.guild.member_count-bot}명", inline=True)
        embed.add_field(name=f"{emojis.aboost()} 서버 부스트", value=f"• {interaction.guild.premium_tier}레벨\n• {interaction.guild.premium_subscription_count}개", inline=True)
        embed.set_thumbnail(url=f"{interaction.guild.icon}")
        await interaction.followup.send(embed=embed)

    @nextcord.slash_command(name="유저정보", description="디스코드 계정 정보를 알려줍니다")
    async def 유저정보(self, interaction : nextcord.Interaction, 유저 : nextcord.Member=SlashOption(description="멤버 선택", required=False)):
        await interaction.response.defer()
        if 유저 is None:
            date=datetime.utcfromtimestamp(((int(interaction.user.id) >> 22) + 1420070400000) / 1000)
            embed=nextcord.Embed(title=f"{interaction.user.name}", color=0x2f3136)
            embed.add_field(name=f"{emojis.discord()} 디스코드 닉네임", value=f"• {interaction.user}", inline=False)
            embed.add_field(name=f"{emojis.postplus()} 디스코드 가입일", value=f"• {date.year}년 {date.month}월 {date.day}일", inline=False)
            embed.add_field(name=f"{emojis.idcard()} 디스코드 고유 ID", value=f"• {interaction.user.id}", inline=False)
            embed.add_field(name=f"{emojis.settings()} 디스코드 상태", value=(interaction.user.status.name).replace("online","```diff\n+ 온라인\n```").replace("idle","```fix\n자리 비움\n```").replace("dnd","```diff\n- 다른 용무 중\n```").replace("offline","```bf\n오프라인\n```"))
            embed.set_thumbnail(url=f"{interaction.user.avatar}")
            await interaction.followup.send(embed=embed)
        else:
            date=datetime.utcfromtimestamp(((int(유저.id) >> 22) + 1420070400000) / 1000)
            embed=nextcord.Embed(title=f"{유저.name}", color=0x2f3136)
            embed.add_field(name=f"{emojis.discord()} 디스코드 닉네임", value=f"• {유저}", inline=False)
            embed.add_field(name=f"{emojis.postplus()} 디스코드 가입일", value=f"• {date.year}년 {date.month}월 {date.day}일", inline=False)
            embed.add_field(name=f"{emojis.idcard()} 디스코드 고유 ID", value=f"• {유저.id}", inline=False)
            embed.add_field(name=f"{emojis.settings()} 디스코드 상태", value=(유저.status.name).replace("online","```diff\n+ 온라인\n```").replace("idle","```fix\n자리 비움\n```").replace("dnd","```diff\n- 다른 용무 중\n```").replace("offline","```bf\n오프라인\n```"))
            embed.set_thumbnail(url=f"{유저.avatar}")
            await interaction.followup.send(embed=embed)

    @nextcord.slash_command(name="버튼", description="버튼을 만듭니다")
    async def 버튼(self, interaction : nextcord.Interaction,
    이름 : str=SlashOption(description="이름을 적어주세요"),
    색상 : str=SlashOption(description="색상을 선택해주세요", choices=buttonList),
    답장 : str=SlashOption(description="버튼을 눌렀을때의 답장을 입력해주세요"),
    답장보이기 : str=SlashOption(description="답장을 했을때 보일지 안보일지 선택합니다", choices=ynList)):
        choice : str={"파란색" : nextcord.ButtonStyle.blurple, "빨간색" : nextcord.ButtonStyle.red, "회색" : nextcord.ButtonStyle.gray, "초록색" : nextcord.ButtonStyle.green}[색상]
        await interaction.response.defer()
        if 답장보이기=="예":
            button=nextcord.ui.Button(label=이름, style=choice)

            view=nextcord.ui.View()
            view.add_item(button)

            async def button_callback(interaction : nextcord.Interaction):
                await interaction.response.send_message(content=f"{답장}")

            button.callback=button_callback
            await interaction.followup.send(view=view)
        elif 답장보이기=="아니요":
            button=nextcord.ui.Button(label=이름, style=choice)

            view=nextcord.ui.View()
            view.add_item(button)

            async def button_callback(interaction : nextcord.Interaction):
                await interaction.response.send_message(content=f"{답장}", ephemeral=True)

            button.callback=button_callback
            await interaction.followup.send(view=view)

def setup(bot):
    bot.add_cog(Util(bot))