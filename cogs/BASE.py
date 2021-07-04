import discord,json,os,asyncio,psycopg2
from discord.ext.commands import *
from discord_components import Button

con = psycopg2.connect(os.environ.get("DATABASE_URL"))
cur = con.cursor()

class BASE(Cog):

    def __init__(self,client):

        self.client = client

    @command()
    async def sql(self,ctx,*code):
        
        sqlstr = " ".join(code)
        cur.execute(sqlstr)
        con.commit()
        await ctx.send("Done ig")

con.close()

def setup(client):
    client.add_cog(BASE(client))