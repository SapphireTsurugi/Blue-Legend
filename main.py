import discord, os, asyncio
from discord_components import DiscordComponents , Button
from discord.ext import commands

client = commands.Bot(command_prefix=['2'],intents=discord.Intents().all())

cogs = ["BASICCMD","ADMINS"]

for i in cogs:
    client.load_extension(f"cogs.{i}")

@client.event
async def on_ready():

    DiscordComponents(client)
    print(f"{client.user.name} has Awoken!")

client.run(os.environ.get("Token"), bot=True, reconnect=True)
