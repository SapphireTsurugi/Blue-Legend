import discord,json,os,asyncio,psycopg2
from discord.ext.commands import *
from discord_components import Button
from functions import *

con = psycopg2.connect(os.environ.get("DATABASE_URL"))
cur = con.cursor()

class BASE(Cog):

    def __init__(self,client):

        self.client = client

    @command()
    async def start(self,ctx):
        cur.execute("ROLLBACK")
        cur.execute(f"SELECT * FROM Main WHERE ID = {ctx.author.id}")
        if cur.rowcount == 0:
            cur.execute(f"INSERT INTO Main (ID,MONEY,LEVEL,XP,BUFFS,WORKPLACE,WTIER,INCOME,LASTWORKED,STAMINA,MSTAMINA,SLEPT,HOUSE,HOUSESOWNED,FOODSOWNED,WSTREAK,DSTREAK,DAILY,DAILYELAPSED) VALUES ({ctx.author.id},0,1,0,'[]','Fast Food',1,10,5,10,10,True,'Homeless','[]','[]',0,0,False,0);")
            con.commit()
            embed = discord.Embed(title = "Welcome", color = discord.Color.blue())
            embed.set_author(name = ctx.author)
            embed.set_thumbnail(url = ctx.author.avatar_url)
            embed.add_field(name = "Umm Hello Adventurer. What Can I help you with today?",value = "Used command 1start.",inline = False)
            msg = await ctx.send(embed = embed)
            
        else:
            embed = discord.Embed(title = "Welcome", color = discord.Color.blue())
            embed.set_author(name = ctx.author)
            embed.set_thumbnail(url = ctx.author.avatar_url)
            embed.add_field(name = "Umm Hello Adventurer. What Can I help you with today?",value = "Used command 1start.",inline = False)
            msg = await ctx.send(embed = embed)
            await asyncio.sleep(3)
            embed.clear_fields()
            embed.add_field(name="Oh you want to register yourself as a new adventurer? Great.",value = "Used command 1start",inline = False)
            await msg.edit(embed=embed)
            await asyncio.sleep(5)
            embed.clear_fields()
            embed.add_field(name="You are a popular adventurer throughout the Kingdom and you want to start over?",value ="Used command 1start")
            await msg.edit(embed=embed)
            await asyncio.sleep(3)
            embed.clear_fields()
            embed.add_field(name="Maybe are you looking to prestige. Try 1prestige for that. Hope we can meet again soon.",value = "Try using 1prestige command.",inline = False)
            await msg.edit(embed=embed)

def setup(client):
    client.add_cog(BASE(client))