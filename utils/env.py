from os import getenv
from dotenv import load_dotenv

from .logger import Logger
from .codes import ExitCode

_logger: Logger = Logger("ENV")

load_dotenv()
TOKEN: str = getenv('DISCORD_TOKEN')
GUILD: str = getenv('DISCORD_GUILD')
OWNER: int = int(getenv('DISCORD_OWNER').strip())

if not TOKEN:
    _logger.error("TOKEN is None. EXITING")
    exit(ExitCode.CONFIG_ERROR)

if not GUILD:
    _logger.error("GUILD is None. EXITING")
    exit(ExitCode.CONFIG_ERROR)

if not OWNER:
    _logger.error("OWNER is None. EXITING")
    exit(ExitCode.CONFIG_ERROR)
