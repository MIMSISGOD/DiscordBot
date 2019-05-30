import discord


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


client.run("NTU4MjY5ODk4OTQyMzE2NTU0.XO1Bwg.SIJjWBzL9Zac3vfpg9-MVkfHi7o")
