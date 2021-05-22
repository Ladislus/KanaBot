from typing import Any, Optional
from discord import TextChannel, Client

from config import GlobalConfig
from utils import Logger, OWNER, ExitCode, Injector
from .commands import commands, DiscordElement, CommandElement

defaultArgName: str = "args"


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
        if self._name not in Command._commands:
            Command._logger.log(f'Command "{self._name}" dosen\'t exist')
        else:
            infos: dict[CommandElement, Any] = self._commands[self._name]

            if not self._hasPermission(infos):
                Command._logger.log(
                    f'Error: command "{self._name}" require admin privileges, but "{self._author}" is not')
            else:
                if not self._hasArguments(infos):
                    Command._logger.log(
                        f'Command "{self._name}" requires {str(infos[CommandElement.ARGUMENT_REQUIRED])} arguments, '
                        f'{str(self._argCount)} given')
                else:
                    success, error = self._checkNamedArgs(infos)
                    if not success:
                        if error == "":
                            Command._logger.log(
                                f'Command "{self._name}" dosen\'t support named arguments')
                        else:
                            Command._logger.log(
                                f'Command "{self._name}" recognize named argument "{error}"')
                    else:
                        elements: dict[DiscordElement, object] = self._retrieve_elements(
                            infos[CommandElement.ELEMENT_REQUIRED])
                        execution, error = await Command._commands[self._name][CommandElement.FUNCTION](self._args,
                                                                                                        elements)
                        if execution:
                            Command._logger.log(f'"{self._rawCommand}" executed with success')
                        else:
                            Command._logger.log(f'"{self._rawCommand}" error: {error}')

    def _hasPermission(self, infos: dict[CommandElement, Any]) -> bool:
        config: Optional[GlobalConfig] = Injector.getConfig()
        if config is None:
            Command._logger.log(f'Couldn\'t get {GlobalConfig} from Injector')
            exit(ExitCode.INJECTOR_ERROR)
        if config.adminRequired or infos[CommandElement.ADMIN]:
            return (self._author in config.admins) or self._author == OWNER
        return True

    def _hasArguments(self, infos: dict[CommandElement, Any]) -> bool:
        return (infos[CommandElement.VARARGS] and self._argCount >= infos[CommandElement.ARGUMENT_REQUIRED]) or \
               self._argCount == infos[CommandElement.ARGUMENT_REQUIRED]

    def _checkNamedArgs(self, infos: dict[CommandElement, Any]) -> (bool, str):
        if len(infos[CommandElement.NAMED_ARGUMENTS]) > 0:
            for key in self._args.keys():
                if key != defaultArgName and key not in infos[CommandElement.NAMED_ARGUMENTS]:
                    return False, key
                return True, ""
        else:
            return self._optionalArgCount == 0, ""

    def _retrieve_elements(self, command_elements: list[DiscordElement]) -> dict[DiscordElement, object]:
        elements: dict[DiscordElement, object] = {}
        # TODO check GAME
        if DiscordElement.CHANNEL in command_elements:
            elements[DiscordElement.CHANNEL] = self._channel
        if DiscordElement.USERS in command_elements:
            config: Optional[GlobalConfig] = Injector.getConfig()
            if config is None:
                Command._logger.log(f'Couldn\'t get {GlobalConfig} from Injector')
                exit(ExitCode.INJECTOR_ERROR)
            elements[DiscordElement.USERS] = config.guild.members
        return elements
