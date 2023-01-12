from bot import Bot
from utils import TOKEN

if __name__ == '__main__':

    bot: Bot = Bot('./config.cfg')
    bot.run(TOKEN)

