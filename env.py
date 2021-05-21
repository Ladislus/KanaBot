from os import getenv
from dotenv import load_dotenv


load_dotenv()
TOKEN = getenv('DISCORD_TOKEN')
GUILD = getenv('DISCORD_GUILD')
OWNER = getenv('DISCORD_OWNER')

assert TOKEN is not None
assert GUILD is not None
assert OWNER is not None
