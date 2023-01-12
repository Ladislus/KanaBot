from discord import Client, Message, Intents, Guild
from discord.utils import get

from .bot_config import BotConfiguration, get_bot_config

from utils import GUILD, Logger, ExitCode
from bot.command import Command, try_parse, COMMAND_SET, CommandInformation


class Bot(Client):
    _logger = Logger("BOT")

    def __init__(self, config_filepath: str, **options):
        # Option to enable list of members & message content
        intent: Intents = Intents.default()
        intent.members = True
        intent.message_content = True
        super().__init__(intents=intent, **options)

        self._config: BotConfiguration = get_bot_config(config_filepath)
        self._commands: dict[str, CommandInformation] = COMMAND_SET

    def __repr__(self):
        return f'{self._config}'

    def _get_guild(self) -> Guild:
        guild: Guild = get(super().guilds, name=GUILD)
        if guild is None:
            Bot._logger.error(f'could not find guild named {GUILD}, EXITING')
            exit(ExitCode.DISCORD_ERROR)

        return guild

    @property
    def config(self) -> BotConfiguration:
        return self._config

    @config.setter
    def config(self, value: BotConfiguration):
        if value and isinstance(value, BotConfiguration):
            self._config = value
        else:
            self._logger.error(f'Invalid value for config `{value}`')

    @property
    def commands(self) -> dict[str, CommandInformation]:
        return self._commands

    @commands.setter
    def commands(self, value: set[Command]):
        if value and isinstance(value, set):
            self._commands = value
        else:
            self._logger.error(f'Invalid value for commands `{value}`')

    async def on_ready(self):
        self._config.guild = self._get_guild()
        self._logger.log(f'`{super().user.name}` connected to `{self._config.guild.name}`')
        self._logger.log(f'{self._config}')

    async def on_message(self, message: Message):
        self._logger.debug(f'Receiver message: ({message.author.display_name}) => `{message.content}`')

        command: Command | None = try_parse(message, self.commands, self.config)
        if command:
            await command.execute()
