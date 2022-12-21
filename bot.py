import discord
import responses

"""
This code runs a Discord bot with an AI that responds to user input. 
The 'send_message' function defines how the program responds to the user by processing the 
    input message and sending a response.
The client.run() method is used to run the bot with the provided token.
"""


async def send_message(message, user_message, is_private):
    try:
        response = responses.get_response(user_message)
        await message.channel.send(response) if is_private else await message.author.send(response)

    except Exception as e:
        print(e)


def run_discord_bot() -> object:
    TOKEN = 'MTA1NDkxNTQ0NzkxODY5ODU0Ng.GIOe2_.NoWuOMycdtueDxc7xS8xeLkOSf7-JS4XVKfI4A'
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} just showed up!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} said "{user_message}" in {channel}')

        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

    client.run(TOKEN)
