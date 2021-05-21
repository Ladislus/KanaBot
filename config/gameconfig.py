from characters import Family, hiraganasSet, katakanaSet
from configparser import ConfigParser


class GameConfig:
    def __init__(self,
                 hiraganaActivated=True,
                 katakanaActivated=False,
                 manuelStep=True,
                 responseTime=10,
                 questions=5,
                 propositions=3,
                 delay=10):
        self._hiraganaActivated: bool = hiraganaActivated
        self._hiraganas: dict = {}
        self._katakanaActivated: bool = katakanaActivated
        self._katakanas: dict = {}
        self._manualStep: bool = manuelStep
        self._responseTime: int = responseTime
        self._questions: int = questions
        self._propositions: int = propositions
        self._delay: int = delay

    def __repr__(self) -> str:
        return f'Game config: \n\
            \tHiragana activated: {self._hiraganaActivated}\n\
            \tHiragana list: {self._hiraganas}\n\
            \tKatakana activated: {self._katakanaActivated}\n\
            \tKatakana list: {self._katakanas}\n\
            \tManual step: {self._manualStep}\n\
            \tResponse time: {self._responseTime}s\n\
            \tNumber of questions: {self._questions}\n\
            \tNumber of propositions: {self._propositions}\n\
            \tDelay between question: {self._delay}s\n'

    def addHiragana(self, family: Family) -> None:
        """
        Method to add a hiragana family set to the game set
        :param family: The hiragana family to add
        """
        if family == Family.ALL:
            self.addHiragana(Family.BASIC)
            self.addHiragana(Family.COMPLEXE)
        elif family == Family.BASIC:
            for hir, rom in hiraganasSet[Family.BASIC.name]:
                self._hiraganas[hir] = rom
        elif family == Family.COMPLEXE:
            for hir, rom in hiraganasSet[Family.COMPLEXE.name]:
                self._hiraganas[hir] = rom

    def addKatakana(self, family: Family) -> None:
        """
        Method to add a katakana family set to the game set
        :param family: The katakana family to add
        """
        if family == Family.ALL:
            self.addKatakana(Family.BASIC)
            self.addKatakana(Family.COMPLEXE)
        elif family == Family.BASIC:
            for kat, rom in katakanaSet[Family.BASIC.name]:
                self._katakanas[kat] = rom
        elif family == Family.COMPLEXE:
            for kat, rom in katakanaSet[Family.COMPLEXE.name]:
                self._katakanas[kat] = rom

    @property
    def hiraganaActivated(self) -> bool:
        return self._hiraganaActivated

    @property
    def katakanaActivated(self) -> bool:
        return self._katakanaActivated

    @property
    def manualStep(self) -> bool:
        return self._manualStep

    @property
    def responseTime(self) -> int:
        return self._responseTime

    @property
    def questions(self) -> int:
        return self._questions

    @property
    def propositions(self) -> int:
        return self._propositions

    @property
    def delay(self) -> int:
        return self._delay


def gameConfigFromFile(filepath: str = 'config/config.cfg') -> GameConfig:
    """
    Function to create a GameConfig from a .cfg file
    :param filepath: (Optional) Path to the config file
    :return: An instance of GameConfig
    """
    config: ConfigParser = ConfigParser()
    config.read(filepath)
    return GameConfig(
        hiraganaActivated=config['GAME']['hiraganaActivated'].lstrip().rstrip() == "True",
        katakanaActivated=config['GAME']['katakanaActivated'].lstrip().rstrip() == "True",
        manuelStep=config['GAME']['manualStep'].lstrip().rstrip() is True,
        responseTime=int(config['GAME']['responseTime']),
        questions=int(config['GAME']['questions']),
        propositions=int(config['GAME']['propositions']),
        delay=int(config['GAME']['delay'])
    )


def gameConfigToFile(gameConfig: GameConfig, filepath: str = 'config/config.cfg') -> None:
    """
    Function to write the configuration to a .cfg file
    :param gameConfig: The configuration to write
    :param filepath: (Optional) Path to the config file
    """
    config: ConfigParser = ConfigParser()
    config.read(filepath)
    config['GAME'] = {
        'hiraganaActivated': str(gameConfig.hiraganaActivated),
        'katakanaActivated': str(gameConfig.katakanaActivated),
        'manualStep': str(gameConfig.manualStep),
        'responseTime': str(gameConfig.responseTime),
        'questions': str(gameConfig.questions),
        'propositions': str(gameConfig.propositions),
        'delay': str(gameConfig.delay)
    }
    with open(filepath, 'w') as configFile:
        config.write(configFile)
