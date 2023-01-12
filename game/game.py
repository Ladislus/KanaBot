from enum import Enum, auto

from .game_config import GameConfiguration

from utils import Logger, ExitCode, todo


class GameStatus(Enum):
    CONFIGURATION = auto()
    QUESTION = auto()
    RESPONDING = auto()
    CORRECTING = auto()
    WAITING = auto()
    END = auto()


ScoreType: type = dict[str, int]


class Game:
    _logger = Logger("GAME")

    def __init__(self, game_config: GameConfiguration):
        self._config: GameConfiguration = game_config
        self._status: GameStatus = GameStatus.CONFIGURATION
        self._question_number: int = 1
        self._scores: ScoreType = {}

    def __repr__(self):
        return f'Game settings :\n\
            \tStatus: {self._status.name}\n\
            \tCurrent question number: {self._question_number}\n\
            {self._config}'

    def _validate_config(self):
        if not (self._config.hiragana_activated or self._config.katakana_activated):
            self._logger.error('No alphabet selected')
            exit(ExitCode.GAME_ERROR)

        if self._question_number > self._config.question_count:
            self._logger.error('Invalid question count')
            exit(ExitCode.GAME_ERROR)

    def play(self):
        self._status = GameStatus.QUESTION
        todo("Game::play() not implemented")

    def start(self):
        self._question_number = 1

        self._validate_config()

        self.play()
