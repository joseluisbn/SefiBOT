from datetime import datetime
import discord
from discord.ext import commands
from matplotlib.pyplot import title

# Add a prefix to command bot in Discord
bot = commands.Bot(command_prefix='!', description="Hi all, I'm SefiBOT, your robotic friend")

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

# About. Some examples
@bot.command()
async def about(ctx):
    embed = discord.Embed(title = f"{ctx.guild.name}", description = "SefiBOT, developed by **BleizeN**", timestamp=datetime.utcnow(), color = discord.Color.blue())
    embed.add_field(name="Server created by testing proposals at", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Server owner", value=f"{ctx.guild.owner}")
    embed.add_field(name="Server region", value=f"{ctx.guild.region}")  
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
    embed.set_thumbnail(url="https://pbs.twimg.com/profile_images/1401793142324699136/ECowi4TP_400x400.jpg")
    await ctx.send(embed = embed)

# Event on connect
@bot.event
async def on_ready():
    # await bot.change_presence(activity="busy")
    print("SefiBOT is connected. Prepare your materia")

bot.run('<YOUR ID>')