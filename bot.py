from discord import Client, Message
from discord.utils import get
from config import globalconfig
from utils import validate
import env


client = Client()

globalCfg = globalconfig.from_file()


@client.event
async def on_ready():
    # Problem while fetching the discord guild
    guild = get(client.guilds, name=env.GUILD)
    if guild is None:
        exit()
    # Else, save the guild informations
    globalCfg._guild = guild

    print(f'{client.user.name} is connected to the following guild: {guild.name}\n')
    print(globalCfg)


@client.event
async def on_message(msg: Message):
    if validate(msg, globalCfg):
        print('ok')


client.run(env.TOKEN)
