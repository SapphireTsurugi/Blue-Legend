import discord,json,os,asyncio,psycopg2
from discord.ext.commands import *
from discord_components import Button

con = psycopg2.connect(os.environ.get("DATABASE_URL"))
cur = con.cursor()

class BASE(Cog):

    def __init__(self,client):

        self.client = client

    def userconvertor(Convertor):
        def convert(self,ctx,argument):
           
            try:
                if isinstance(argument,discord.Member):
                    return argument

            except:
                return ctx.message.author

    @command()
    async def start(self,ctx):
        
        cur.execute(f"SELECT * FROM Main WHERE ID = {ctx.author.id}")
        if cur.rowcount == 0:
            cur.execute(f"INSERT INTO Main (ID,HP,MHP,DEF,ATK,ARMOR,WEP,LEVEL,XP,LOCX,LOCY,LOCN,LOCZ,GOLD,GEMS,INV,PRESTIGE,BATTLE,TUT_STATE) VALUES ({ctx.author.id},100,100,10,10,'None','None',1,0,1,1,'The Village',1,0,100,'[]',0,0,0)")
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
        if num == 1:
            user.send("Works")
        else:
            ctx.send("You completed the tutorial already. You can use 1quests now.")
            
    @command(aliases=["pf",])
    async def profile(self,ctx,user : userconvertor and discord.Member):
        
        await ctx.send(user.avatar_url)
            
    @command()
    async def world(self,ctx):
        
        pass

def setup(client):
    client.add_cog(BASE(client))