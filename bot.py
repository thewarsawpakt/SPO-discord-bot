import discord 
from discord.ext import commands
from apihandler import getProfile
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
async def profile(ctx, playername):
    if not playername:
        await ctx.send("Please enter a player name.")
        return
    data = getProfile(playername)
    await ctx.send(embed=data)
    

client.run(TOKEN)