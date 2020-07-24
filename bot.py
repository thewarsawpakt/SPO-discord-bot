import discord 
from discord.ext import commands
import database

with open("token", "r") as token_file:
    TOKEN = token_file.read()
    token_file.close()


client = commands.Bot(command_prefix=".")


@client.event
async def on_ready():
    print(f'\n\nLogged in as: {client.user.name} - {client.user.id}\nDiscord.py Version: {discord.__version__}\n')
    
@client.event   
async def on_member_join(member: discord.Member):
    database.CreateUser(member.id, member.name)

@client.command()
async def ping(ctx):
    latency = round(client.latency, 4)*1000
    await ctx.send(f"Bot's latency is {latency}ms")


client.run(TOKEN)