from config import GameConfig
from .errors import throw, GameError
from enum import Enum, auto
from commands import Logger


class GameStatus(Enum):
    CONFIGURATION = auto()
    QUESTION = auto()
    RESPONDING = auto()
    CORRECTING = auto()
    WAITING = auto()
    END = auto()


class Game:
    _logger = Logger("GAME")

    def __init__(self, gameConfig: GameConfig):
        self._gameConfig = gameConfig
        self._status: GameStatus = GameStatus.CONFIGURATION
        self._currentQuestion = 1
        self._scores = {}

    def __repr__(self):
        return f'Game settings :\n\
            \tStatus: {self._status.name}\n\
            \tCurrent question number: {self._currentQuestion}\n\
            {self._gameConfig}'

    def play(self):
        self._status = GameStatus.QUESTION

    def start(self):
        self._currentQuestion = 1
        if self._currentQuestion <= self._gameConfig.questions:
            if self._gameConfig.hiraganaActivated or self._gameConfig.katakanaActivated:
                self.play()
            else:
                throw(GameError.INVALID_GAME_CONFIGURATION, 'Aucun des deux alphabets n\'est activé')
        else:
            throw(GameError.INVALID_GAME_CONFIGURATION, 'Le nombre de partie est inférieur à 1')
