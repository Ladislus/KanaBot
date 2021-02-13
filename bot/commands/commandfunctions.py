from .commandelement import Element
from discord import TextChannel
from discord.utils import get


async def test(args: dict, elements: dict):
    chan: TextChannel = elements[Element.CHANNEL]
    await chan.send("Niquez vos race**s** (Oui, je pense à toi enculai) avec les tests")


async def enculai(args: dict, elements: dict):
    chan: TextChannel = elements[Element.CHANNEL]
    mention: str = get(elements[Element.USERS], name='Dwindwin').mention
    if mention is not None:
        await chan.send(f'{mention}: tg encul**ai**')


async def ladislas(args: dict, elements: dict):
    chan: TextChannel = elements[Element.CHANNEL]
    await chan.send('Ladislus est un homme magnifique')
