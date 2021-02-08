from enum import Enum


class Error(Enum):
    INVALID_GAME_CONFIGURATION = '[INVALID GAME CONFIGURATION] Error in the game configuration'


def throw(error: Error, reason: str):
    print(f'{error.value} ({reason})')
