from config.globalconfig import globalConfig_from_file
from bot.bot import Bot
from env import TOKEN


bot: Bot = Bot(globalConfig_from_file())
bot.run(TOKEN)
