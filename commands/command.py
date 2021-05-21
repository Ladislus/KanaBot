from discord import TextChannel, Client
from utils.logger import Logger
from .commands import commands, DiscordElement, CommandElement


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
            command_infos: dict = self._commands[self._name]

            if self._argCount < command_infos[CommandElement.ARGUMENT_REQUIRED]:
                Command._logger.log(f'Command "{self._name}" requires {str(command_infos[CommandElement.ARGUMENT_REQUIRED])}, '
                                    f'only {str(self._argCount)} given')
            elif self._argCount > command_infos[CommandElement.ARGUMENT_REQUIRED] and not command_infos[CommandElement.VARARGS]:
                Command._logger.log(f'Command "{self._name}" requires {str(command_infos[CommandElement.ARGUMENT_REQUIRED])}, '
                                    f'but {str(self._argCount)} were given ({self._args})')
            else:
                # TODO Check named args
                elements: dict[DiscordElement, object] = self._retrieve_elements(command_infos[CommandElement.ELEMENT_REQUIRED])
                result: (bool, str) = await Command._commands[self._name][CommandElement.FUNCTION](self._args, elements)
                if result[0]:
                    Command._logger.log(f'"{self._rawCommand}" executed with success')
                else:
                    Command._logger.log(f'"{self._rawCommand}" error: {result[1]}')

    def _retrieve_elements(self, command_elements: list[DiscordElement]) -> dict[DiscordElement, object]:
        elements: dict[DiscordElement, object] = {}
        # TODO check GAME
        if DiscordElement.CHANNEL in command_elements:
            elements[DiscordElement.CHANNEL] = self._channel
        if DiscordElement.USERS in command_elements:
            elements[DiscordElement.USERS] = self._client.config.guild.members
        return elements
