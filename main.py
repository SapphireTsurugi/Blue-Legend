import discord, os, asyncio
from discord_components import DiscordComponents , Button
from discord.ext import commands
import json

with open("data.json") as f:
    envs = json.load(f)

client = commands.Bot(command_prefix=['1'],intents=discord.Intents().all())

cogs = ["BASICCMD","BASE"]

for i in cogs:
    client.load_extension(f"cogs.{i}")

@client.event
async def on_ready():

    DiscordComponents(client)
    print(f"{client.user.name} has Awoken!")

client.run(envs["Token"], bot=True, reconnect=True)