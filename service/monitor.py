from mirai import Startup
import PyPlugin
from service.MessageServer import send_text
def monitor(bot):
    PyPlugin.__init__(bot)
    @bot.on(Startup)
    async def monitor(event:Startup):
        await send_text(bot,'机器人启动成功！')