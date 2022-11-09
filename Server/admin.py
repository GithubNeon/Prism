import asyncio
from Modul import *

import nextcord
from nextcord import *
from nextcord.utils import get
from nextcord.ext import commands

from datetime import *
from time import *
import datetime, time, pytz, humanfriendly

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @nextcord.slash_command(name="추방", description="유저를 서버에서 추방합니다")
    async def 추방(self, interaction : nextcord.Interaction, 유저 : nextcord.Member=SlashOption(description="유저 선택"), 사유 : str=SlashOption(description="추방 사유")):
        await interaction.response.defer()
        if interaction.user.guild_permissions.kick_members:
            await 유저.kick()
            embed=nextcord.Embed(title=f"• {유저.name}님을 {interaction.guild.name} 서버에서 추방했습니다.", description=f"**• 사유 : {사유}**", color=0x2f3136)
            embed.add_field(name="• 디스코드 닉네임", value=f"{유저}", inline=True)
            embed.add_field(name="• 디스코드 ID", value=f"{유저.id}", inline=True)
            embed.set_author(name=f"{유저}", icon_url=f"{유저.avatar}")
            await interaction.followup.send(embed=embed)
        else:
            embed=nextcord.Embed(title="권한 부족", color=0x2f3136)
            embed.add_field(name=f"{interaction.user.name}님, 권한을 얻고 실행시켜 주세요!!\n필요권한 : 유저 추방하기", value="||설마 악용하실려고 하신건 아니죠?||", inline=False)
            await interaction.followup.send(embed=embed, ephemeral=True)

    @nextcord.slash_command(name="차단", description="유저를 서버에서 차단합니다")
    async def 차단(self, interaction : nextcord.Interaction, 유저 : nextcord.Member=SlashOption(description="유저 선택"), 사유 : str=SlashOption(description="차단 사유")):
        await interaction.response.defer()
        if interaction.user.guild_permissions.ban_members:
            await 유저.ban()
            embed=nextcord.Embed(title=f"• {유저.name}님을 {interaction.guild.name} 서버에서 차단했습니다.", description=f"**• 사유 : {사유}**",color=0x2f3136)
            embed.add_field(name="• 디스코드 닉네임", value=f"{유저}", inline=True)
            embed.add_field(name="• 디스코드 ID", value=f"{유저.id}", inline=True)
            embed.set_author(name=f"{유저}", icon_url=f"{유저.avatar}")
            await interaction.followup.send(embed=embed)
        else:
            embed=nextcord.Embed(title="권한 부족", color=0x2f3136)
            embed.add_field(name=f"{interaction.user.name}님, 권한을 얻고 실행시켜 주세요!!\n필요권한 : 유저 차단하기", value="||설마 악용하실려고 하신건 아니죠?||", inline=False)
            await interaction.followup.send(embed=embed, ephemeral=True)

    @nextcord.slash_command(name="청소", description="메세지를 삭제합니다")
    async def 청소(self, interaction : nextcord.Interaction, 갯수 : int=SlashOption(description="삭제할 메세지 갯수")):
        await interaction.response.defer()
        if interaction.user.guild_permissions.manage_messages:
            await interaction.channel.purge(limit=갯수 + 1)
            embed=nextcord.Embed(title=f"• {갯수}개의 메시지를 삭제했습니다.", color=0x2f3136)
            embed.set_author(name=f"{interaction.user}", icon_url=f"{interaction.user.avatar}")
            await interaction.followup.send(embed=embed, delete_after=5)
        else:
            embed=nextcord.Embed(title="권한 부족", color=0x2f3136)
            embed.add_field(name=f"{interaction.user.name}님, 권한을 얻고 실행시켜 주세요!!\n필요권한 : 채널 관리하기", value="||설마 악용하실려고 하신건 아니죠?||", inline=False)
            await interaction.followup.send(embed=embed, ephemeral=True)

    @nextcord.slash_command(name="슬로우", description="해당 채널에 슬로우를 설정합니다")
    async def 슬로우(self, interaction : nextcord.Interaction, 시간 : int=SlashOption(description="채널 슬로우 시간")):
        await interaction.response.defer()
        if interaction.user.guild_permissions.manage_channels:
            if int(시간) > 21600:
                await interaction.followup.send(f"{interaction.user.name}님, 0~21600초 사이로 정해주세요!!", ephemeral=True)
                raise commands.BadArgument
            else:
                await interaction.channel.edit(slowmode_delay=int(시간))
                embed=nextcord.Embed(title=f"• 채널 슬로우 모드를 {시간}초로 설정했습니다.", color=0x2f3136)
                embed.set_author(name=f"{interaction.user}", icon_url=f"{interaction.user.avatar}")
                await interaction.followup.send(embed=embed)
        else:
            embed=nextcord.Embed(title="권한 부족", color=0x2f3136)
            embed.add_field(name=f"{interaction.user.name}님, 권한을 얻고 실행시켜 주세요!!\n필요권한 : 채널 관리하기", value="||설마 악용하실려고 하신건 아니죠?||", inline=False)
            await interaction.followup.send(embed=embed, ephemeral=True)

    @nextcord.slash_command(name="타임아웃", description="유저를 타임아웃 합니다")
    async def 타임아웃(self, interaction : nextcord.Interaction, 유저 : nextcord.Member=SlashOption(description="유저 선택"), 시간 : str=SlashOption(description="타임아웃 시간"), 사유 : str=SlashOption(description="타임아웃 사유")):
        await interaction.response.defer()
        if interaction.user.guild_permissions.moderate_members:
            try:
                int(시간)
                시간=str(시간)+"초"
            except:
                pass
            기간=str(시간).replace("초","s").replace("분","m").replace("시간","h").replace("일","d").replace("주일","w").replace("주","w").replace("년","y")
            time=humanfriendly.parse_timespan(기간)
            print(time)

            max_time=2419200.0
            if time > max_time:
                time=max_time
                시간="28일"
            
            await 유저.edit(timeout=utils.utcnow() + datetime.timedelta(seconds=time))
            await interaction.followup.send(embed=nextcord.Embed(title=f"• {유저.name}님을 {시간}동안 타임아웃 했습니다", description=f"\n**• 사유 : {사유}**", color=0x2f3136))
        else:
            embed=nextcord.Embed(title="권한 부족", color=0x2f3136)
            embed.add_field(name=f"{interaction.user.name}님, 권한을 얻고 실행시켜 주세요!!\n필요권한 : 타임아웃 유저", value="||설마 악용하실려고 하신건 아니죠?||", inline=False)
            await interaction.followup.send(embed=embed, ephemeral=True)

    @nextcord.slash_command(name="역할", description="유저에게 역할을 추가/제거 합니다")
    async def 역할(self, interaction : nextcord.Interaction, 유저 : nextcord.Member=SlashOption(description="유저 선택"), 방법 : str=SlashOption(description="추가/제거", choices=["추가", "제거"]), 역할 : nextcord.Role=SlashOption(description="역할 선택")):
        await interaction.response.defer()
        if interaction.user.guild_permissions.manage_roles:
            if 방법=="추가":
                role=nextcord.utils.get(interaction.guild.roles, name=역할.name)
                await 유저.add_roles(role)
                await interaction.followup.send(embed=nextcord.Embed(description=f"{유저.mention}님에게 {역할.mention} 역할을 추가했습니다", color=0x2f3136))
            elif 방법=="제거":
                role=nextcord.utils.get(interaction.guild.roles, name=역할.name)
                await 유저.remove_roles(role)
                await interaction.followup.send(embed=nextcord.Embed(description=f"{유저.mention}님에게 {역할.mention} 역할을 제거했습니다", color=0x2f3136))
        else:
            embed=nextcord.Embed(title="권한 부족", color=0x2f3136)
            embed.add_field(name=f"{interaction.user.name}님, 권한을 얻고 실행시켜 주세요!!\n필요권한 : 역할 관리하기", value="||설마 악용하실려고 하신건 아니죠?||", inline=False)
            await interaction.followup.send(embed=embed, ephemeral=True)

def setup(bot):
    bot.add_cog(Admin(bot))
