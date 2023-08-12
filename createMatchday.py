import discord
from discord import app_commands
from discord.ext import commands
from GspreadSetup import gc
import gspread

class CreateMatchday(commands.Cog, name= "Matchday Channel Creation commands"):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command(name="setupMatchdayChannelsWithoutCategory", help="Sets up match day channels under default category \'MATCHES\'" )
    async def setupMatchdayChannelsWithoutCategory(self, interaction: discord.Interaction, sheetlink: str):
        #TODO implement
        raise NotImplementedError

    @commands.command(name="setupMatchdayChannelsWithCategory", help="Sets up tmatch day channels with first argument being the category under which the channels go under")
    async def setupMatchdayChannelsWithCategory(self, interaction: discord.Interaction, sheetlink: str, categoryname: str):
        #TODO implement
        raise NotImplementedError
    
    @app_commands.command(name="test-gspread-command")
    @app_commands.describe(sheetlink = "The link to the sheet of information about matches, make sure it follows the given template")
    async def testgspreadcommand(self, interaction: discord.Interaction, sheetlink: str):
        sh = await self.CheckSheetContact(interaction, sheetlink)
        if sh is not None:
            await interaction.response.send_message(sh.sheet1.acell('A1').value)


    async def CheckSheetContact(interaction: discord.Interaction, sheetlink: str):
        try:
            sh = gc.open_by_url(sheetlink)
        except gspread.exceptions.APIError as a:
            first_value = next(iter(a.args[0].values()))
            response = ""
            if(first_value==404):
                response = "The sheet provided can not be found, make sure you have given a correct link"
            elif(first_value==403):
                response = "The sheet provided can not be accessed by bot, make sure you have set share settings, General access to anyone with link can edit"
            else:
                response = f"The error {a} is not currently handled contact bot owners about this issue"
            await interaction.response.send_message(response)
            return None
        
        try:
            matchdayssheet = sh.worksheet("Matchdays")
        except gspread.exceptions.WorksheetNotFound:
            await interaction.response.send_message("You changed the name of the worksheet to something other than Matchdays, please change it back or get new template")
            return None
        
        UUIDCode = matchdayssheet.acell("L2").value
        if UUIDCode != "7bd4e9e2-88d9-4606-ba44-3fec90b4f339":
            await interaction.response.send_message("You are either not using template or have deleted the ID, if you need template go to discord x or contact x to get it")
            return None
        
        return sh