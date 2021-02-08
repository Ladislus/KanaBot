from enum import Enum


class Error(Enum):
    INVALID_GAME_CONFIGURATION = '[INVALID GAME CONFIGURATION] Error in the game configuration'


def throw(error: Error, reason: str):
    """
    Function to print an error related to the bot
    :param error: The type of error
    :param reason: The details of the error
    """
    print(f'{error.value} ({reason})')
