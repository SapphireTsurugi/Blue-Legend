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
            cur.execute(f"INSERT INTO Main (ID,HP,MHP,DEF,ATK,STAMINA,MSTAM,ARMOR,WEP,LEVEL,XP,LOCX,LOCY,LOCN,LOCZ,GOLD,GEMS,INV,PRESTIGE,BATTLE,TUT_STATE) VALUES ({ctx.author.id},100,100,10,10,20,20,'None','None',1,0,1,1,'The Village',1,0,100,'[]',0,0,0)")
            con.commit()
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
            embed.add_field(name="Done!.Type 1tut for the Master to help you.",value = "Used command 1start",inline = False)
            await msg.edit(embed=embed)
            await asyncio.sleep(3)
            embed.clear_fields()
            embed.add_field(name="Also Come back after you received the Master's certification to start getting Quests. Good Luck!.",value = "Use 1tut for more help.",inline = False)
            await msg.edit(embed=embed)
            
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
        
    @command(aliases=["tut",])
    async def tutorial(self,ctx):
        
        cur.execute(f"SELECT TUT_STATE FROM Main WHERE ID={ctx.author.id}")
        data = cur.fetchall()[0]
        num = data[0]
        user = ctx.author
        if num == 0:
            await user.send("Works")
        else:
            await ctx.send("You completed the tutorial already. You can use 1quests now.")
            
    @command(aliases=["pf",])
    async def profile(self,ctx,user : discord.Member = None):
        
        if user == None:
            user = ctx.author
            
        cur.execute(f"SELECT HP,MHP,ATK,DEF,STAMINA,ARMOR,WEP,LEVEL,XP,GOLD,GEMS,LOCX,LOCY,LOCZ,LOCN,MSTAM,PRESTIGE FROM Main WHERE ID={ctx.author.id}")
        d = cur.fetchall()[0]
        embed = discord.Embed(title="Profile", description="Do 1inv for inventory.",color = discord.Color.random())
        embed.set_author(name=ctx.author.name)
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.add_field(name=f"Gold : {d[9]}",value=f"Gems : {d[10]}",inline=False)
        embed.add_field(name=f"Hp : { d[0]}/{d[1]}\t\tStamina : {d[4]}/{d[15]}",value=f"Atk : {d[2]}\t\tDef : {d[3]}",inline=False)
        embed.add_field(name=f"Armor : {d[4]}",value=f"Weapon : {d[5]}",inline=False)
        embed.add_field(name=f"Location {d[14]}({d[11]},{d[12]})",value = f"Floor : {d[13]}",inline=False)
        exp = xplevel(ctx.author)
        embed.add_field(name=f"Level:{d[7]}",value=f"Exp:{d[8]}/{exp}",inline=False)
        embed.add_field(name=f"Prestige :",value=d[16],inline=False)
        await ctx.send(embed=embed)
        
    @command(aliases=["hp","stat","stam"])
    async def stats(self,ctx,user : discord.Member = None):
        
        if user == None:
            user = ctx.author
            
        cur.execute(f"SELECT HP,MHP,ATK,DEF,ARMOR,WEP,STAMINA,MSTAM FROM Main WHERE ID={ctx.author.id};")
        d = cur.fetchall()[0]
        embed = discord.Embed(title="Stats",color=discord.Color.red())
        embed.set_author(name=ctx.author.name)
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.add_field(name=f"Hp : {d[0]}/{d[1]}",value=f"STAMINA : {d[6]}/{d[7]}",inline=False)
        embed.add_field(name=f"Attack : {d[2]}",value=f"Defense : {d[3]}",inline=False)
        embed.add_field(name=f"Armor : {d[4]}",value=f"Weapon : {d[5]}",inline=False)
        await ctx.send(embed=embed)
    
    @command()
    async def world(self,ctx):
        
        pass

def setup(client):
    client.add_cog(BASE(client))