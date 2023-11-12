import discord
import responses

async def send_message(message, user_message):
    try:
        response = responses.handle_response(user_message)
        await message.channel.send(response)
    except Exception as e:
        await message.author.send("Error: " + str(e))

def run_bot():
    TOKEN = 'ODA3NjgxNzI1NDM3NTc1MTk4.G_XkJP.5ApyftfwgnFgAb7sVi9OO7Sr-XJcupQyfeRQSg'
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

        print(f'{username}: {user_message} 'in' ({channel})')

        await send_message(message, user_message)

    client.run(TOKEN)