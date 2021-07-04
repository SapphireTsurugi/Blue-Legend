import discord,json,os,asyncio,psycopg2
from discord.ext.commands import *
from discord_components import Button

con = psycopg2.connect(os.environ.get("DATABASE_URL"))
cur = con.cursor()

class ADMINS(Cog):

    def __init__(self,client):

        self.client = client

    @command()
    async def sql(self,ctx,*code):
        
        sqlstr = r" ".join(code)
        cur.execute(sqlstr)
        con.commit()
        await ctx.send("Done ig")
        
    @command()
    async def sqlview(self,ctx,*code):
        
        sqlstr = r" ".join(code)
        cur.execute(sqlstr)
        data = cur.fetchall()
        msg = ""
        for i in data:
            msg+=str(i)
            msg+="\n"
        await ctx.send(msg)

def setup(client):
    client.add_cog(ADMINS(client))