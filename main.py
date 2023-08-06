import discord
from discord import app_commands
from discord.ext import commands
from discord import CategoryChannel
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

async def createTeamsAndCategory(interaction: discord.Interaction, categoryName: str, args: str):
        teams = list(args.split(","))
        createdTeamsChannels = ""
        notCreatedTeamsChannels = ""
        createdRoles = ""
        notCreatedRoles = ""
        guild = interaction.guild
        category = discord.utils.get(guild.categories, name=categoryName.lower())
        if not category:
            await guild.create_category(categoryName.lower())
            category = discord.utils.get(guild.categories, name=categoryName.lower())
        for x in teams:
            x=x.strip().replace(" ", "-")
            channel = discord.utils.get(guild.text_channels, name=x.lower(), category=category)
            if not channel:
                await guild.create_text_channel(x.lower(), category=category)
                channel = discord.utils.get(guild.text_channels, name=x.lower(), category=category)
                createdTeamsChannels += x + ', '
            else:
                notCreatedTeamsChannels += x + ', '
            await channel.set_permissions(guild.default_role, view_channel=False)
            role = discord.utils.get(guild.roles, name=x.lower())
            if not role:
                await guild.create_role(name=x.lower())
                role = discord.utils.get(guild.roles, name=x.lower())
                createdRoles += x + ', '
            else:
                notCreatedRoles += x + ', '
            await channel.set_permissions(role, view_channel=True)
        response = ""
        if len(createdTeamsChannels)>0:
            createdTeamsChannels = createdTeamsChannels.rstrip(', ') 
            response += f'{len(createdTeamsChannels.split(","))} team channels created: {createdTeamsChannels} in categeory {categoryName}\n'
        if len(notCreatedTeamsChannels)>0:
            notCreatedTeamsChannels = notCreatedTeamsChannels.rstrip(', ')
            response += f'Team channels already exists for: {notCreatedTeamsChannels} in category {categoryName}\n'

        if len(createdRoles)>0:
           createdRoles = createdRoles.rstrip(', ')
           response += f'{len(createdRoles.split(","))} team roles created: {createdRoles}\n'
        if len(notCreatedRoles)>0:
            notCreatedRoles = notCreatedRoles.rstrip(', ')
            response += f'Team roles already exists for: {notCreatedRoles}\n'
        await interaction.response.send_message(response)

@bot.tree.command(name="hello")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message("Hello " + interaction.user.mention)
    
async def SendMassMessageChosenChannels(interaction: discord.Interaction, message, channel_names):
    channel_names_list = list(channel_names.lower().split(","))
    response =""
    for channel_name in channel_names_list:
            channel_name=channel_name.strip().replace(" ", "-")
            try:
                channel = discord.utils.get(bot.get_all_channels(), name=channel_name)
                if channel:
                    await channel.send(message)
                    response += f"Message sent successfully to channel {channel.mention}.\n"
                else:
                   response += f"Channel with name {channel_name} not found.\n"
            except discord.Forbidden:
                response += f"I do not have permission to send messages in channel {channel_name}.\n"
            except discord.HTTPException as e:
                response += f"Failed to send the message to channel {channel_name}: {e}\n"
    await interaction.response.send_message(response) 

class MassMessage(commands.Cog, name= "Mass message commands"):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None      

    @app_commands.command(name="message-channels-in-category", description="Sends a chosen message in all channels in named category")
    @app_commands.describe(message = "The message you want to send to all channels in chosen category", category = "The category in which these should be send")
    async def MassMessageChannelsInChosenCategory(self, interaction: discord.Interaction, message: str, category: CategoryChannel):
        channels = category.text_channels
        channels_str = ""
        for channel in channels:
            channels_str += channel.name + ', '
        channels_str = channels_str.rstrip(', ')
        await SendMassMessageChosenChannels(interaction, message, channels_str)

    @app_commands.command(name="message-all-channels", description="Sends a chosen message in all channels")
    @app_commands.describe(message = "The message you want to send to all channels")
    async def MassMessageAllChannels(self, interaction: discord.Interaction, message: str):
        channels = interaction.guild.text_channels
        channels_str = ""
        for channel in channels:
            channels_str += channel.name + ', '
        channels_str = channels_str.rstrip(', ')
        await SendMassMessageChosenChannels(interaction, message, channels_str)  
    
    @app_commands.command(name="message-chosen-channels", description="Sends a chosen message in all chosen channel names")
    @app_commands.describe(message = "The message you want to send to channels", channel_names = "A comma seperated list of channels you want to send the message to")
    async def MessageChosenChannels(self, interaction: discord.Interaction, message: str, channel_names: str):
        await SendMassMessageChosenChannels(interaction, message, channel_names)


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

