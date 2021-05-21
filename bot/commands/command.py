from discord import TextChannel, Client
from .logger import Logger
from .commands import commands, Element, Option


class Command:
    _logger: Logger = Logger('COMMAND EXECUTION')
    _commands: dict = commands

    def __init__(self,
                 client: Client,
                 rawCommand: str,
                 name: str,
                 author: str,
                 channel: TextChannel,
                 argCount: int,
                 optionalArgCount: int,
                 args: dict):
        self._client: Client = client
        self._rawCommand: str = rawCommand
        self._name: str = name
        self._author: str = author
        self._channel: TextChannel = channel
        self._argCount: int = argCount
        self._optionalArgCount: int = optionalArgCount
        self._args: dict = args

    def __repr__(self) -> str:
        return f'Command: \n\
            \tRaw: {self._rawCommand}\n\
            \tName: {self._name}\n\
            \tAuthor: {self._author}\n\
            \tChannel: {self._channel.name}\n\
            \tArgCount: {str(self._argCount)}\n\
            \tOptionalArgCount: {str(self._optionalArgCount)}\n\
            \tArgs: {self._args}\n'

    async def execute(self):
        # TODO more tests
        # TODO Split into smaller methods
        if self._name not in Command._commands:
            Command._logger.log(f'Command "{self._name}" dosen\'t exist')
        else:
            command_infos: dict = Command._commands[self._name]

            if self._argCount < command_infos[Option.ARGUMENT_REQUIRED]:
                Command._logger.log(f'Command "{self._name}" requires {str(command_infos[Option.ARGUMENT_REQUIRED])}, '
                                    f'only {str(self._argCount)} given')
            elif self._argCount > command_infos[Option.ARGUMENT_REQUIRED] and not command_infos[Option.VARARGS_SUPPORTED]:
                Command._logger.log(f'Command "{self._name}" requires {str(command_infos[Option.ARGUMENT_REQUIRED])}, '
                                    f'but {str(self._argCount)} were given ({self._args})')
            else:
                # TODO Check named args
                elements: dict[Element, object] = self._retrieve_elements(command_infos[Option.ELEMENT_REQUIRED])
                await Command._commands[self._name][Option.FUNCTION](self._args, elements)
                Command._logger.log(f'{self._rawCommand} executed')

    def _retrieve_elements(self, command_elements: list[Element]) -> dict[Element, object]:
        elements: dict[Element, object] = {}
        # TODO check for other elements
        if Element.CHANNEL in command_elements:
            elements[Element.CHANNEL] = self._channel
        if Element.USERS in command_elements:
            elements[Element.USERS] = self._client.config.guild.members
        return elements
