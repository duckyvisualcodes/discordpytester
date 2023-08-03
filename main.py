import discord
from discord.ext import commands
import asyncio
import gspread

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print ("Tournament Admin is online")

@bot.command(name="ping", help="Will return pong")
async def ping(ctx):
    await ctx.send("Pong")

@bot.command(name="createTeam", help="Sends a message saying your team is created")
async def createteam(ctx):
    await ctx.send(ctx.author.name + " Your team is being created")

@bot.command(name="typingtest", help="A test for the typing functionality")
async def typingtest(ctx):
    await ctx.channel.send("Starting big computation")
    async with ctx.channel.typing():
        # simulate something heavy
        await asyncio.sleep(20)
    await ctx.channel.send('Done!')
    
@bot.command(name="argstest", help="A test for inputting specific defined amount of arguments")
async def argstest(ctx, arg1, arg2):
    await ctx.send(f'you send {arg1} and {arg2}')

@bot.command(name="setupTeamsWithoutCategory", help="Sets up team text channels under default category \'TEAMS\'" )
async def setupTeamsWithoutCategory(ctx, *teams ):
    await createTeamsAndCategory(ctx, *teams, categoryName='teams')

@bot.command(name="setupTeamsWithCategory", help="Sets up team text channels with first argument being the category under which the text channels go under")
async def setupTeamsWithCategory(ctx, categoryName, *teams):
    await createTeamsAndCategory(ctx, *teams, categoryName=categoryName)
    
@bot.command(name="POG", help="Milo wanted a support for when he does something POG ;)")
async def POG(ctx):
    await ctx.send('well done!')

@bot.command()
async def testArgumentDescriptions(ctx, arg1 ):
    return

async def createTeamsAndCategory(ctx, *args, categoryName):
    arguments = ', '.join(args)
    guild = ctx.message.guild
    category = discord.utils.get(guild.categories, name=categoryName.upper())
    if not category:
        await guild.create_category(categoryName)
        category = discord.utils.get(guild.categories, name=categoryName)
    for x in args:
        channel = discord.utils.get(guild.text_channels, name=x.lower(), category=category)
        if not channel:
            await guild.create_text_channel(x, category=category)
    await ctx.send(f'{len(args)} Teams: {arguments}')

bot.run("MTEzNjAwMzUxMTU0NTQ5OTc3OQ.G1nGkj.tWdI1pGTvjocll0dQtLOgcP2xA_LvcHVAcAklA")