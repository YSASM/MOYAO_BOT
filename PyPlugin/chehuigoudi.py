from mirai import GroupMessage
n = 0
m = 0
string = []
def main(bot):
    @bot.on(GroupMessage)
    async def zuzhi(event:GroupMessage):
        global n
        if n == 1:
            if event.sender.id == 2650886344:
                if str(event.message_chain) == "[图片]" or str(event.message_chain) == "不支持查看视频短片，请期待后续版本。":
                    await bot.recall(event.message_chain.message_id)
                    return bot.send(event,"不许色色！")
        else:
            pass
        if str(event.message_chain)=="开启撤回狗弟/" and event.sender.id != 2650886344:
            if n!=1:
                n=1
                await bot.send(event,"开启成功！")
            else:
                await bot.send(event,"已经开启了！")
        if str(event.message_chain)=="关闭撤回狗弟/" and event.sender.id != 2650886344:
            if n!=0:
                n=0
                await bot.send(event,"关闭成功！")
            else:
                await bot.send(event,"已经关闭了！")
    