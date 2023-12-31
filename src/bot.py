import discord
import responses

async def send_message(message, user_message):
    try:
        response = responses.handle_response(user_message)
        await message.channel.send(response)
    except Exception as e:
        await message.author.send("Error: " + str(e))

def run_bot():
    TOKEN = '' # Add your bot token here
    intents = discord.Intents.default()
    intents.message_content = True  # Enable this if you need to access message content
    
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is runniung')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel.name)

        if channel != "bot":
            return
 
        print(f"{username} said: '{user_message}' ({channel})")

        await send_message(message, user_message)

    client.run(TOKEN)