from discord import TextChannel, Message, User

from .registerer import CommandSetType, CommandInformation

from utils import Logger


class Command:
    _logger: Logger = Logger('COMMAND')

    def __init__(self,
                 command_name: str,
                 author: User,
                 channel: TextChannel,
                 raw_content: str,
                 info: CommandInformation):
        self._raw_message: str = raw_content
        self._name: str = command_name
        self._author: User = author
        self._channel: TextChannel = channel
        self._info: CommandInformation = info

    def __repr__(self) -> str:
        return f'Command: \n\
            \tRaw: `{self._raw_message}`\n\
            \tCommand: `{self._name}`\n\
            \tAuthor: {self._author.display_name}\n\
            \tChannel: {self._channel.name}\n'

    @staticmethod
    def is_valid(message: str, command_prefix: str) -> bool:
        return message[0] == command_prefix

    # TODO: Check permission
    def _has_permission(self):
        pass

    async def execute(self):
        result: bool = await self._info.function(self)
        pass

    @property
    def channel(self) -> TextChannel:
        return self._channel

    @property
    def author(self) -> User:
        return self._author

    @property
    def logger(self):
        return self._logger


# TODO: specify config type
def try_parse(message: Message, known_commands: CommandSetType, config) -> Command | None:

    _logger: Logger = Logger('COMMAND PARSER')

    author: User = message.author
    content: str = message.content.strip()
    channel: TextChannel = message.channel

    if not Command.is_valid(content, config.command_prefix):
        _logger.debug(f'`{content}` is not a valid command')
        return

    command_name = content.split(' ')[0][1:]
    if command_name not in known_commands.keys():
        _logger.debug(f'Unknown command `{command_name}`')
        return

    command_info: CommandInformation = known_commands[command_name]

    return Command(command_name, author, channel, content, command_info)

