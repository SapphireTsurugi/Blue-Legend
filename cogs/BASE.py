import discord,json,os,asyncio
from discord.ext.commands import *
from discord_components import Button 

class BASE(Cog):

    def __init__(self,client):

        self.client = client

    @command()
    async def start(self,ctx):
        
        return

def setup(client):
    client.add_cog(BASE(client))