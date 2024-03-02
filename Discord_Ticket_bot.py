import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='Your messages'))
    print(f'Bot is ready. Logged in as {bot.user}')

@bot.event
async def on_message(message):
    if isinstance(message.channel, discord.DMChannel) and not message.author.bot:
        user_id = YOUR_USER_ID
        user = await bot.fetch_user(user_id)
        await user.send(f"**{message.author}** said: {message.content}")
    await bot.process_commands(message)

bot.run('YOUR_BOT_TOKEN')
