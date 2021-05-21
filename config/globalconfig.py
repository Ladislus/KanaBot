from typing import Optional
from discord import Guild
from configparser import ConfigParser


class GlobalConfig:
    def __init__(self,
                 activated: bool = True,
                 adminRequired: bool = False,
                 admins: set[int] = None,
                 channels: set[str] = None):
        self._activated: bool = activated
        self._adminRequired: bool = adminRequired
        self._admins: set[int] = (admins if admins is not None else set())
        self._guild: Optional[Guild] = None
        self._channels: set[str] = (channels if channels is not None else {'bot'})

    def __repr__(self) -> str:
        return f'Global config: \n\
            \tGuild: {self._guild}\n\
            \tActivated: {self._activated}\n\
            \tAdmin required: {self._adminRequired}\n\
            \tAdmin list: {self._admins}\n\
            \tChannels: {self._channels}\n'

    @property
    def activated(self) -> bool:
        return self._activated

    @property
    def adminRequired(self) -> bool:
        return self._adminRequired

    @property
    def admins(self) -> set[int]:
        return self._admins

    @property
    def guild(self) -> Guild:
        return self._guild

    @property
    def channels(self) -> set[str]:
        return self._channels


def globalConfigFromFile(filepath: str = 'config/config.cfg') -> GlobalConfig:
    """
    Function to create a GlobalConfig from a .cfg file
    :param filepath: (Optional) Path to the config file
    :return: An instance of GlobalConfig
    """
    config: ConfigParser = ConfigParser()
    config.read(filepath)
    return GlobalConfig(
        activated=config['GLOBAL']['activated'].lstrip().rstrip() == "True",
        adminRequired=config['GLOBAL']['adminRequired'].lstrip().rstrip() == "True",
        admins=set(map(int, config['GLOBAL']['admins'].split(','))) if config['GLOBAL']['admins'] != '' else set(),
        channels=set(config['GLOBAL']['channels'].split(','))
    )


def globalConfigToFile(globalConfig: GlobalConfig, filepath: str = 'config/config.cfg') -> None:
    """
    Function to write the configuration to a .cfg file
    :param filepath: (Optional) Path to the config file
    :param globalConfig: The configuration to write
    """
    config: ConfigParser = ConfigParser()
    config.read(filepath)
    config['GLOBAL'] = {
        'activated': str(globalConfig.activated),
        'adminRequired': str(globalConfig.adminRequired),
        'admins': ','.join(map(str, globalConfig.admins)),
        'channels': ','.join(globalConfig.channels)
    }
    with open(filepath, 'w') as configFile:
        config.write(configFile)
