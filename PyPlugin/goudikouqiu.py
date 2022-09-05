from mirai import GroupMessage
m = 0
string = []
def main(bot):
    @bot.on(GroupMessage)
    async def jinzhifudu(event:GroupMessage):
            global m,string
            if m == 1:
                if event.sender.id == 2650886344:
                    msg = str(event.message_chain)
                    count = 0
                    for i in string:
                        if msg == i:
                            count+=1
                    if count>3:
                        await bot.mute(
                                    memberId = 2650886344,
                                    target = event.group.id,
                                    time = 60
                                )
                        await bot.send(event,"狗弟不要复读哦！")
                        count = 0
                        string = []
                    if string.__len__()>5:
                        string.pop(0)
                    string.append(msg)
                    print(string)
            else:
                pass
            if str(event.message_chain)=="开启狗弟口球/" and event.sender.id != 2650886344:
                if m!=1:
                    m=1
                    await bot.send(event,"开启成功！")
                else:
                    await bot.send(event,"已经开启了！")
            if str(event.message_chain)=="关闭狗弟口球/" and event.sender.id != 2650886344:
                if m!=0:
                    m=0
                    await bot.send(event,"关闭成功！")
                else:
                    await bot.send(event,"已经关闭了！")