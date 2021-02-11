from config.globalconfig import GlobalConfig
from .commands.command import Command
from discord import Client, Message
from discord.utils import get
from .commands.commandparser import Parser
from env import GUILD


class Bot(Client):
    def __init__(self, config: GlobalConfig, **options):
        super().__init__(**options)
        self._config: GlobalConfig = config

    def __repr__(self):
        return f'{self._config}'

    async def on_ready(self, ):
        # Problem while fetching the discord guild
        guild = get(super().guilds, name=GUILD)
        if guild is None:
            exit()
        # Else, save the guild informations
        self._config._guild = guild

        print(f'{super().user.name} is connected to the following guild: {guild.name}\n')
        print(self._config)

    async def on_message(self, msg: Message):
        if Command.isValidCommand(msg, self._config):
            com: Command = Parser.parse(msg)
            com.execute()
