import asyncio
from Modul import *

import nextcord
from nextcord import *
from nextcord.utils import get
from nextcord.ext import commands

import datetime, time, pytz, yarl, func
from datetime import *
from yarl import *
from time import *
from func import emojis

class Vote(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @nextcord.slash_command(name="찬반투표", description="찬반투표 기능입니다")
    async def 찬반투표(self, interaction : nextcord.Interaction, 투표주제 : str=SlashOption(description="투표 주제를 적어주세요")):
        embed=nextcord.Embed(title=f"📋 투표주제 : {투표주제}", description=f"{emojis.good()} | 0표\n{emojis.bad()} | 0표", color=0x2f3136)
        await interaction.response.send_message(embed=embed, view=vote1(title=투표주제, admin=interaction.user))

    @nextcord.slash_command(name="투표", description="투표 기능입니다")
    async def 투표(self, interaction : nextcord.Interaction, 투표주제 : str=SlashOption(description="투표 주제를 적어주세요"),
    항목1 : str=SlashOption(description="항목1번"),
    항목2 : str=SlashOption(description="항목2번"),
    항목3 : str=SlashOption(description="항목3번", required=False),
    항목4 : str=SlashOption(description="항목4번", required=False),
    항목5 : str=SlashOption(description="항목5번", required=False)):
        if 항목3 is None:
            embed=nextcord.Embed(title=f"📋 투표주제 : {투표주제}", description=f"{emojis.one()} {항목1} | 0표\n{emojis.two()} {항목2} | 0표", color=0x2f3136)
            await interaction.response.send_message(embed=embed, view=vote2(title=투표주제, admin=interaction.user, vone=항목1, vtwo=항목2))
        elif 항목4 is None:
            embed=nextcord.Embed(title=f"📋 투표주제 : {투표주제}", description=f"{emojis.one()} {항목1} | 0표\n{emojis.two()} {항목2} | 0표\n{emojis.three()} {항목3} | 0표", color=0x2f3136)
            await interaction.response.send_message(embed=embed, view=vote3(title=투표주제, admin=interaction.user, vone=항목1, vtwo=항목2, vthree=항목3))
        elif 항목5 is None:
            embed=nextcord.Embed(title=f"📋 투표주제 : {투표주제}", description=f"{emojis.one()} {항목1} | 0표\n{emojis.two()} {항목2} | 0표\n{emojis.three()} {항목3} | 0표\n{emojis.four()} {항목4} | 0표", color=0x2f3136)
            await interaction.response.send_message(embed=embed, view=vote4(title=투표주제, admin=interaction.user, vone=항목1, vtwo=항목2, vthree=항목3, vfour=항목4))
        else:
            embed=nextcord.Embed(title=f"📋 투표주제 : {투표주제}", description=f"{emojis.one()} {항목1} | 0표\n{emojis.two()} {항목2} | 0표\n{emojis.three()} {항목3} | 0표\n{emojis.four()} {항목4} | 0표\n{emojis.five()} {항목5} | 0표", color=0x2f3136)
            await interaction.response.send_message(embed=embed, view=vote5(title=투표주제, admin=interaction.user, vone=항목1, vtwo=항목2, vthree=항목3, vfour=항목4, vfive=항목5))

class vote1(nextcord.ui.View):
    def __init__(self, title=None, admin : nextcord.Member=None):
        super().__init__(timeout=None)
        self.title=title
        self.admin=admin
        self.yesALL=[]
        self.noALL=[]

    @nextcord.ui.button(emoji=f"{emojis.good()} ", style=nextcord.ButtonStyle.green)
    async def yes(self, button : nextcord.ui.Button, interaction : nextcord.Interaction):
        if ((interaction.user.id in self.yesALL)==False):
            try:self.noALL.remove(interaction.user.id)
            except:pass

            try:self.yesALL.append(interaction.user.id)
            except:pass

            description=f"{emojis.good()} | {len(self.yesALL)}표\n{emojis.bad()} | {len(self.noALL)}표"
            embed=nextcord.Embed(title=f"📋 투표주제 : {self.title}", description=description, color=0x2f3136)
            await interaction.response.edit_message(embed=embed)
        else:
            await interaction.response.send_message(f"이미 {emojis.good()} 에 투표를 하였습니다", ephemeral=True)

    @nextcord.ui.button(emoji=f"{emojis.bad()}", style=nextcord.ButtonStyle.red)
    async def no(self, button : nextcord.ui.Button, interaction : nextcord.Interaction):
        if ((interaction.user.id in self.noALL)==False):
            try:self.noALL.append(interaction.user.id)
            except:pass

            try:self.yesALL.remove(interaction.user.id)
            except:pass

            description=f"{emojis.good()} | {len(self.yesALL)}표\n{emojis.bad()} | {len(self.noALL)}표"
            embed=nextcord.Embed(title=f"📋 투표주제 : {self.title}", description=description, color=0x2f3136)
            await interaction.response.edit_message(embed=embed)
        else:
            await interaction.response.send_message(f"이미 {emojis.bad()}에 투표를 하였습니다", ephemeral=True)
    
    @nextcord.ui.button(emoji=f"{emojis.lock()}", style=nextcord.ButtonStyle.gray)
    async def end(self, button : nextcord.ui.Button, interaction : nextcord.Interaction):
        if interaction.user==self.admin:
            # super().__init__(timeout=0)


            self.clear_items()
            self.add_item(nextcord.ui.Button(emoji=f"{emojis.good()} ", style=nextcord.ButtonStyle.green, disabled=True))
            self.add_item(nextcord.ui.Button(emoji=f"{emojis.bad()}", style=nextcord.ButtonStyle.red, disabled=True))
            self.add_item(nextcord.ui.Button(emoji=f"{emojis.lock()}", style=nextcord.ButtonStyle.gray, disabled=True))

            # self.dis=0
            description=f"**최종 결과**\n{emojis.good()} | {len(self.yesALL)}표\n{emojis.bad()} | {len(self.noALL)}표"
            embed=nextcord.Embed(title=f"📋 투표주제 : {self.title}", description=description, color=0x2f3136).set_footer(text="투표가 종료되었습니다")
            await interaction.response.edit_message(embed=embed, view=self)
            del self
        else:
            await interaction.response.send_message("투표를 만든사람만 끝낼수 있습니다", ephemeral=True)

class vote2(nextcord.ui.View):
    def __init__(self, title=None, admin : nextcord.Member=None, vone=None, vtwo=None):
        super().__init__(timeout=None)
        self.title=title
        self.admin=admin
        self.vone=vone
        self.vtwo=vtwo
        self.voting1=[]
        self.voting2=[]

    @nextcord.ui.button(emoji=f"{emojis.one()}", style=nextcord.ButtonStyle.blurple)
    async def voting21(self, button : nextcord.ui.Button, interaction : nextcord.Interaction):
        if ((interaction.user.id in self.voting1)==False):
            try:self.voting1.append(interaction.user.id)
            except:pass

            try:self.voting2.remove(interaction.user.id)
            except:pass

            description=f"{emojis.one()} {self.vone} | {len(self.voting1)}표\n{emojis.two()} {self.vtwo} | {len(self.voting2)}표"
            embed=nextcord.Embed(title=f"📋 투표주제 : {self.title}", description=description, color=0x2f3136)
            await interaction.response.edit_message(embed=embed)
        else:
            await interaction.response.send_message(f"이미 {emojis.one()}에 투표를 하였습니다", ephemeral=True)

    @nextcord.ui.button(emoji=f"{emojis.two()}", style=nextcord.ButtonStyle.blurple)
    async def voting22(self, button : nextcord.ui.Button, interaction : nextcord.Interaction):
        if ((interaction.user.id in self.voting2)==False):
            try:self.voting2.append(interaction.user.id)
            except:pass

            try:self.voting1.remove(interaction.user.id)
            except:pass

            description=f"{emojis.one()} {self.vone} | {len(self.voting1)}표\n{emojis.two()} {self.vtwo} | {len(self.voting2)}표"
            embed=nextcord.Embed(title=f"📋 투표주제 : {self.title}", description=description, color=0x2f3136)
            await interaction.response.edit_message(embed=embed)
        else:
            await interaction.response.send_message(f"이미 {emojis.two()}에 투표를 하였습니다", ephemeral=True)

    @nextcord.ui.button(emoji=f"{emojis.lock()}", style=nextcord.ButtonStyle.gray)
    async def end(self, button : nextcord.ui.Button, interaction : nextcord.Interaction):
        if interaction.user==self.admin:
            # super().__init__(timeout=0)

            self.clear_items()
            self.add_item(nextcord.ui.Button(emoji=f"{emojis.one()}", style=nextcord.ButtonStyle.blurple, disabled=True))
            self.add_item(nextcord.ui.Button(emoji=f"{emojis.two()}", style=nextcord.ButtonStyle.blurple, disabled=True))
            self.add_item(nextcord.ui.Button(emoji=f"{emojis.lock()}", style=nextcord.ButtonStyle.gray, disabled=True))

            # self.dis=0
            description=f"**최종 결과**\n{emojis.one()} {self.vone} | {len(self.voting1)}표\n{emojis.two()} {self.vtwo} | {len(self.voting2)}표"
            embed=nextcord.Embed(title=f"📋 투표주제 : {self.title}", description=description, color=0x2f3136).set_footer(text="투표가 종료되었습니다")
            await interaction.response.edit_message(embed=embed, view=self)
            del self
        else:
            await interaction.response.send_message("투표를 만든사람만 끝낼수 있습니다", ephemeral=True)

class vote3(nextcord.ui.View):
    def __init__(self, title=None, admin : nextcord.Member=None, vone=None, vtwo=None, vthree=None):
        super().__init__(timeout=None)
        self.title=title
        self.admin=admin
        self.vone=vone
        self.vtwo=vtwo
        self.vthree=vthree
        self.voting1=[]
        self.voting2=[]
        self.voting3=[]

    @nextcord.ui.button(emoji=f"{emojis.one()}", style=nextcord.ButtonStyle.blurple)
    async def voting31(self, button : nextcord.ui.Button, interaction : nextcord.Interaction):
        if ((interaction.user.id in self.voting1)==False):
            try:self.voting1.append(interaction.user.id)
            except:pass

            try:self.voting2.remove(interaction.user.id)
            except:pass

            try:self.voting3.remove(interaction.user.id)
            except:pass

            description=f"{emojis.one()} {self.vone} | {len(self.voting1)}표\n{emojis.two()} {self.vtwo} | {len(self.voting2)}표\n{emojis.three()} {self.vthree} | {len(self.voting3)}표"
            embed=nextcord.Embed(title=f"📋 투표주제 : {self.title}", description=description, color=0x2f3136)
            await interaction.response.edit_message(embed=embed)
        else:
            await interaction.response.send_message(f"이미 {emojis.one()}에 투표를 하였습니다", ephemeral=True)

    @nextcord.ui.button(emoji=f"{emojis.two()}", style=nextcord.ButtonStyle.blurple)
    async def voting32(self, button : nextcord.Button, interaction : nextcord.Interaction):
        if ((interaction.user.id in self.voting2)==False):
            try:self.voting2.append(interaction.user.id)
            except:pass

            try:self.voting1.remove(interaction.user.id)
            except:pass

            try:self.voting3.remove(interaction.user.id)
            except:pass

            description=f"{emojis.one()} {self.vone} | {len(self.voting1)}표\n{emojis.two()} {self.vtwo} | {len(self.voting2)}표\n{emojis.three()} {self.vthree} | {len(self.voting3)}표"
            embed=nextcord.Embed(title=f"📋 투표주제 : {self.title}", description=description, color=0x2f3136)
            await interaction.response.edit_message(embed=embed)
        else:
            await interaction.response.send_message(f"이미 {emojis.two()}에 투표를 하였습니다", ephemeral=True)

    @nextcord.ui.button(emoji=f"{emojis.three()}", style=nextcord.ButtonStyle.blurple)
    async def voting33(self, button : nextcord.Button, interaction : nextcord.Interaction):
        if ((interaction.user.id in self.voting3)==False):
            try:self.voting3.append(interaction.user.id)
            except:pass

            try:self.voting1.remove(interaction.user.id)
            except:pass

            try:self.voting2.remove(interaction.user.id)
            except:pass

            description=f"{emojis.one()} {self.vone} | {len(self.voting1)}표\n{emojis.two()} {self.vtwo} | {len(self.voting2)}표\n{emojis.three()} {self.vthree} | {len(self.voting3)}표"
            embed=nextcord.Embed(title=f"📋 투표주제 : {self.title}", description=description, color=0x2f3136)
            await interaction.response.edit_message(embed=embed)
        else:
            await interaction.response.send_message(f"이미 {emojis.three()}에 투표를 하였습니다", ephemeral=True)

    @nextcord.ui.button(emoji=f"{emojis.lock()}", style=nextcord.ButtonStyle.gray)
    async def end(self, button : nextcord.ui.Button, interaction : nextcord.Interaction):
        if interaction.user==self.admin:
            # super().__init__(timeout=0)

            self.clear_items()
            self.add_item(nextcord.ui.Button(emoji=f"{emojis.one()}", style=nextcord.ButtonStyle.blurple, disabled=True))
            self.add_item(nextcord.ui.Button(emoji=f"{emojis.two()}", style=nextcord.ButtonStyle.blurple, disabled=True))
            self.add_item(nextcord.ui.Button(emoji=f"{emojis.three()}", style=nextcord.ButtonStyle.blurple, disabled=True))
            self.add_item(nextcord.ui.Button(emoji=f"{emojis.lock()}", style=nextcord.ButtonStyle.gray, disabled=True))

            # self.dis=0
            description=f"**최종 결과**\n{emojis.one()} {self.vone} | {len(self.voting1)}표\n{emojis.two()} {self.vtwo} | {len(self.voting2)}표\n{emojis.three()} {self.vthree} | {len(self.voting3)}표"
            embed=nextcord.Embed(title=f"📋 투표주제 : {self.title}", description=description, color=0x2f3136).set_footer(text="투표가 종료되었습니다")
            await interaction.response.edit_message(embed=embed, view=self)
            del self
        else:
            await interaction.response.send_message("투표를 만든사람만 끝낼수 있습니다", ephemeral=True)

class vote4(nextcord.ui.View):
    def __init__(self, title=None, admin : nextcord.Member=None, vone=None, vtwo=None, vthree=None, vfour=None):
        super().__init__(timeout=None)
        self.title=title
        self.admin=admin
        self.vone=vone
        self.vtwo=vtwo
        self.vthree=vthree
        self.vfour=vfour
        self.voting1=[]
        self.voting2=[]
        self.voting3=[]
        self.voting4=[]

    @nextcord.ui.button(emoji=f"{emojis.one()}", style=nextcord.ButtonStyle.blurple)
    async def voting41(self, button : nextcord.ui.Button, interaction : nextcord.Interaction):
        if ((interaction.user.id in self.voting1)==False):
            try:self.voting1.append(interaction.user.id)
            except:pass

            try:self.voting2.remove(interaction.user.id)
            except:pass

            try:self.voting3.remove(interaction.user.id)
            except:pass

            try:self.voting4.remove(interaction.user.id)
            except:pass

            description=f"{emojis.one()} {self.vone} | {len(self.voting1)}표\n{emojis.two()} {self.vtwo} | {len(self.voting2)}표\n{emojis.three()} {self.vthree} | {len(self.voting3)}표\n{emojis.four()} {self.vfour} | {len(self.voting4)}표"
            embed=nextcord.Embed(title=f"📋 투표주제 : {self.title}", description=description, color=0x2f3136)
            await interaction.response.edit_message(embed=embed)
        else:
            await interaction.response.send_message(f"이미 {emojis.one()}에 투표를 하였습니다", ephemeral=True)

    @nextcord.ui.button(emoji=f"{emojis.two()}", style=nextcord.ButtonStyle.blurple)
    async def voting42(self, button : nextcord.Button, interaction : nextcord.Interaction):
        if ((interaction.user.id in self.voting2)==False):
            try:self.voting2.append(interaction.user.id)
            except:pass

            try:self.voting1.remove(interaction.user.id)
            except:pass

            try:self.voting3.remove(interaction.user.id)
            except:pass

            try:self.voting4.remove(interaction.user.id)
            except:pass

            description=f"{emojis.one()} {self.vone} | {len(self.voting1)}표\n{emojis.two()} {self.vtwo} | {len(self.voting2)}표\n{emojis.three()} {self.vthree} | {len(self.voting3)}표\n{emojis.four()} {self.vfour} | {len(self.voting4)}표"
            embed=nextcord.Embed(title=f"📋 투표주제 : {self.title}", description=description, color=0x2f3136)
            await interaction.response.edit_message(embed=embed)
        else:
            await interaction.response.send_message(f"이미 {emojis.two()}에 투표를 하였습니다", ephemeral=True)

    @nextcord.ui.button(emoji=f"{emojis.three()}", style=nextcord.ButtonStyle.blurple)
    async def voting43(self, button : nextcord.Button, interaction : nextcord.Interaction):
        if ((interaction.user.id in self.voting3)==False):
            try:self.voting3.append(interaction.user.id)
            except:pass

            try:self.voting1.remove(interaction.user.id)
            except:pass

            try:self.voting2.remove(interaction.user.id)
            except:pass

            try:self.voting4.remove(interaction.user.id)
            except:pass

            description=f"{emojis.one()} {self.vone} | {len(self.voting1)}표\n{emojis.two()} {self.vtwo} | {len(self.voting2)}표\n{emojis.three()} {self.vthree} | {len(self.voting3)}표\n{emojis.four()} {self.vfour} | {len(self.voting4)}표"
            embed=nextcord.Embed(title=f"📋 투표주제 : {self.title}", description=description, color=0x2f3136)
            await interaction.response.edit_message(embed=embed)
        else:
            await interaction.response.send_message(f"이미 {emojis.three()}에 투표를 하였습니다", ephemeral=True)

    @nextcord.ui.button(emoji=f"{emojis.four()}", style=nextcord.ButtonStyle.blurple)
    async def voting44(self, button : nextcord.Button, interaction : nextcord.Interaction):
        if ((interaction.user.id in self.voting4)==False):
            try:self.voting4.append(interaction.user.id)
            except:pass

            try:self.voting1.remove(interaction.user.id)
            except:pass

            try:self.voting2.remove(interaction.user.id)
            except:pass

            try:self.voting3.remove(interaction.user.id)
            except:pass

            description=f"{emojis.one()} {self.vone} | {len(self.voting1)}표\n{emojis.two()} {self.vtwo} | {len(self.voting2)}표\n{emojis.three()} {self.vthree} | {len(self.voting3)}표\n{emojis.four()} {self.vfour} | {len(self.voting4)}표"
            embed=nextcord.Embed(title=f"📋 투표주제 : {self.title}", description=description, color=0x2f3136)
            await interaction.response.edit_message(embed=embed)
        else:
            await interaction.response.send_message(f"이미 {emojis.four()}에 투표를 하였습니다", ephemeral=True)

    @nextcord.ui.button(emoji=f"{emojis.lock()}", style=nextcord.ButtonStyle.gray)
    async def end(self, button : nextcord.ui.Button, interaction : nextcord.Interaction):
        if interaction.user==self.admin:
            # super().__init__(timeout=0)

            self.clear_items()
            self.add_item(nextcord.ui.Button(emoji=f"{emojis.one()}", style=nextcord.ButtonStyle.blurple, disabled=True))
            self.add_item(nextcord.ui.Button(emoji=f"{emojis.two()}", style=nextcord.ButtonStyle.blurple, disabled=True))
            self.add_item(nextcord.ui.Button(emoji=f"{emojis.three()}", style=nextcord.ButtonStyle.blurple, disabled=True))
            self.add_item(nextcord.ui.Button(emoji=f"{emojis.four()}", style=nextcord.ButtonStyle.blurple, disabled=True))
            self.add_item(nextcord.ui.Button(emoji=f"{emojis.lock()}", style=nextcord.ButtonStyle.gray, disabled=True))

            # self.dis=0
            description=f"**최종 결과**\n{emojis.one()} {self.vone} | {len(self.voting1)}표\n{emojis.two()} {self.vtwo} | {len(self.voting2)}표\n{emojis.three()} {self.vthree} | {len(self.voting3)}표\n{emojis.four()} {self.vfour} | {len(self.voting4)}표"
            embed=nextcord.Embed(title=f"📋 투표주제 : {self.title}", description=description, color=0x2f3136).set_footer(text="투표가 종료되었습니다")
            await interaction.response.edit_message(embed=embed, view=self)
            del self
        else:
            await interaction.response.send_message("투표를 만든사람만 끝낼수 있습니다", ephemeral=True)

class vote5(nextcord.ui.View):
    def __init__(self, title=None, admin : nextcord.Member=None, vone=None, vtwo=None, vthree=None, vfour=None, vfive=None):
        super().__init__(timeout=None)
        self.title=title
        self.admin=admin
        self.vone=vone
        self.vtwo=vtwo
        self.vthree=vthree
        self.vfour=vfour
        self.vfive=vfive
        self.voting1=[]
        self.voting2=[]
        self.voting3=[]
        self.voting4=[]
        self.voting5=[]

    @nextcord.ui.button(emoji=f"{emojis.one()}", style=nextcord.ButtonStyle.blurple)
    async def voting51(self, button : nextcord.ui.Button, interaction : nextcord.Interaction):
        if ((interaction.user.id in self.voting1)==False):
            try:self.voting1.append(interaction.user.id)
            except:pass

            try:self.voting2.remove(interaction.user.id)
            except:pass

            try:self.voting3.remove(interaction.user.id)
            except:pass

            try:self.voting4.remove(interaction.user.id)
            except:pass

            try:self.voting5.remove(interaction.user.id)
            except:pass

            description=f"{emojis.one()} {self.vone} | {len(self.voting1)}표\n{emojis.two()} {self.vtwo} | {len(self.voting2)}표\n{emojis.three()} {self.vthree} | {len(self.voting3)}표\n{emojis.four()} {self.vfour} | {len(self.voting4)}표\n{emojis.five()} {self.vfive} | {len(self.voting5)}표"
            embed=nextcord.Embed(title=f"📋 투표주제 : {self.title}", description=description, color=0x2f3136)
            await interaction.response.edit_message(embed=embed)
        else:
            await interaction.response.send_message(f"이미 {emojis.one()}에 투표를 하였습니다", ephemeral=True)

    @nextcord.ui.button(emoji=f"{emojis.two()}", style=nextcord.ButtonStyle.blurple)
    async def voting52(self, button : nextcord.Button, interaction : nextcord.Interaction):
        if ((interaction.user.id in self.voting2)==False):
            try:self.voting2.append(interaction.user.id)
            except:pass

            try:self.voting1.remove(interaction.user.id)
            except:pass

            try:self.voting3.remove(interaction.user.id)
            except:pass

            try:self.voting4.remove(interaction.user.id)
            except:pass

            try:self.voting5.remove(interaction.user.id)
            except:pass

            description=f"{emojis.one()} {self.vone} | {len(self.voting1)}표\n{emojis.two()} {self.vtwo} | {len(self.voting2)}표\n{emojis.three()} {self.vthree} | {len(self.voting3)}표\n{emojis.four()} {self.vfour} | {len(self.voting4)}표\n{emojis.five()} {self.vfive} | {len(self.voting5)}표"
            embed=nextcord.Embed(title=f"📋 투표주제 : {self.title}", description=description, color=0x2f3136)
            await interaction.response.edit_message(embed=embed)
        else:
            await interaction.response.send_message(f"이미 {emojis.two()}에 투표를 하였습니다", ephemeral=True)

    @nextcord.ui.button(emoji=f"{emojis.three()}", style=nextcord.ButtonStyle.blurple)
    async def voting53(self, button : nextcord.Button, interaction : nextcord.Interaction):
        if ((interaction.user.id in self.voting3)==False):
            try:self.voting3.append(interaction.user.id)
            except:pass

            try:self.voting1.remove(interaction.user.id)
            except:pass

            try:self.voting2.remove(interaction.user.id)
            except:pass

            try:self.voting4.remove(interaction.user.id)
            except:pass

            try:self.voting5.remove(interaction.user.id)
            except:pass

            description=f"{emojis.one()} {self.vone} | {len(self.voting1)}표\n{emojis.two()} {self.vtwo} | {len(self.voting2)}표\n{emojis.three()} {self.vthree} | {len(self.voting3)}표\n{emojis.four()} {self.vfour} | {len(self.voting4)}표\n{emojis.five()} {self.vfive} | {len(self.voting5)}표"
            embed=nextcord.Embed(title=f"📋 투표주제 : {self.title}", description=description, color=0x2f3136)
            await interaction.response.edit_message(embed=embed)
        else:
            await interaction.response.send_message(f"이미 {emojis.three()}에 투표를 하였습니다", ephemeral=True)

    @nextcord.ui.button(emoji=f"{emojis.four()}", style=nextcord.ButtonStyle.blurple)
    async def voting54(self, button : nextcord.Button, interaction : nextcord.Interaction):
        if ((interaction.user.id in self.voting4)==False):
            try:self.voting4.append(interaction.user.id)
            except:pass

            try:self.voting1.remove(interaction.user.id)
            except:pass

            try:self.voting2.remove(interaction.user.id)
            except:pass

            try:self.voting3.remove(interaction.user.id)
            except:pass

            try:self.voting5.remove(interaction.user.id)
            except:pass

            description=f"{emojis.one()} {self.vone} | {len(self.voting1)}표\n{emojis.two()} {self.vtwo} | {len(self.voting2)}표\n{emojis.three()} {self.vthree} | {len(self.voting3)}표\n{emojis.four()} {self.vfour} | {len(self.voting4)}표\n{emojis.five()} {self.vfive} | {len(self.voting5)}표"
            embed=nextcord.Embed(title=f"📋 투표주제 : {self.title}", description=description, color=0x2f3136)
            await interaction.response.edit_message(embed=embed)
        else:
            await interaction.response.send_message(f"이미 {emojis.four()}에 투표를 하였습니다", ephemeral=True)

    @nextcord.ui.button(emoji=f"{emojis.five()}", style=nextcord.ButtonStyle.blurple)
    async def voting55(self, button : nextcord.Button, interaction : nextcord.Interaction):
        if ((interaction.user.id in self.voting5)==False):
            try:self.voting5.append(interaction.user.id)
            except:pass

            try:self.voting1.remove(interaction.user.id)
            except:pass

            try:self.voting2.remove(interaction.user.id)
            except:pass

            try:self.voting3.remove(interaction.user.id)
            except:pass
    
            try:self.voting4.remove(interaction.user.id)
            except:pass

            description=f"{emojis.one()} {self.vone} | {len(self.voting1)}표\n{emojis.two()} {self.vtwo} | {len(self.voting2)}표\n{emojis.three()} {self.vthree} | {len(self.voting3)}표\n{emojis.four()} {self.vfour} | {len(self.voting4)}표\n{emojis.five()} {self.vfive} | {len(self.voting5)}표"
            embed=nextcord.Embed(title=f"📋 투표주제 : {self.title}", description=description, color=0x2f3136)
            await interaction.response.edit_message(embed=embed)
        else:
            await interaction.response.send_message(f"이미 {emojis.five()}에 투표를 하였습니다", ephemeral=True)

    @nextcord.ui.button(emoji=f"{emojis.lock()}", style=nextcord.ButtonStyle.gray)
    async def end(self, button : nextcord.ui.Button, interaction : nextcord.Interaction):
        if interaction.user==self.admin:
            # super().__init__(timeout=0)

            self.clear_items()
            self.add_item(nextcord.ui.Button(emoji=f"{emojis.one()}", style=nextcord.ButtonStyle.blurple, disabled=True))
            self.add_item(nextcord.ui.Button(emoji=f"{emojis.two()}", style=nextcord.ButtonStyle.blurple, disabled=True))
            self.add_item(nextcord.ui.Button(emoji=f"{emojis.three()}", style=nextcord.ButtonStyle.blurple, disabled=True))
            self.add_item(nextcord.ui.Button(emoji=f"{emojis.four()}", style=nextcord.ButtonStyle.blurple, disabled=True))
            self.add_item(nextcord.ui.Button(emoji=f"{emojis.five()}", style=nextcord.ButtonStyle.blurple, disabled=True))
            self.add_item(nextcord.ui.Button(emoji=f"{emojis.lock()}", style=nextcord.ButtonStyle.gray, disabled=True))

            # self.dis=0
            description=f"**최종 결과**\n{emojis.one()} {self.vone} | {len(self.voting1)}표\n{emojis.two()} {self.vtwo} | {len(self.voting2)}표\n{emojis.three()} {self.vthree} | {len(self.voting3)}표\n{emojis.four()} {self.vfour} | {len(self.voting4)}표\n{emojis.five()} {self.vfive} | {len(self.voting5)}표"
            embed=nextcord.Embed(title=f"📋 투표주제 : {self.title}", description=description, color=0x2f3136).set_footer(text="투표가 종료되었습니다")
            await interaction.response.edit_message(embed=embed, view=self)
            del self
        else:
            await interaction.response.send_message("투표를 만든사람만 끝낼수 있습니다", ephemeral=True)

def setup(bot):
    bot.add_cog(Vote(bot))