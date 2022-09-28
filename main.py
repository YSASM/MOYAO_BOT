from service.BotServer import bot_config
from service.monitor import monitor


if __name__ == '__main__':
    bot = bot_config()
    monitor(bot)
    bot.run()