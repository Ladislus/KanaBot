from env import OWNER
from config.globalconfig import GlobalConfig
from discord import Message
from discord.abc import User


def is_owner(u: User) -> bool:
    """
    Function to check if the User passed in parameter is the owner of the bot
    :param u: The User to test
    :return: True if the user is the owner, False otherwise
    """
    return OWNER == f'{u.name}#{u.discriminator}'


def is_command(msg: str) -> bool:
    """
    Function to check if the message start with a '!' (remove spaces)
    :param msg: the message to test (discord.Message)
    :return: True if the message starts with '!', False otherwise
    """
    return msg.lstrip()[0] == '!'


def isValidCommand(msg: Message, globalCfg: GlobalConfig) -> bool:
    """
    Function to check if a message is a command, and if it's authorized
    :param msg: The message to check
    :param globalCfg: The configuration file
    :return: True if the message should be interpreted as a command, False otherwise
    """
    return globalCfg.activated and \
        is_command(msg.content) and \
        msg.channel.name in globalCfg.channels and \
        (not globalCfg.adminRequired or (msg.author.id in globalCfg.admins or is_owner(msg.author)))
