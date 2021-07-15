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
    async def eat(self,ctx,*fdname):
        
        food = " ".join(fdname)
        cur.execute(f"SELECT FOODSOWNED,STAMINA,MSTAMINA,HUNGER FROM Main WHERE ID={ctx.author.id}")
        d = cur.fetchall()[0]
        foods = tolist(d[0])
        if food in foods:
            cur.execute(f"SELECT STAMINA FROM Foods WHERE FOOD=\'{food}\'")
            e = cur.fetchall()[0][0]
            if d[1] == d[2] or d[3] > 90:
                await ctx.send("You are already full.")
            elif d[1] < d[2] and d[3] <= 90:
                if d[1] + e <= d[2]:
                    f = d[1] + e
                else:
                    f = d[2]
                foods.remove(food)
                cur.execute(f"UPDATE Main SET STAMINA={f},HUNGER=HUNGER+10,FOODSOWNED=\'{foods}\' WHERE ID={ctx.author.id}")
                con.commit()
                await ctx.send("*Burp* Shhh! Dont Burp loudly.")

        else:
            await ctx.send("Either that food dont exist or you dont have it. Go buy it.")
            
    @command()
    async def sleep(self,ctx):
        
        cur.execute(f"SELECT HOUSE,STAMINA,MSTAMINA,SLEEPINESS FROM Main WHERE ID={ctx.author.id}")
        d = cur.fetchall()[0]
        cur.execute(f"SELECT STAMINA FROM Houses WHERE HOUSE=\'{d[0]}\';")
        e = cur.fetchall()[0][0]
        if d[1] == d[2] or d[3] > 90:
            await ctx.send("You dont even feel sleepy the slightest.")
        elif d[1] < d[2] and d[3] <= 90:
            if d[1] + e <= d[2]:
                f = d[1] + e
            else:
                f = d[2]
            cur.execute(f"UPDATE Main SET STAMINA={f},SLEEPINESS=SLEEPINESS+10 WHERE ID={ctx.author.id}")
            con.commit()
            await ctx.send("Wakey wakey, YOU ARE LATE!.")

def setup(client):
    client.add_cog(BASE(client))