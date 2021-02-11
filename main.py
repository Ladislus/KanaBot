from config.globalconfig import globalConfig_from_file
from bot.bot import Bot
from env import TOKEN

if __name__ == '__main__':
    bot: Bot = Bot(globalConfig_from_file())
    bot.run(TOKEN)
