from discord import Client, Message
from discord.utils import get
from config import globalconfig
from env import TOKEN, GUILD
from utils import validate


client = Client()

globalCfg = globalconfig.from_file()


@client.event
async def on_ready():
    guild = get(client.guilds, name=GUILD)

    if guild is None:
        exit()

    globalCfg._guild = guild

    print(f'{client.user.name} is connected to the following guild: {guild.name}\n')
    print(globalCfg)


@client.event
async def on_message(msg: Message):
    if validate(msg, globalCfg):
        print('ok')


client.run(TOKEN)
