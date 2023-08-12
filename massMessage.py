import discord
from discord import app_commands
from discord.ext import commands
from discord import CategoryChannel

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
        await self.SendMassMessageChosenChannels(interaction, message, channels_str)

    @app_commands.command(name="message-all-channels", description="Sends a chosen message in all channels")
    @app_commands.describe(message = "The message you want to send to all channels")
    async def MassMessageAllChannels(self, interaction: discord.Interaction, message: str):
        channels = interaction.guild.text_channels
        channels_str = ""
        for channel in channels:
            channels_str += channel.name + ', '
        channels_str = channels_str.rstrip(', ')
        await self.SendMassMessageChosenChannels(interaction, message, channels_str)  
    
    @app_commands.command(name="message-chosen-channels", description="Sends a chosen message in all chosen channel names")
    @app_commands.describe(message = "The message you want to send to channels", channel_names = "A comma seperated list of channels you want to send the message to")
    async def MessageChosenChannels(self, interaction: discord.Interaction, message: str, channel_names: str):
        await self.SendMassMessageChosenChannels(interaction, message, channel_names)
    
    


    async def SendMassMessageChosenChannels(self, interaction: discord.Interaction, message, channel_names):
        channel_names_list = list(channel_names.lower().split(","))
        response =""
        for channel_name in channel_names_list:
                channel_name=channel_name.strip().replace(" ", "-")
                try:
                    channel = discord.utils.get(self.bot.get_all_channels(), name=channel_name)
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