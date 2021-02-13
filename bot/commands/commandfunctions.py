from .commandelement import Element
from discord import TextChannel


async def test(args: dict, elements: dict[Element, object]):
    chan: TextChannel = elements[Element.CHANNEL]
    await chan.send("Niquez vos race**s** (Oui, je pense à toi enculai) avec les tests")
