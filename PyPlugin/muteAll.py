
from mirai import GroupMessage
qq = ["941229119","1613921123"]
def main(bot):
    @bot.on(GroupMessage)
    async def muteAll(event:GroupMessage):

        if(str(event.sender.id) in qq):
            if (str(event.message_chain)=="全体禁言/"):
                await bot.mute_all(event.group.id)
            if (str(event.message_chain)=="解除全体禁言/"):
                await bot.unmute_all(event.group.id)