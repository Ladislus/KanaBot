from enum import Enum


class ExitCode(Enum):
    KILL_COMMAND = 0
    CONFIG_ERROR = 1
    DISCORD_ERROR = 2
    INJECTOR_ERROR = 4
