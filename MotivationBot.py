import discord
import Response
from discord import app_commands
from discord.ext import commands
from discord import Interaction
# from discord import commands
# import interactions
# from discord_slash import SlashCommand
async def send_message(message, user_message, is_private):
    try:
        response= Response.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

def run_discord_bot():
    TOKEN = 'MTE3MzU4MTQ2NDczMDg4MjE3OA.GZcHe0.eO80EVJwa2r5I1zsh9XaDnzYKLm7C3rqBK9aYg'

    # intents = discord.Intents.default()
    # intents.message_content = True
    # client = discord.Client(intents=intents)
    # tree = app_commands.CommandTree(client)
    client = commands.Bot(command_prefix=".", intents= discord.Intents.all())

    @client.event
    async def on_ready():
        await client.tree.sync()
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f"{username} said: '{user_message}' ({channel})")

        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

    # bot= commands.Bot(command_prefix="!", intents= discord.Intents.all())
    # bot= discord.Client(intents=intents)
    # tree = app_commands.CommandTree(bot)

    # @bot.event
    # async def on_ready():
    #     print("Bot is up and ready!")
    #     try:
    #         synced = await bot.tree.sync()
    #         print(f"Synced {len(synced)} command(s)")
    #     except Exception as e:
    #         print(e)
    
    @client.tree.command(name= "hello")
    async def hello(interaction: discord.Interaction):
        await interaction.response.send_message(f"Hey {interaction.user.mention}! This is a slash command!", ephemeral=True)

    @client.tree.command(name= "say")
    @app_commands.describe(thing_to_say = "What should I say?")
    async def say(interaction: discord.Interaction, thing_to_say: str):
        await interaction.response.send_message(f"{interaction.user.name} said: '{thing_to_say}'")
    
    client.run(TOKEN)
    # bot.run(TOKEN)