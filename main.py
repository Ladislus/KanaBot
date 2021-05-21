from bot import Bot
from config import globalConfigFromFile
from env import TOKEN

if __name__ == '__main__':
    bot: Bot = Bot(globalConfigFromFile())
    bot.run(TOKEN)
