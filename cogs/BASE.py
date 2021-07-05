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
            cur.execute(f"INSERT INTO Main (ID,HP,MHP,DEF,ATK,ARMOR,WEP,LEVEL,XP,LOCX,LOCY,LOCN,LOCZ,GOLD,GEMS,INV,PRESTIGE,BATTLE,TUT_STATE) VALUES ({ctx.author.id},100,100,10,10,None,None,1,0,1,1,'The Village',1,0,100,[],0,False,0)")
            con.commit()
            await ctx.send("Umm Hello Adventurer. What Can I help you with today? Oh you want to register yourself as a new adventurer? Great. ... . Done!.Type !tut for the Master to help you. Also Come back after you received the Master's certification to start getting Quests. Good Luck!.")
        else:
            await ctx.send("Want to start over again? Try prestiging.")
        

def setup(client):
    client.add_cog(BASE(client))