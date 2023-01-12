from discord import Guild
from configparser import ConfigParser

from utils import Logger, ExitCode, as_bool, as_int


class BotConfiguration:
    _logger: Logger = Logger('BOT CONFIGURATION')

    def __init__(self,
                 admin_required: bool = False,
                 admin_set: set[int] = None,
                 channel: str | None = None,
                 command_prefix: str = '!'):
        self._admin_required: bool = admin_required
        self._admin_set: set[int] = (admin_set if admin_set else set())
        self._guild: Guild | None = None
        self._channel: str = (channel if channel else 'bot')
        self._command_prefix = command_prefix

    def __repr__(self) -> str:
        return f'Bot configuration: \n\
            \tGuild: `{self._guild}`\n\
            \tAdmin required: `{self._admin_required}`\n\
            \tAdmin list: {self._admin_set}\n\
            \tChannel: `{self._channel}`'

    @property
    def admin_required(self) -> bool:
        return self._admin_required

    @admin_required.setter
    def admin_required(self, value: bool):
        if value is not None and isinstance(value, bool):
            self._admin_required = value
        else:
            self._logger.error(f'Invalid value for admin_required `{value}`')

    @property
    def admin_set(self) -> set[int]:
        return self._admin_set

    @admin_set.setter
    def admin_set(self, value: set[int] | int):
        match value:
            case int() as int_value:
                self._admin_set = {int_value}
            case set() as set_value:
                self._admin_set = set_value
            case _:
                self._logger.error(f'Invalid value for admin_set `{value}`')

    @property
    def guild(self) -> Guild:
        if not self._guild:
            self._logger.error(f'Guild is None, EXITING')
            exit(ExitCode.DISCORD_ERROR)
        return self._guild

    @guild.setter
    def guild(self, value: Guild):
        if value and isinstance(value, Guild):
            self._guild = value
        else:
            self._logger.error(f'Invalid value for guild `{value}`')

    @property
    def channel(self) -> str:
        return self._channel

    @channel.setter
    def channel(self, value: str):
        if value and isinstance(value, str):
            self._channel = value
        else:
            self._logger.error(f'Invalid value for channel `{value}`')

    @property
    def command_prefix(self):
        return self._command_prefix

    @command_prefix.setter
    def command_prefix(self, value: str):
        if value and isinstance(value, str) and len(value) == 1:
            self._command_prefix = value
        else:
            self._logger.error(f'Invalid value for command prefix `{value}`')


def get_bot_config(filepath: str) -> BotConfiguration:
    """
    Function to create a GlobalConfig from a .cfg file
    :param filepath: (Optional) Path to the config file
    :return: An instance of GlobalConfig
    """
    config_parser: ConfigParser = ConfigParser()
    config_parser.read(filepath)

    bot_section = config_parser['BOT']
    if not bot_section:
        BotConfiguration._logger.error('Configuration file missing section `BOT`')
        exit(ExitCode.GAME_ERROR)

    config: BotConfiguration = BotConfiguration()
    config.admin_required = as_bool(bot_section['admin-required'])
    config.admin_set = {as_int(current_id.strip()) for current_id in bot_section['admin-ids'].split(',') if bot_section['admin-ids']}
    config.channel = bot_section['channel']
    config.command_prefix = bot_section['command-prefix']

    return config
