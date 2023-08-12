import discord
from discord.ext import commands
from createTeams import CreateTeams
from massMessage import MassMessage
from createMatchday import CreateMatchday

bot = commands.Bot(command_prefix="/", intents=discord.Intents.all())

@bot.event
async def on_ready():
    await bot.add_cog(CreateTeams(bot))
    await bot.add_cog(CreateMatchday(bot))
    await bot.add_cog(MassMessage(bot))
    synced = await bot.tree.sync()
    print(f"Synced {len(synced)} command(s).")
    print ("Tournament Admin is online")

@bot.tree.command(name="hello")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message("Hello " + interaction.user.mention)

bot.run("MTEzNjAwMzUxMTU0NTQ5OTc3OQ.G1nGkj.tWdI1pGTvjocll0dQtLOgcP2xA_LvcHVAcAklA")

