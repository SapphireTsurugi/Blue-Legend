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
                fooods = tostring(foods)
                cur.execute(f"UPDATE Main SET STAMINA={f},HUNGER=HUNGER+10,FOODSOWNED=\'{fooods}\' WHERE ID={ctx.author.id}")
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
            
    @command()
    async def work(self,ctx):
        
        cur.execute(f"SELECT JOB,STAMINA,BUFF1T,BUFF2T,BUFF3T FROM Main WHERE ID={ctx.author.id}")
        d = cur.fetchall()[0]
        
        gb,eb,sb = 1,1,1
        if d[2] != 0:
            gb = 1.5
        if d[3] != 0:
            eb = 1.5
        if d[4] != 0:
            sb = 0.75
        
        cur.execute(f"SELECT INCOME,STAMINA,TIER FROM Jobs WHERE JOB=\'{d[0]}\'")
        e = cur.fetchall()[0]
        js = e[1] * sb
        if d[1] >= js:
            pass
        else:
            await ctx.send("You worked so hard already. Get some sleep and eat.")
            return
        f = d[1] - js
        moni = e[0]*gb
        cur.execute(f"UPDATE Main SET STAMINA={f},MONEY=MONEY+{moni} WHERE ID={ctx.author.id}")
        con.commit()
        await ctx.send("Worked")

def setup(client):
    client.add_cog(BASE(client))