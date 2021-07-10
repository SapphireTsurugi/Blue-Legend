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
            cur.execute(f"INSERT INTO Main (ID,MONEY,LEVEL,XP,BUFFS,WORKPLACE,WTIER,INCOME,LASTWORKED,STAMINA,MSTAMINA,SLEPT,HOUSE,HOUSESOWNED,FOODSOWNED,WSTREAK,DSTREAK,DAILY,DAILYELAPSED,VOTE,VSTREAK) VALUES ({ctx.author.id},0,1,0,'[]','Fast Food',1,10,5,10,10,True,'Homeless','[]','[]',0,0,False,0,False,0);")
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
            embed.add_field(name = "Error using this command. Can\'t make an existance exist.",value = "Used command 1start.",inline = False)
            msg = await ctx.send(embed = embed)
            
    @command(aliases=["pf",])
    async def profile(self,ctx,user : discord.Member = None):
        
        if user == None:
            user = ctx.author
            
        cur.execute(f"SELECT MONEY,LEVEL,XP,BUFFS,WORKPLACE,INCOME,STAMINA,MSTAMINA,HOUSE,VSTREAK,DSTREAK FROM Main WHERE ID={ctx.author.id}")
        d = cur.fetchall()[0]
        embed = discord.Embed(title="Profile", description="Do 1houses and 1foods for more options.",color = discord.Color.random())
        embed.set_author(name=ctx.author.name)
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.add_field(name=f"Money : {d[0]}",value=f"Buffs : {d[3]}",inline=False)
        embed.add_field(name=f"Stamina : { d[6]}",value=f"Maximum Stamina : {d[7]}",inline=False)
        exp = xplevel(ctx.author)
        embed.add_field(name=f"Level:{d[1]}",value=f"Exp:{d[2]}/{exp}",inline=False)
        embed.add_field(name=f"Home : {d[8]}",value=f"Workplace : {d[4]}",inline=False)
        embed.add_field(name=f"Daily Streak : {d[10]}",value=f"Voting Streak : {d[9]})
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(BASE(client))