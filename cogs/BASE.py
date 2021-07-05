import discord,json,os,asyncio,psycopg2
from discord.ext.commands import *
from discord_components import Button

con = psycopg2.connect(os.environ.get("DATABASE_URL"))
cur = con.cursor()

class BASE(Cog):

    def __init__(self,client):

        self.client = client

    @command()
    async def start(self,ctx):
        
        cur.execute(f"SELECT * FROM Main WHERE ID = {ctx.author.id}")
        if cur.rowcount == 0:
            cur.execute(f"INSERT INTO Main (ID,HP,MHP,DEF,ATK,ARMOR,WEP,LEVEL,XP,LOCX,LOCY,LOCN,LOCZ,GOLD,GEMS,INV,PRESTIGE,BATTLE,TUT_STATE) VALUES ({ctx.author.id},100,100,10,10,'None','None',1,0,1,1,'The Village',1,0,100,'[]',0,0,0)")
            con.commit()
            msg = await ctx.send("Umm Hello Adventurer. What Can I help you with today?")
            await asyncio.sleep(1)
            await msg.edit("Oh you want to register yourself as a new adventurer? Great.")
            await asyncio.sleep(5)
            await msg.edit("Done!.Type 1tut for the Master to help you.")
            await asyncio.sleep(2)
            await msg.edit("Also Come back after you received the Master's certification to start getting Quests. Good Luck!.")
        else:
            msg = await ctx.send("Umm Hello Adventurer. What Can I help you with today?")
            await asyncio.sleep(1)
            await msg.edit("Oh you want to register yourself as a new adventurer? Great.")
            await asyncio.sleep(5)
            await msg.edit("You are a popular adventurer throughout the Kingdom and you want to start over?")
            await asyncio.sleep(2)
            await msg.edit("Maybe are you looking to prestige. Try 1prestige for that. Hope we can meet again soon.")
        

def setup(client):
    client.add_cog(BASE(client))