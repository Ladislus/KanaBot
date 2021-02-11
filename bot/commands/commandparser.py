from .utils import sanitize
from .logger import Logger
from .command import Command
from discord import Message


class Parser:
    _logger: Logger = Logger('COMMAND CREATED')

    @staticmethod
    def parse(msg: Message) -> Command:
        com_str: list[str] = msg.content.split(' ')
        name: str = sanitize(com_str[0][1:])
        args: dict = {'args': []}
        argcount: int = 0
        optionalargcount: int = 0

        for i in range(1, len(com_str)):
            sanitized: str = sanitize(com_str[i])
            if Parser._isNamedArg(sanitized) and i < len(com_str) - 1:
                i += 1
                args[sanitized[2:]] = sanitize(com_str[i])
                optionalargcount += 1
            else:
                argcount += 1
                args['args'].append(sanitized)

        Parser._logger.log(f'Command "{msg.content}" created by user "{msg.author.name}" in channel "{msg.channel.name}"')
        return Command(msg.content, name, msg.author.name, msg.channel.name, argcount, optionalargcount, args)

    @staticmethod
    def _isNamedArg(msg: str) -> bool:
        """
        Function to check if the message start with '--' (remove spaces)
        :param msg: the message to test
        :return: True if the message starts with '--', False otherwise
        """
        return (sanitize(msg)[:2] == '--') if len(msg) > 0 else False
