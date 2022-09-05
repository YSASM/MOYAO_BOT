from mirai.models.events import GroupMessage
from mirai.models.message import Image
def main(bot):
    @bot.on(GroupMessage)
    async def sui_ji(event:GroupMessage):
        string = str(event.message_chain)
        if string == "随机图片":
            await bot.send(event,"图片加载中。。。")
            await bot.send(event,Image(url = "https://api.ixiaowai.cn/api/api.php"))