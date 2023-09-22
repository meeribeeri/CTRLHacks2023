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
    await client.tree.sync(guild=guild)
    print("ready")

@client.command(aliases = ["sync"])
async def synchronise(ctx):
    print("synchronising")
    await client.tree.sync(guild=guild)
    await ctx.send("Synchonised!")
    print("synced")

# make the slash command
@client.tree.command(name="name", description="description")
async def slash_command(interaction: discord.Interaction, test : discord.app_commands.Range[int,0,100]):    
    await interaction.response.send_message("command")

client.run('MTE1NDYxMjQ5ODAyMDk2MjMyNA.GAggS6.hEG38XxfI0VfglZ3RSujbeSBjNpAn0AspBxQn4')
