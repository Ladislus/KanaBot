from discord import TextChannel
from discord.utils import get
from typing import Callable, Optional, Any
from enum import Enum, auto

F = Callable[[...], None]


class Option(Enum):
    ARGUMENT_REQUIRED = auto()
    ELEMENT_REQUIRED = auto()
    VARARGS_SUPPORTED = auto()
    NAMED_ARGUMENTS = auto()
    FUNCTION = auto()


class Element(Enum):
    CHANNEL = auto()
    USERS = auto()
    GAME = auto()


commands: dict[str, dict[Option, Any]] = dict()


def register(
        name: str,
        arguments: int,
        elements: list[Element],
        varargs: bool = False,
        named: Optional[list[str]] = None) -> Callable[[...], F]:
    def wrapper(function: F) -> F:
        assert name not in commands
        commands[name] = {
            Option.ARGUMENT_REQUIRED: arguments,
            Option.ELEMENT_REQUIRED: elements,
            Option.VARARGS_SUPPORTED: varargs,
            Option.NAMED_ARGUMENTS: named,
            Option.FUNCTION: function
        }
        return function

    return wrapper


@register(
    name="test",
    arguments=0,
    elements=[Element.CHANNEL])
async def test(args: dict, elements: dict):
    channel: TextChannel = elements[Element.CHANNEL]
    await channel.send("Niquez vos race**s** (Oui, je pense à toi enculai) avec les tests")


@register(
    name="ladislas",
    arguments=0,
    elements=[Element.CHANNEL])
async def ladislas(args: dict, elements: dict):
    channel: TextChannel = elements[Element.CHANNEL]
    await channel.send('Ladislus est un homme magnifique')


@register(
    name="enculai",
    arguments=0,
    elements=[Element.CHANNEL, Element.USERS])
async def enculai(args: dict, elements: dict):
    channel: TextChannel = elements[Element.CHANNEL]
    mention: str = get(elements[Element.USERS], name='Dwindwin').mention
    if mention is not None:
        await channel.send(f'{mention}: tg encul**ai**')


@register(
    name="tomeu",
    arguments=0,
    elements=[Element.CHANNEL, Element.USERS])
async def enculai(args: dict, elements: dict):
    channel: TextChannel = elements[Element.CHANNEL]
    mention: str = get(elements[Element.USERS], name='tom99').mention
    if mention is not None:
        await channel.send(f'{mention}: Tu veux quoi TOMEU !')


@register(
    name="patapé",
    arguments=0,
    elements=[Element.CHANNEL])
async def enculai(args: dict, elements: dict):
    channel: TextChannel = elements[Element.CHANNEL]
    await channel.send(f'#patapé\nhttps://giphy.com/gifs/nouveaucinema-fnc-fnc2019-newcinema-daVAZonLPwv6ThjVX2')
