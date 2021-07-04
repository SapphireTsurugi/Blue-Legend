import discord,json,os,asyncio,psycopg2
from discord.ext.commands import *
from discord_components import Button
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

con = psycopg2.connect(os.environ.get("DATABASE_URL"))
con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cur = con.cursor()

class BASE(Cog):

    def __init__(self,client):

        self.client = client

    @command()
    async def sql(self,ctx,*code):
        
        sqlstr = r" ".join(code)
        cur.execute(sqlstr)
        con.commit()
        await ctx.send("Done ig")
        con.close()
        
    @command()
    async def sqlview(self,ctx,*code):
        
        sqlstr = r" ".join(code)
        cur.execute(sqlstr)
        data = cur.fetchall()
        await ctx.send(data)

def setup(client):
    client.add_cog(BASE(client))