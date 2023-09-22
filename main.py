import discord
import discord.ext
from discord.ext import commands

intents = discord.Intents.all() 
#client = discord.Client(intents=intents)
client = commands.Bot(command_prefix = "+",intents=discord.Intents.all())
#tree = discord.app_commands.CommandTree(client)
guild = discord.Object(id=1154614970676412446)

# sync the slash command to your server
@client.event
async def on_ready():
    print("ready")

@client.command(aliases = ["sync"])
async def synchronise(ctx):
    print("synchronising")
    await ctx.send("Synchonising...")
    await client.tree.sync(guild=guild)
    await ctx.send("Commands synchonised!")
    print("synced")

# make the slash command
@client.tree.command(name="name", description="description")
async def slash_command(interaction: discord.Interaction, test : str):    
    await interaction.response.send_message("command",test)

@client.tree.command(name="solve",description="solve a math equation")
async def solve(interaction : discord.Interaction):
    pass


client.run('MTE1NDYxMjQ5ODAyMDk2MjMyNA.GAggS6.hEG38XxfI0VfglZ3RSujbeSBjNpAn0AspBxQn4')
