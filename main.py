import discord, os, asyncio,psycopg2
from discord_components import DiscordComponents , Button
from discord.ext import commands,tasks

client = commands.Bot(command_prefix=['2'],intents=discord.Intents().all())

con = psycopg2.connect(os.environ.get("DATABASE_URL"))
cur = con.cursor()

cogs = ["BASICCMD","ADMINS","USER","BASE"]

for i in cogs:
    client.load_extension(f"cogs.{i}")

@client.event
async def on_ready():

    DiscordComponents(client)
    add_time.start()
    print(f"{client.user.name} has Awoken")

@tasks.loop(seconds=60)
async def add_time():
    cur.execute("UPDATE Main SET DAILYELAPSED=DAILYELAPSED+1")
    cur.execute("UPDATE Main SET HUNGER=HUNGER-10 WHERE HUNGER>10")
    cur.execute("UPDATE Main SET SLEEPINESS=SLEEPINESS-10 WHERE HUNGER>10")
    con.commit()
    
client.run(os.environ.get("Token"), bot=True, reconnect=True)
