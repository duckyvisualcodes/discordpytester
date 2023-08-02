import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print ("Tournament Admin is online")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong")

@bot.command()
async def createteam(ctx):
    test1 = ""
    await ctx.send(ctx.author + " Creating your team")
    

bot.run("MTEzNjAwMzUxMTU0NTQ5OTc3OQ.G1nGkj.tWdI1pGTvjocll0dQtLOgcP2xA_LvcHVAcAklA")