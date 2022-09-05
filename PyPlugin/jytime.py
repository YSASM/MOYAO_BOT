from mirai import GroupMessage
from mirai.exceptions import ApiError
import random
day = 0
hour = 0
minuts = 0
s = 0
qq = ["1613921123","1978365765","1758287689","1549055631","1806941781","3468797319","941229119","1270145391"]
group = ["948496242","389391931","340671472","917706233"]
def RandomNum(y):
    num=random.randint(0,y)
    return num
def get_Id(string):
    list_str = list(string)
    try:
        list_str.pop(0)
    except IndexError:
        return 'Null'
    list_str = ''.join(list_str)
    return str(list_str)
def main(bot):
    @bot.on(GroupMessage)
    async def send_group_message(event: GroupMessage):
        if str(event.group.id) in group:
            if str(event.sender.id) in qq or "-1" in qq:    
                async def Do(string_time,groupid,id):
                    try:
                        if string_time == 'd':
                            day = RandomNum(29)
                            hour = RandomNum(23)
                            minuts = RandomNum(59)
                            s = day*24*60*60+hour*60*60+minuts*60
                            string = str(day)+"天"+str(hour)+"小时"+str(minuts)+"分"
                            await bot.mute(
                                memberId = id,
                                target = groupid,
                                time = s
                            )
                            await bot.send(event,'禁言成功'+string)
                        if string_time == 'h':
                            hour = RandomNum(23)
                            minuts = RandomNum(59)
                            s = hour*60*60+minuts*60
                            string = str(hour)+"小时"+str(minuts)+"分钟"
                            await bot.mute(
                                memberId = id,
                                target = groupid,
                                time = s
                            )
                            await bot.send(event,'禁言成功'+string)
                        if string_time == 'm':
                            minuts = RandomNum(59)
                            s = minuts*60
                            string = str(minuts)+"分钟"
                            print(id)
                            await bot.mute(
                                memberId = id,
                                target = groupid,
                                time = s
                            )
                            await bot.send(event,'禁言成功'+string)
                    except ApiError:
                        await bot.send(event,"bot的权限不够哦")
                        return
                if "禁言/" in str(event.message_chain):
                    groupid = event.group.id
                    string = []
                    string = str(event.message_chain).split('/',2)
                    try:
                        string[2]
                    except IndexError:
                        return
                    string[2] = get_Id(string[2])
                    try:
                        string[2] = int(string[2])
                    except ValueError:
                        return bot.send(event,"复制粘贴或者随便乱输没有用哦")
                    try:
                        member= await  bot.get_group_member(
                            group=groupid,
                            id_=string[2])
                        if member.mute_time_remaining != 0:
                            await bot.send(event,"好惨啊，已经被禁言了还要继续禁他")
                    except AttributeError:
                        await bot.send(event,"找不到这个人诶，是输错了吗")
                        return
                    await Do(string[1],groupid,string[2])
                if "解禁/" in str(event.message_chain):
                    groupid = event.group.id
                    string = []
                    string = str(event.message_chain).split('/',1)
                    if get_Id(string[1]) == 'Null':
                        return
                    else:
                        string[1] = get_Id(string[1])
                    try:
                        string[1] = int(string[1])#如果用户是复制粘贴的，就会是@加上中文字符int()的时候就会出现ValueError
                    except ValueError:
                        return bot.send(event,"复制粘贴或者随便乱输没有用哦")
                    try:
                        member= await  bot.get_group_member(
                            group=groupid,
                            id_=string[1])
                        if  member.mute_time_remaining == 0:
                            return bot.send(event,"没有被禁言哦")
                    except AttributeError:
                        await bot.send(event,"找不到这个人诶，是输错了吗")
                        return
                    try:
                        await bot.unmute(
                            memberId = string[1],
                            target = groupid
                        )
                    except ApiError:
                        await bot.send(event,"bot的权限不够哦")
                        return
                    return bot.send(event,"解禁成功")
