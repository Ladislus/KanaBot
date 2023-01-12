from configparser import ConfigParser

from .character import AlphabetType, CategoryType, CharacterSetType, HIRAGANA_DICTIONARY, KATAKANA_DICTIONARY

from utils import Logger, ExitCode, as_bool, as_int


class GameConfiguration:
    _logger: Logger = Logger('GAME CONFIGURATION')

    def __init__(self,
                 hiragana_activated: bool = True,
                 katakana_activated: bool = False,
                 manuel_step: bool = True,
                 response_time: int = 10,
                 question_count: int = 5,
                 proposition_count: int = 3,
                 delay: int = 10):
        self._hiragana_activated: bool = hiragana_activated
        self._hiragana_set: CharacterSetType = {}
        self._katakana_activated: bool = katakana_activated
        self._katakana_set: CharacterSetType = {}
        self._manual_stepping: bool = manuel_step
        self._response_time: int = response_time
        self._question_count: int = question_count
        self._proposition_count: int = proposition_count
        self._delay: int = delay

    def __repr__(self) -> str:
        return f'Game config: \n\
            \tHiragana activated: {self._hiragana_activated}\n\
            \tHiragana set: {self._hiragana_set}\n\
            \tKatakana activated: {self._katakana_activated}\n\
            \tKatakana set: {self._katakana_set}\n\
            \tManual stepping: {self._manual_stepping}\n\
            \tResponse time: {self._response_time}s\n\
            \tNumber of questions: {self._question_count}\n\
            \tNumber of propositions: {self._proposition_count}\n\
            \tDelay between questions: {self._delay}s\n'

    def _add_hiragana_category(self, family: AlphabetType, category: CategoryType | list[CategoryType] | None = None):
        match category:
            case list() as category_list:
                for category in category_list:
                    self._add_hiragana_category(family, category)
            case CategoryType() as single_category:
                for hiragana, romaji in HIRAGANA_DICTIONARY[family][single_category]:
                    self._hiragana_set[hiragana] = romaji
            case None:
                self._add_hiragana_category(family, [category for category in CategoryType])
            case _:
                self._logger.error(f'GameConfiguration::_add_hiragana_category(family={family}, category={category}) -> Invalid category')
                exit(ExitCode.GAME_ERROR)

    def add_hiragana(self, family: AlphabetType, category: CategoryType | list[CategoryType] | None = None) -> None:
        """
        Method to add a hiragana family set to the game set
        :param category: TODO
        :param family: The hiragana family to add
        """
        match family:
            case AlphabetType.ALL:
                self.add_hiragana(AlphabetType.SIMPLE)
                self.add_hiragana(AlphabetType.COMPLEX)
            case AlphabetType.SIMPLE | AlphabetType.COMPLEX:
                self._add_hiragana_category(family, category)
            case _:
                self._logger.error(f'GameConfiguration::add_hiragana(family={family}, category={category}) -> Invalid family')
                exit(ExitCode.GAME_ERROR)

    def _add_katakana_category(self, family: AlphabetType, category: CategoryType | list[CategoryType] | None = None):
        match category:
            case list() as category_list:
                for category in category_list:
                    self._add_katakana_category(family, category)
            case CategoryType() as single_category:
                for katakana, romaji in KATAKANA_DICTIONARY[family][single_category]:
                    self._katakana_set[katakana] = romaji
            case None:
                self._add_katakana_category(family, [category for category in CategoryType])
            case _:
                self._logger.error(f'GameConfiguration::_add_katakana_category(family={family}, category={category}) -> Invalid category')
                exit(ExitCode.GAME_ERROR)

    def add_katakana(self, family: AlphabetType, category: CategoryType | list[CategoryType] | None = None) -> None:
        """
        Method to add a katakana family set to the game set
        :param category: TODO
        :param family: The katakana family to add
        """
        match family:
            case AlphabetType.ALL:
                self.add_katakana(AlphabetType.SIMPLE)
                self.add_katakana(AlphabetType.COMPLEX)
            case AlphabetType.SIMPLE | AlphabetType.COMPLEX:
                self._add_katakana_category(family, category)
            case _:
                self._logger.error(f'GameConfiguration::add_katakana(family={family}, category={category}) -> Invalid family')
                exit(ExitCode.GAME_ERROR)

    @property
    def hiragana_activated(self) -> bool:
        return self._hiragana_activated

    @hiragana_activated.setter
    def hiragana_activated(self, value: bool):
        if value and isinstance(value, bool):
            self._hiragana_activated = value
        else:
            self._logger.error(f'Invalid value for hiragana_activated `{value}`')

    @property
    def katakana_activated(self) -> bool:
        return self._katakana_activated

    @katakana_activated.setter
    def katakana_activated(self, value: bool):
        if value and isinstance(value, bool):
            self._katakana_activated = value
        else:
            self._logger.error(f'Invalid value for katakana_activated `{value}`')

    @property
    def manual_stepping(self) -> bool:
        return self._manual_stepping

    @manual_stepping.setter
    def manual_stepping(self, value: bool):
        if value and isinstance(value, bool):
            self._manual_stepping = value
        else:
            self._logger.error(f'Invalid value for manual_stepping `{value}`')

    @property
    def response_time(self) -> int:
        return self._response_time

    @response_time.setter
    def response_time(self, value: int):
        if value and isinstance(value, int) and value > 0:
            self._response_time = value
        else:
            self._logger.error(f'Invalid value for response time `{value}`')

    @property
    def question_count(self) -> int:
        return self._question_count

    @question_count.setter
    def question_count(self, value):
        if value and isinstance(value, int) and value > 0:
            self._question_count = value
        else:
            self._logger.error(f'Invalid value for question count `{value}`')

    @property
    def proposition_count(self) -> int:
        return self._proposition_count

    @proposition_count.setter
    def proposition_count(self, value: int):
        max_length: int = len(self._katakana_set) + len(self._hiragana_set)
        if value and isinstance(value, int) and 0 < value <= max_length:
            self._proposition_count = value
        else:
            self._logger.error(f'Invalid value for proposition count `{value}` (max: {max_length})')

    @property
    def delay(self) -> int:
        return self._delay

    @delay.setter
    def delay(self, value: int):
        if value and isinstance(value, int) and value > 0:
            self._delay = value
        else:
            self._logger.error(f'Invalid value for delay `{value}`')


def get_game_config(filepath: str) -> GameConfiguration:
    """
    Function to create a GameConfig from a .cfg file
    :param filepath: Path to the config file
    :return: An instance of GameConfiguration
    """
    config_parser: ConfigParser = ConfigParser()
    config_parser.read(filepath)

    game_section = config_parser['GAME']
    if not game_section:
        GameConfiguration._logger.error('Configuration file missing section `GAME`')
        exit(ExitCode.GAME_ERROR)

    config: GameConfiguration = GameConfiguration()
    config.hiragana_activated = as_bool(game_section['hiragana-activated'])
    config.katakana_activated = as_bool(game_section['hiragana-activated'])
    config.manual_stepping = as_bool(game_section['manual-stepping'])
    config.response_time = as_int(game_section['response-time'])
    config.question_count = as_int(game_section['question-count'])
    config.proposition_count = as_int(game_section['proposition-count'])
    config.delay = as_int(game_section['delay'])

    return config
