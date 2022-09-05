from email import message
from service.BotServer import bot_config
from service.monitor import monitor
from service.MysqlServer import mysqlserver


if __name__ == '__main__':
    bot = bot_config()
    monitor(bot)
    db,cursor=mysqlserver(bot)
    bot.run()