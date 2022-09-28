from mirai import GroupMessage
import random
from base.PluginBase import PluginBase
class Tuijianeat(PluginBase):
    def __init__(self,bot):
        @bot.on(GroupMessage)
        async def Tuijianeat(event:GroupMessage):
            if str(event.message_chain) == "推荐吃什么/":
                arr = self.get_sql("SELECT * FROM tuijianeat;")[0]
                return bot.send(event,arr[random.randint(0,arr.__len__()-1)])