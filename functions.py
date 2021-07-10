import discord,json,os,asyncio,psycopg2
from discord.ext.commands import *
from discord_components import Button

con = psycopg2.connect(os.environ.get("DATABASE_URL"))
cur = con.cursor()

def xplevel(user):
    cur.execute(f"SELECT LEVEL FROM Main WHERE ID={user.id}")
    level = cur.fetchall()[0][0]
    exp = 2500*level
    if level == 100:
        return 0
        
    else:
        return exp

def buffstolist(buffs):
    buff = json.loads(buffs)
    msg = ""
    for i in buff:
        msg += str(i)
        msg += "\n"
