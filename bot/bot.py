from config.globalconfig import GlobalConfig
from .commands.command import Command
from discord import Client, Message, Intents
from discord.utils import get
from .commands.commandparser import Parser
from env import GUILD


class Bot(Client):
    def __init__(self, config: GlobalConfig, **options):
        # Option to enable list of members
        intent: Intents = Intents.default()
        intent.members = True
        super().__init__(intents=intent, **options)
        self._config: GlobalConfig = config

    def __repr__(self):
        return f'{self._config}'

    @property
    def config(self):
        return self._config

    async def on_ready(self, ):
        # Problem while fetching the discord guild
        guild = get(super().guilds, name=GUILD)
        print(guild.members)
        if guild is None:
            exit()
        # Else, save the guild informations
        self._config._guild = guild

        print(f'{super().user.name} is connected to the following guild: {guild.name}\n')
        print(self)

    async def on_message(self, msg: Message):
        if Command.isValidCommand(msg, self._config):
            com: Command = Parser.parse(self, msg)
            await com.execute()
