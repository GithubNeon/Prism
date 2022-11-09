import asyncio
from Modul import *

import nextcord
from nextcord import *
from nextcord.utils import get
from nextcord.ext import commands

from math import *

class Calc(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @nextcord.slash_command(name="계산기", description="계산기")
    async def 계산기(self, interaction : nextcord.Interaction):
        await interaction.response.send_message(embed=nextcord.Embed(description="```\n \n```", color=0x2f3136), view=calculator(interaction.user))

async def Calculator(x):
    return eval(str(x).replace("```","").replace("\n","").replace("ㅤ","").replace("×","*").replace("÷","/").replace("²","**2").replace("𝝅","3.141592"))

class calculator(nextcord.ui.View):
    def __init__(self, user):
        super().__init__(timeout=None)
        self.user=user

    @nextcord.ui.button(label="1", style=nextcord.ButtonStyle.gray)
    async def one(self, button : nextcord.ui.Button, interaction : nextcord.Interaction):
        if interaction.user==self.user:
            integer=(str(interaction.message.embeds[0].description).replace("```","").replace("\n","").replace(" ",""))+str(button.label)
            await interaction.message.edit(embed=nextcord.Embed(description=f"```\n{integer}\n```", color=interaction.message.embeds[0].color))
        else:
            await interaction.response.send_message("자신의것을 사용하세요", ephemeral=True)
    
    @nextcord.ui.button(label="2", style=nextcord.ButtonStyle.gray)
    async def two(self, button : nextcord.ui.Button, interaction : nextcord.Interaction):
        if interaction.user==self.user:
            integer=(str(interaction.message.embeds[0].description).replace("```","").replace("\n","").replace(" ",""))+str(button.label)
            await interaction.message.edit(embed=nextcord.Embed(description=f"```\n{integer}\n```", color=interaction.message.embeds[0].color))
        else:
            await interaction.response.send_message("자신의것을 사용하세요", ephemeral=True)
    
    @nextcord.ui.button(label="3", style=nextcord.ButtonStyle.gray)
    async def three(self, button : nextcord.ui.Button, interaction : nextcord.Interaction):
        if interaction.user==self.user:
            integer=(str(interaction.message.embeds[0].description).replace("```","").replace("\n","").replace(" ",""))+str(button.label)
            await interaction.message.edit(embed=nextcord.Embed(description=f"```\n{integer}\n```", color=interaction.message.embeds[0].color))
        else:
            await interaction.response.send_message("자신의것을 사용하세요", ephemeral=True)

    @nextcord.ui.button(label="×", style=nextcord.ButtonStyle.blurple)
    async def x(self, button : nextcord.ui.Button, interaction : nextcord.Interaction):
        if interaction.user==self.user:
            integer=(str(interaction.message.embeds[0].description).replace("```","").replace("\n","").replace(" ",""))+str(button.label)
            await interaction.message.edit(embed=nextcord.Embed(description=f"```\n{integer}\n```", color=interaction.message.embeds[0].color))
        else:
            await interaction.response.send_message("자신의것을 사용하세요", ephemeral=True)

    @nextcord.ui.button(label="끝", style=nextcord.ButtonStyle.red)
    async def end(self, button : nextcord.ui.Button, interaction : nextcord.Interaction):
        if interaction.user==self.user:
            await interaction.message.delete()
        else:
            await interaction.response.send_message("자신의것을 사용하세요", ephemeral=True)

    @nextcord.ui.button(label="4", style=nextcord.ButtonStyle.gray)
    async def four(self, button : nextcord.ui.Button, interaction : nextcord.Interaction):
        if interaction.user==self.user:
            integer=(str(interaction.message.embeds[0].description).replace("```","").replace("\n","").replace(" ",""))+str(button.label)
            await interaction.message.edit(embed=nextcord.Embed(description=f"```\n{integer}\n```", color=interaction.message.embeds[0].color))
        else:
            await interaction.response.send_message("자신의것을 사용하세요", ephemeral=True)
    
    @nextcord.ui.button(label="5", style=nextcord.ButtonStyle.gray)
    async def five(self, button : nextcord.ui.Button, interaction : nextcord.Interaction):
        if interaction.user==self.user:
            integer=(str(interaction.message.embeds[0].description).replace("```","").replace("\n","").replace(" ",""))+str(button.label)
            await interaction.message.edit(embed=nextcord.Embed(description=f"```\n{integer}\n```", color=interaction.message.embeds[0].color))
        else:
            await interaction.response.send_message("자신의것을 사용하세요", ephemeral=True)
    
    @nextcord.ui.button(label="6", style=nextcord.ButtonStyle.gray)
    async def six(self, button : nextcord.ui.Button, interaction : nextcord.Interaction):
        if interaction.user==self.user:
            integer=(str(interaction.message.embeds[0].description).replace("```","").replace("\n","").replace(" ",""))+str(button.label)
            await interaction.message.edit(embed=nextcord.Embed(description=f"```\n{integer}\n```", color=interaction.message.embeds[0].color))
        else:
            await interaction.response.send_message("자신의것을 사용하세요", ephemeral=True)
    
    @nextcord.ui.button(label="÷", style=nextcord.ButtonStyle.blurple)
    async def divide(self, button : nextcord.ui.Button, interaction : nextcord.Interaction):
        if interaction.user==self.user:
            integer=(str(interaction.message.embeds[0].description).replace("```","").replace("\n","").replace(" ",""))+str(button.label)
            await interaction.message.edit(embed=nextcord.Embed(description=f"```\n{integer}\n```", color=interaction.message.embeds[0].color))
        else:
            await interaction.response.send_message("자신의것을 사용하세요", ephemeral=True)
    
    @nextcord.ui.button(label="지우기", style=nextcord.ButtonStyle.red)
    async def delete(self, button : nextcord.ui.Button, interaction : nextcord.Interaction):
        if interaction.user==self.user:
            integer=(str(interaction.message.embeds[0].description).replace("```","").replace("\n","").replace(" ",""))[:len((str(interaction.message.embeds[0].description).replace("```","").replace("\n","")))-1]
            if integer=="":integer=" "
            await interaction.message.edit(embed=nextcord.Embed(description=f"```\n{integer}\n```", color=interaction.message.embeds[0].color))
        else:
            await interaction.response.send_message("자신의것을 사용하세요", ephemeral=True)

    @nextcord.ui.button(label="7", style=nextcord.ButtonStyle.gray)
    async def seven(self, button : nextcord.ui.Button, interaction : nextcord.Interaction):
        if interaction.user==self.user:
            integer=(str(interaction.message.embeds[0].description).replace("```","").replace("\n","").replace(" ",""))+str(button.label)
            await interaction.message.edit(embed=nextcord.Embed(description=f"```\n{integer}\n```", color=interaction.message.embeds[0].color))
        else:
            await interaction.response.send_message("자신의것을 사용하세요", ephemeral=True)
    
    @nextcord.ui.button(label="8", style=nextcord.ButtonStyle.gray)
    async def eight(self, button : nextcord.ui.Button, interaction : nextcord.Interaction):
        if interaction.user==self.user:
            integer=(str(interaction.message.embeds[0].description).replace("```","").replace("\n","").replace(" ",""))+str(button.label)
            await interaction.message.edit(embed=nextcord.Embed(description=f"```\n{integer}\n```", color=interaction.message.embeds[0].color))
        else:
            await interaction.response.send_message("자신의것을 사용하세요", ephemeral=True)
    
    @nextcord.ui.button(label="9", style=nextcord.ButtonStyle.gray)
    async def nine(self, button : nextcord.ui.Button, interaction : nextcord.Interaction):
        if interaction.user==self.user:
            integer=(str(interaction.message.embeds[0].description).replace("```","").replace("\n","").replace(" ",""))+str(button.label)
            await interaction.message.edit(embed=nextcord.Embed(description=f"```\n{integer}\n```", color=interaction.message.embeds[0].color))
        else:
            await interaction.response.send_message("자신의것을 사용하세요", ephemeral=True)
    
    @nextcord.ui.button(label="+", style=nextcord.ButtonStyle.blurple)
    async def plus(self, button : nextcord.ui.Button, interaction : nextcord.Interaction):
        if interaction.user==self.user:
            integer=(str(interaction.message.embeds[0].description).replace("```","").replace("\n","").replace(" ",""))+str(button.label)
            await interaction.message.edit(embed=nextcord.Embed(description=f"```\n{integer}\n```", color=interaction.message.embeds[0].color))
        else:
            await interaction.response.send_message("자신의것을 사용하세요", ephemeral=True)

    @nextcord.ui.button(label="삭제", style=nextcord.ButtonStyle.red)
    async def deleteALL(self, button : nextcord.ui.Button, interaction : nextcord.Interaction):
        if interaction.user==self.user:
            integer=" "
            await interaction.message.edit(embed=nextcord.Embed(description=f"```\n{integer}\n```", color=interaction.message.embeds[0].color))
        else:
            await interaction.response.send_message("자신의것을 사용하세요", ephemeral=True)

    @nextcord.ui.button(label="0", style=nextcord.ButtonStyle.gray)
    async def zero(self, button : nextcord.ui.Button, interaction : nextcord.Interaction):
        if interaction.user==self.user:
            integer=(str(interaction.message.embeds[0].description).replace("```","").replace("\n","").replace(" ",""))+str(button.label)
            await interaction.message.edit(embed=nextcord.Embed(description=f"```\n{integer}\n```", color=interaction.message.embeds[0].color))
        else:
            await interaction.response.send_message("자신의것을 사용하세요", ephemeral=True)
   
    @nextcord.ui.button(label="00", style=nextcord.ButtonStyle.gray)
    async def DoubleZero(self, button : nextcord.ui.Button, interaction : nextcord.Interaction):
        if interaction.user==self.user:
            integer=(str(interaction.message.embeds[0].description).replace("```","").replace("\n","").replace(" ",""))+str(button.label)
            await interaction.message.edit(embed=nextcord.Embed(description=f"```\n{integer}\n```", color=interaction.message.embeds[0].color))
        else:
            await interaction.response.send_message("자신의것을 사용하세요", ephemeral=True)
    
    @nextcord.ui.button(label=".", style=nextcord.ButtonStyle.gray)
    async def dot(self, button : nextcord.ui.Button, interaction : nextcord.Interaction):
        if interaction.user==self.user:
            integer=(str(interaction.message.embeds[0].description).replace("```","").replace("\n","").replace(" ",""))+str(button.label)
            await interaction.message.edit(embed=nextcord.Embed(description=f"```\n{integer}\n```", color=interaction.message.embeds[0].color))
        else:
            await interaction.response.send_message("자신의것을 사용하세요", ephemeral=True)
    
    @nextcord.ui.button(label="-", style=nextcord.ButtonStyle.blurple)
    async def minus(self, button : nextcord.ui.Button, interaction : nextcord.Interaction):
        if interaction.user==self.user:
            integer=(str(interaction.message.embeds[0].description).replace("```","").replace("\n","").replace(" ",""))+str(button.label)
            await interaction.message.edit(embed=nextcord.Embed(description=f"```\n{integer}\n```", color=interaction.message.embeds[0].color))
        else:
            await interaction.response.send_message("자신의것을 사용하세요", ephemeral=True)
    
    @nextcord.ui.button(label="=", style=nextcord.ButtonStyle.green)
    async def equal(self, button : nextcord.ui.Button, interaction : nextcord.Interaction):
        if interaction.user==self.user:
            integer=eval(str(interaction.message.embeds[0].description).replace("```","").replace("\n","").replace(" ","").replace("×","*").replace("÷","/").replace("²","**2").replace("𝝅","3.141592"))
            await interaction.message.edit(embed=nextcord.Embed(description=f"```\n{integer}\n```", color=interaction.message.embeds[0].color))
        else:
            await interaction.response.send_message("자신의것을 사용하세요", ephemeral=True)

    @nextcord.ui.button(label="(", style=nextcord.ButtonStyle.gray)
    async def open(self, button : nextcord.ui.Button, interaction : nextcord.Interaction):
        if interaction.user==self.user:
            integer=(str(interaction.message.embeds[0].description).replace("```","").replace("\n","").replace(" ",""))+str(button.label)
            await interaction.message.edit(embed=nextcord.Embed(description=f"```\n{integer}\n```", color=interaction.message.embeds[0].color))
        else:
            await interaction.response.send_message("자신의것을 사용하세요", ephemeral=True)
    
    @nextcord.ui.button(label=")", style=nextcord.ButtonStyle.gray)
    async def cloose(self, button : nextcord.ui.Button, interaction : nextcord.Interaction):
        if interaction.user==self.user:
            integer=(str(interaction.message.embeds[0].description).replace("```","").replace("\n","").replace(" ",""))+str(button.label)
            await interaction.message.edit(embed=nextcord.Embed(description=f"```\n{integer}\n```", color=interaction.message.embeds[0].color))
        else:
            await interaction.response.send_message("자신의것을 사용하세요", ephemeral=True)

    @nextcord.ui.button(label="x²", style=nextcord.ButtonStyle.gray)
    async def squared(self, button : nextcord.ui.Button, interaction : nextcord.Interaction):
        if interaction.user==self.user:
            integer=(str(interaction.message.embeds[0].description).replace("```","").replace("\n","").replace(" ",""))+"²"
            await interaction.message.edit(embed=nextcord.Embed(description=f"```\n{integer}\n```", color=interaction.message.embeds[0].color))
        else:
            await interaction.response.send_message("자신의것을 사용하세요", ephemeral=True)
    
    @nextcord.ui.button(label="𝝅", style=nextcord.ButtonStyle.gray)
    async def pie(self, button : nextcord.ui.Button, interaction : nextcord.Interaction):
        if interaction.user==self.user:
            integer=(str(interaction.message.embeds[0].description).replace("```","").replace("\n","").replace(" ",""))+str(button.label)
            await interaction.message.edit(embed=nextcord.Embed(description=f"```\n{integer}\n```", color=interaction.message.embeds[0].color))
        else:
            await interaction.response.send_message("자신의것을 사용하세요", ephemeral=True)

    @nextcord.ui.button(label="√", style=nextcord.ButtonStyle.gray)
    async def root(self, button : nextcord.ui.Button, interaction : nextcord.Interaction):
        if interaction.user==self.user:
            integer=eval(str(interaction.message.embeds[0].description).replace("```","").replace("\n","").replace(" ",""))**(1/2)
            await interaction.message.edit(embed=nextcord.Embed(description=f"```\n{integer}\n```", color=interaction.message.embeds[0].color))
        else:
            await interaction.response.send_message("자신의것을 사용하세요", ephemeral=True)

def setup(bot):
    bot.add_cog(Calc(bot))