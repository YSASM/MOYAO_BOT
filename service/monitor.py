from mirai import Startup
from PyPlugin import Start
from service.MessageServer import send_text
def monitor(bot):
    @bot.on(Startup)
    async def monitor(event:Startup):
        Start.import_plugins(bot)
        await send_text(bot,'机器人启动成功！')