import discord,json,os,asyncio,psycopg2
from discord.ext.commands import *
from discord_components import Button
from functions import *

con = psycopg2.connect(os.environ.get("DATABASE_URL"))
cur = con.cursor()

class ADMINS(Cog):

    def __init__(self,client):

        self.client = client

    def admin():
        
        def predicate(ctx):
            
            cur.execute("SELECT * FROM Admins")
            data = cur.fetchall()
            admins = []
            for i in data:
                admins.append(i[0])
            return ctx.author.id in admins

        return check(predicate)

    @command()
    @admin()
    async def sql(self,ctx,*code):
        
        sqlstr = r" ".join(code)
        cur.execute(sqlstr)
        con.commit()
        await ctx.send("Done ig")
        
    @command()
    @admin()
    async def sqlview(self,ctx,*code):
        
        sqlstr = r" ".join(code)
        cur.execute(sqlstr)
        data = cur.fetchall()
        msg = ""
        for i in data:
            msg+=str(i)
            msg+="\n"
        await ctx.send(msg)
        await ctx.send(cur.rowcount)
        
    @command()
    async def rb(self,ctx):
        
        cur.execute("ROLLBACK")
        await ctx.send("Done.")
        
    @command()
    @admin()
    async def sqll(self,ctx,table,what,one,two : int,items):
        item = tostring(items)
        cur.execute(f"UPDATE {table} SET {what}={item} WHERE {one}={two}")
        await ctx.send("Done.")
        
def setup(client):
    client.add_cog(ADMINS(client))