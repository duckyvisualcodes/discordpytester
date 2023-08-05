import discord
from discord import app_commands
from discord.ext import commands
import asyncio
import gspread

bot = commands.Bot(command_prefix="/", intents=discord.Intents.all())

@bot.event
async def on_ready():
    await bot.add_cog(CreateTeams(bot))
    await bot.add_cog(CreateMatchday(bot))
    await bot.add_cog(MassMessage(bot))
    synced = await bot.tree.sync()
    print(f"Synced {len(synced)} command(s).")
    print ("Tournament Admin is online")

async def createTeamsAndCategory(interaction: discord.Interaction, categoryName, args: str):
        teams = list(args.split(","))
        arguments = ""
        guild = interaction.guild
        category = discord.utils.get(guild.categories, name=categoryName)
        if not category:
            await guild.create_category(categoryName)
            category = discord.utils.get(guild.categories, name=categoryName)
        for x in teams:
            x=x.strip().replace(" ", "-")
            channel = discord.utils.get(guild.text_channels, name=x, category=category)
            if not channel:
                await guild.create_text_channel(x, category=category)
                arguments += x + ', '
        if len(arguments)>0:
            arguments = arguments.rstrip(', ') 
            await interaction.response.send_message(f'{len(arguments.split(","))} team channels created: {arguments} in categeory {categoryName}')   
        else:
            await interaction.response.send_message(f'No new team channels created team channels already exists for: {args} in category {categoryName}')

@bot.tree.command(name="hello")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message("Hello " + interaction.user.mention)

@bot.tree.command(name="sync") 
async def sync(ctx):
    synced = await bot.tree.sync()
    print(f"Synced {len(synced)} command(s).")

async def SendMassMessageChosenChannels(ctx, message, *channel_ids):
    for channel_id in channel_ids:
            try:
                channel = discord.utils.get(bot.get_all_channels(), name=channel_id)
                if channel:
                    await channel.send(message)
                    await ctx.channel.send(f"Message sent successfully to channel {channel.mention}.")
                else:
                    await ctx.channel.send(f"Channel with ID {channel_id} not found.")
            except discord.Forbidden:
                await ctx.channel.send(f"I do not have permission to send messages in channel {channel_id}.")
            except discord.HTTPException as e:
                await ctx.channel.send(f"Failed to send the message to channel {channel_id}: {e}") 

class MassMessage(commands.Cog, name= "Mass message commands"):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None      

    @commands.command(name="MassMessageChannelsInChosenCategory", help="Sends a chosen message in all channels in named category" )
    async def MassMessageChannelsInChosenCategory(ctx, *teams ):
        #TODO implement
        raise NotImplementedError

    @commands.command(name="MassMessageAllChannels", help="Sends a chosen message in all channels")
    async def MassMessageAllChannels(self, ctx, categoryName, *teams):
        #TODO implement
        raise NotImplementedError  
    
    @commands.command(name="MassMessageChosenChannels", help="Sends a chosen message in all chosen channel names")
    async def MassMessageChosenChannels(self, ctx, message, *channel_name):
        await SendMassMessageChosenChannels(ctx, message, *channel_name)


class CreateTeams(commands.Cog, name= "Team Role & Channel Setup commands"):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @app_commands.command(name="setup-teams-without-category", description="Sets up team text channels under default category \'TEAMS\'" )
    @app_commands.describe(teams = "What teams you want to create as comma seperated list")
    async def setupteamswithoutcategory(self, interaction: discord.Interaction, teams: str):
        await createTeamsAndCategory(interaction, 'teams', teams)
        #TODO Finish implementation
        raise NotImplementedError

    @app_commands.command(name="setup-teams-with-category", description="Sets up team text channels with first argument being the category under which the channels go under")
    @app_commands.describe(teams = "What teams you want to create as comma seperated list", categoryname = "What you want to name your custom category")
    async def setupteamswithcategory(self, interaction: discord.Interaction, categoryname: str, teams: str):
        await createTeamsAndCategory(interaction, categoryname, teams)   
        #TODO Finish implementation
        raise NotImplementedError 


class CreateMatchday(commands.Cog, name= "Matchday Channel Creation commands"):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command(name="setupMatchdayChannelsWithoutCategory", help="Sets up match day channels under default category \'MATCHES\'" )
    async def setupMatchdayChannelsWithoutCategory(ctx, *teams ):
        #TODO implement
        raise NotImplementedError

    @commands.command(name="setupMatchdayChannelsWithCategory", help="Sets up tmatch day channels with first argument being the category under which the channels go under")
    async def setupMatchdayChannelsWithCategory(ctx, categoryName, *teams):
        #TODO implement
        raise NotImplementedError

bot.run("MTEzNjAwMzUxMTU0NTQ5OTc3OQ.G1nGkj.tWdI1pGTvjocll0dQtLOgcP2xA_LvcHVAcAklA")

