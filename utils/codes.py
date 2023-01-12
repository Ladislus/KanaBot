from enum import Enum


class ExitCode(Enum):
    TODO = -1
    KILL_COMMAND = 0
    CONFIG_ERROR = 1
    DISCORD_ERROR = 2
    GAME_ERROR = 3
    COMMAND_ERROR = 4


def todo(message: str):
    print(message)
    exit(ExitCode.TODO)
