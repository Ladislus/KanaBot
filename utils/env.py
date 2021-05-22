from os import getenv
from dotenv import load_dotenv
from .logger import Logger
from .codes import ExitCode

_logger = Logger("ENV")

load_dotenv()
TOKEN = getenv('DISCORD_TOKEN')
GUILD = getenv('DISCORD_GUILD')
OWNER = getenv('DISCORD_OWNER')

if TOKEN is None:
    _logger.log("Error: TOKEN is None. EXITING")
    exit(ExitCode.CONFIG_ERROR)
if GUILD is None:
    _logger.log("Error: GUILD is None. EXITING")
    exit(ExitCode.CONFIG_ERROR)
if OWNER is None:
    _logger.log("Error: OWNER is None. EXITING")
    exit(ExitCode.CONFIG_ERROR)
