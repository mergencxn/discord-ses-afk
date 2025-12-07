import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True  # Komut mesajlarını okuyabilmek için şart

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command(name='join')
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()

@bot.command(name='leave')
async def leave(ctx):
    await ctx.voice_client.disconnect()

# başka bir hesabının tokenini yazacaksın
bot.run("")
