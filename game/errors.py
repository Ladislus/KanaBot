from enum import Enum
from utils import Logger

_logger: Logger = Logger('GAME ERROR')


class GameError(Enum):
    INVALID_GAME_CONFIGURATION = '-= INVALID GAME CONFIGURATION =- Error in the game configuration'


def throw(error: GameError, reason: str) -> None:
    """
    Function to print an error related to the bot
    :param error: The type of error
    :param reason: The details of the error
    """
    _logger.log(f'{error.value} ({reason})')
