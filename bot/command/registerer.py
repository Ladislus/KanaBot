from typing import Callable

from utils import Logger

CommandFunctionType: type = Callable[[...], bool]


class CommandInformation:
    def __init__(self,
                 name: str,
                 description: str,
                 admin_required: bool,
                 regex: str | None,
                 function: CommandFunctionType):
        self.name: str = name.strip().lower()
        self.description: str = description.strip()
        self.admin_required: bool = admin_required
        self.regex: str | None = regex.strip() if regex else None
        self.function: CommandFunctionType = function


CommandSetType: type = dict[str, CommandInformation]

COMMAND_SET: CommandSetType = {}


def register(
        name: str,
        description: str = '',
        admin_required: bool = False,
        regex: str = None) -> Callable[[...], CommandFunctionType]:
    _logger: Logger = Logger('COMMAND REGISTERER')

    def wrapper(function: CommandFunctionType) -> CommandFunctionType:
        if name in COMMAND_SET.keys():
            _logger.error(f'Command `{name}` already defined, skipping')
        else:
            COMMAND_SET[name] = CommandInformation(name=name, description=description, admin_required=admin_required, regex=regex, function=function)
            _logger.log(f'Command `{name}` loaded')
        return function

    return wrapper


