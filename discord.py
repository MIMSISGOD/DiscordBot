import discord
import os


client = discord.Client()


@client.event
async def on_ready():
    print("login")
    print(client.user.name)
    print(client.user.id
    print("ready")
    await client.change_presence(game=discord.Game(name``,type=1))

@client.event
async def on_message(message):
    if message.content.startswith("*Help"):
        await message.channel.send("바빠")
          

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
