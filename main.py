import discord
from discord.ext import commands
import asyncio

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print ("Tournament Admin is online")
    await bot.add_cog(CreateTeams(bot))

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
    
@bot.command(name="POG", help="Milo wanted a support for when he does something POG ;)",)
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


class CreateTeams(commands.Cog, name= "Create teams commands"):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
    
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send(f'Welcome {member.mention}.') 

    @commands.command(name="setupTeamsWithoutCategory", help="Sets up team text channels under default category \'TEAMS\'" )
    async def setupTeamsWithoutCategory(ctx, *teams ):
        await createTeamsAndCategory(ctx, *teams, categoryName='teams')

    @commands.command(name="setupTeamsWithCategory", help="Sets up team text channels with first argument being the category under which the text channels go under")
    async def setupTeamsWithCategory(ctx, categoryName, *teams):
        await createTeamsAndCategory(ctx, *teams, categoryName=categoryName)

    

class SupremeHelpCommand(commands.HelpCommand):
    def get_command_signature(self, command):
        return '%s%s %s' % (self.context.clean_prefix, command.qualified_name, command.signature)

    async def send_bot_help(self, mapping):
        embed = discord.Embed(title="Help", color=discord.Color.blurple())
        for cog, commands in mapping.items():
            filtered = await self.filter_commands(commands, sort=True)
            if command_signatures := [
                self.get_command_signature(c) for c in filtered
            ]:
                cog_name = getattr(cog, "qualified_name", "No Category")
                embed.add_field(name=cog_name, value="\n".join(command_signatures), inline=False)

        channel = self.get_destination()
        await channel.send(embed=embed)

    async def send_command_help(self, command):
        embed = discord.Embed(title=self.get_command_signature(command) , color=discord.Color.blurple())
        if command.help:
            embed.description = command.help
        if alias := command.aliases:
            embed.add_field(name="Aliases", value=", ".join(alias), inline=False)

        channel = self.get_destination()
        await channel.send(embed=embed)

    async def send_help_embed(self, title, description, commands): # a helper function to add commands to an embed
        embed = discord.Embed(title=title, description=description or "No help found...")

        if filtered_commands := await self.filter_commands(commands):
            for command in filtered_commands:
                embed.add_field(name=self.get_command_signature(command), value=command.help or "No help found...")

        await self.get_destination().send(embed=embed)

    async def send_group_help(self, group):
        title = self.get_command_signature(group)
        await self.send_help_embed(title, group.help, group.commands)

    async def send_cog_help(self, cog):
        title = cog.qualified_name or "No"
        await self.send_help_embed(f'{title} Category', cog.description, cog.get_commands())

    async def send_error_message(self, error):
        embed = discord.Embed(title="Error", description=error, color=discord.Color.red())
        channel = self.get_destination()

        await channel.send(embed=embed)

bot.help_command = SupremeHelpCommand()

bot.run("MTEzNjAwMzUxMTU0NTQ5OTc3OQ.G1nGkj.tWdI1pGTvjocll0dQtLOgcP2xA_LvcHVAcAklA")

