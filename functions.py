import discord,json,os,asyncio,psycopg2
from discord.ext.commands import *
from discord_components import Button

con = psycopg2.connect(os.environ.get("DATABASE_URL"))
cur = con.cursor()

def xplevel(level):
    exp = 2500*level
    if level == 100:
        return 0
        
    else:
        return exp
        
def tolist(str2):
    list2 = str2.split(",")
    return list2

def tostring(list2):
    str2 = ",".join(list2)
    return str2

def levelupcheck(xp,level):
    reqxp = xplevel(level)
    if xp >= reqxp:
        return True
    else:
        return False

