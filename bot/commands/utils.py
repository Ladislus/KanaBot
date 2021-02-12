from env import OWNER
from discord.abc import User


def is_owner(u: User) -> bool:
    """
    Function to check if the User passed in parameter is the owner of the bot
    :param u: The User to test
    :return: True if the user is the owner, False otherwise
    """
    return OWNER == f'{u.name}#{u.discriminator}'


def sanitize(s: str) -> str:
    """
    Function to remove leading and trailling spaces
    :param s: The string to sanitize
    :return: The sanitized string
    """
    return s.lstrip().rstrip().lower()


def isCommand(msg: str) -> bool:
    """
    Function to check if the message start with a '!' (remove spaces)
    :param msg: the message to test
    :return: True if the message starts with '!', False otherwise
    """
    return (sanitize(msg)[0] == '!') if len(msg) > 0 else False
