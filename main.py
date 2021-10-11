#ODk2OTIzNjA3NzkwNDAzNTg0.YWOLNA.PB_02PT1lnDk7dIVWzj8_V1RIq8
import discord 
from discord.ext import commands

client = commands.Bot(command_prefix = '>')

@client.event
async def on_ready():
  print("The bot is online!")
  
@client.command()
async def ping(ctx):
  await ctx.send("Pong! :ping_pong:")

client.run("ODk2OTIzNjA3NzkwNDAzNTg0.YWOLNA.PB_02PT1lnDk7dIVWzj8_V1RIq8")