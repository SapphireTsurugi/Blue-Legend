import discord, os, asyncio,psycopg2,topggpy
from discord_components import DiscordComponents , Button
from discord.ext import commands,tasks

client = commands.Bot(command_prefix=['2'],intents=discord.Intents().all())

con = psycopg2.connect(os.environ.get("DATABASE_URL"))
cur = con.cursor()

cogs = ["BASICCMD","ADMINS","USER"]

for i in cogs:
    client.load_extension(f"cogs.{i}")

@client.event
async def on_ready():

    DiscordComponents(client)
    add_time_for_daily.start()
    print(f"{client.user.name} has Awoken!")
    
@client.event()
async def topgg.on_dbl_vote(data):
    print(vote)
    print(vote["user"])

@tasks.loop(seconds=60)
async def add_time_for_daily():
    cur.execute("UPDATE Main SET DAILYELAPSED=DAILYELAPSED+1")
    con.commit()
    
client.run(os.environ.get("Token"), bot=True, reconnect=True)
