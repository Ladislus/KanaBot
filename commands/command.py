from discord import Message
from utils import sanitize, isOptionalArg


def parser(com: list[str]) -> dict:
    args = {'args': []}
    for i in range(len(com)):
        sanitized: str = sanitize(com[i])
        if isOptionalArg(sanitized) and i < len(com) - 1:
            i += 1
            args[sanitized[2:]] = com[i]
        else:
            args['args'].append(sanitized)
    return args


class Command:
    def __init__(self, msg: Message):
        com: list[str] = msg.content.split(' ')
        self._name: str = com[0][1:]
        self._author: str = msg.author.name
        self._channel: str = msg.channel.name
        self._args: dict = parser(com[1:])

    def __repr__(self) -> str:
        return f'Command: \n\
            \tName: {self._name}\n\
            \tAuthor: {self._author}\n\
            \tChannel: {self._channel}\n\
            \tArgs: {self._args}\n'
