from config import GlobalConfig
from .logger import Logger
from .command import Command
from discord import Message, Client
from env import OWNER
from discord import Member

_logger: Logger = Logger('COMMAND CREATED')
_prefix: str = "!"


def parse(client: Client, msg: Message) -> Command:
    com_str: list[str] = msg.content.split(' ')
    name: str = _sanitize(com_str[0][1:])
    args: dict = {'args': []}
    argcount: int = 0
    optionalargcount: int = 0

    for i in range(1, len(com_str)):
        sanitized: str = _sanitize(com_str[i])
        if _isNamedArg(sanitized) and i < len(com_str) - 1:
            i += 1
            args[sanitized[2:]] = _sanitize(com_str[i])
            optionalargcount += 1
        else:
            argcount += 1
            args['args'].append(sanitized)

    _logger.log(f'Command "{msg.content}" created by user "{msg.author.name}" in channel "{msg.channel.name}"')
    return Command(client, msg.content, name, msg.author.name, msg.channel, argcount, optionalargcount, args)


def _isNamedArg(msg: str) -> bool:
    """
    Function to check if the message start with '--' (remove spaces)
    :param msg: the message to test
    :return: True if the message starts with '--', False otherwise
    """
    return (_sanitize(msg)[:2] == '--') if len(msg) > 0 else False


def _isOwner(u: Member) -> bool:
    """
    Function to check if the User passed in parameter is the owner of the bot
    :param u: The User to test
    :return: True if the user is the owner, False otherwise
    """
    return OWNER == f'{u.name}#{u.discriminator}'


def _sanitize(s: str) -> str:
    """
    Function to remove leading and trailling spaces
    :param s: The string to sanitize
    :return: The sanitized string
    """
    return s.lstrip().rstrip().lower()


def _isCommand(msg: str) -> bool:
    """
    Function to check if the message start with a '!' (remove spaces)
    :param msg: the message to test
    :return: True if the message starts with '!', False otherwise
    """
    return (_sanitize(msg)[0] == _prefix) if len(msg) > 0 else False


def isValidCommand(msg: Message, globalCfg: GlobalConfig) -> bool:
    """
    Function to check if a message is a command, and if it's authorized
    :param msg: The message to check
    :param globalCfg: The configuration file
    :return: True if the message should be interpreted as a command, False otherwise
    """

    return globalCfg.activated and \
           _isCommand(msg.content) and \
           msg.channel.name in globalCfg.channels and \
           (not globalCfg.adminRequired or (msg.author.id in globalCfg.admins or _isOwner(msg.author)))
