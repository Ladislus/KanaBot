from enum import Enum, auto


class GameStatus(Enum):
    CONFIGURATION = auto()
    QUESTION = auto()
    RESPONDING = auto()
    CORRECTING = auto()
    WAITING = auto()
    END = auto()
