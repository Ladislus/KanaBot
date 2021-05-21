from time import time
from discord import TextChannel
from discord.utils import get
from typing import Callable, Optional, Any, Tuple
from enum import Enum, auto
from utils import Logger

F = Callable[[...], Tuple[bool, str]]


class CommandElement(Enum):
    ARGUMENT_REQUIRED = auto()
    ELEMENT_REQUIRED = auto()
    VARARGS = auto()
    NAMED_ARGUMENTS = auto()
    DESCRIPTION = auto()
    FUNCTION = auto()


C = dict[str, dict[CommandElement, Any]]


class DiscordElement(Enum):
    CHANNEL = auto()
    USERS = auto()
    GAME = auto()


_start: time = time()
commands: C = dict()
_logger = Logger("COMMAND CREATOR")


def register(
        name: str,
        description: str = "",
        arguments: int = 0,
        elements: Optional[list[DiscordElement]] = None,
        varargs: bool = False,
        named: Optional[list[str]] = None) -> Callable[[...], F]:
    if elements is None:
        elements = [DiscordElement.CHANNEL]

    def wrapper(function: F) -> F:
        if name in commands:
            _logger.log(f'Command {name} already defined, skipping')
        else:
            commands[name] = {
                CommandElement.DESCRIPTION: description,
                CommandElement.ARGUMENT_REQUIRED: arguments,
                CommandElement.ELEMENT_REQUIRED: elements,
                CommandElement.VARARGS: varargs,
                CommandElement.NAMED_ARGUMENTS: named,
                CommandElement.FUNCTION: function
            }
        return function

    return wrapper


@register(
    name="help",
    description="Command pour obtenir la liste des commandes")
async def help(args: dict, elements: dict) -> (bool, str):
    channel: TextChannel = elements[DiscordElement.CHANNEL]
    if channel is None:
        return False, f'Command: {__name__}, Error: "Channel is None"'
    msg: str = ""
    for name, options in commands.items():
        msg += f'\t*{name}* :\n\t\t{options[CommandElement.DESCRIPTION]}\n'
    await channel.send(f'**Liste des commandes**:\n{msg}')
    return True, ""


@register(
    name="uptime",
    description="Command pour obtenir le temps de fonctionnement de billy")
async def uptime(args: dict, elements: dict) -> (bool, str):
    channel: TextChannel = elements[DiscordElement.CHANNEL]
    if channel is None:
        return False, f'Command: {__name__}, Error: "Channel is None"'
    await channel.send(f'uptime: {int(time() - _start)}s')
    return True, ""


@register(
    name="ladislas",
    description="J'suis juste le meilleur en fait")
async def ladislas(args: dict, elements: dict) -> (bool, str):
    channel: TextChannel = elements[DiscordElement.CHANNEL]
    if channel is None:
        return False, f'Command: {__name__}, Error: "Channel is None"'
    await channel.send('Ladislus est un homme magnifique')
    return True, ""


@register(
    name="enculai",
    description="il mérite**rai**",
    elements=[DiscordElement.CHANNEL, DiscordElement.USERS])
async def enculai(args: dict, elements: dict) -> (bool, str):
    channel: TextChannel = elements[DiscordElement.CHANNEL]
    if channel is None:
        return False, f'Command: {__name__}, Error: "Channel is None"'
    mention: str = get(elements[DiscordElement.USERS], name='Dwindwin').mention
    if mention is None:
        return False, f'Command: {__name__}, Error: "Mention is None"'
    await channel.send(f'{mention}: tg encul**ai**')
    return True, ""
