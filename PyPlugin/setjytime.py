from mirai import GroupMessage
import random
import datetime
day = 0
hour = 0
minuts = 0
s = 0
def RandomNum(y):
    num=random.randint(0,y)
    return num
def RandomTime():
    global day,hour,minuts,s
    month=datetime.datetime.now().month
    year=datetime.datetime.now().year
    day=0
    if month == 1 or month == 7 or month == 3 or month == 5 or month == 8 or month == 10 or month == 12:
        day = 31
    elif month == 4 or month == 6 or month == 9 or month == 11:
        day = 30
    elif month == 2:
        if year%4 == 0 and year%100 != 0 or year%400 == 0:
            day = 29
        else :
            day = 28
    day = RandomNum(day)
    hour = RandomNum(23)
    minuts = RandomNum(59)
    s = day*24*60*60+hour*60*60+minuts*60
    return str(day)+"天"+str(hour)+"小时"+str(minuts)+"分"
def main(bot):
    @bot.on(GroupMessage)
    async def send_group_message(event: GroupMessage):
        global day,hour,minuts,s
        groupid = event.group.id
        if str(event.message_chain) == '禁言/d':
            string = RandomTime()
            await bot.mute(
                memberId = 2650886344,
                target = groupid,
                time = s
            )
            return bot.send(event,string)
        if str(event.message_chain) == '禁言/h':
            hour = RandomNum(23)
            minuts = RandomNum(59)
            s = hour*60*60+minuts*60
            await bot.mute(
                memberId = 2650886344,
                target = groupid,
                time = s
            )
            string = str(hour)+"小时"+str(minuts)+"分钟"
            return bot.send(event,string)
        if str(event.message_chain) == '禁言/m':
            minuts = RandomNum(59)
            s = minuts*60
            await bot.mute(
                memberId = 2650886344,
                target = groupid,
                time = s
            )
            string = str(minuts)+"分钟"
            return bot.send(event,string)
        if str(event.message_chain) == '解禁/':
            await bot.unmute(
                memberId = 2650886344,
                target = groupid
            )
