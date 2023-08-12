import discord
from discord import app_commands
from discord.ext import commands

class CreateTeams(commands.Cog, name= "Team Role & Channel Setup commands"):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @app_commands.command(name="setup-teams-without-category", description="Sets up team text channels under default category \'TEAMS\'" )
    @app_commands.describe(teams = "What teams you want to create as comma seperated list")
    async def setupteamswithoutcategory(self, interaction: discord.Interaction, teams: str):
        await self.createTeamsAndCategory(interaction, 'teams', teams)
        #TODO Finish implementation
        raise NotImplementedError

    @app_commands.command(name="setup-teams-with-category", description="Sets up team text channels with first argument being the category under which the channels go under")
    @app_commands.describe(teams = "What teams you want to create as comma seperated list", categoryname = "What you want to name your custom category")
    async def setupteamswithcategory(self, interaction: discord.Interaction, categoryname: str, teams: str):
        await self.createTeamsAndCategory(interaction, categoryname, teams)   
        #TODO Finish implementation
        raise NotImplementedError 
    



    
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