from datetime import datetime
import random
import asyncio
from mirai import GroupMessage, Startup
from sqlalchemy import false, true

morning = ["早上好啊，小懒虫们！","早起的虫儿有鸟吃！新的一天，大家要先吃饭，还是先吃我呢？","哦哈哟，米娜桑，新的一天也要元气满满哦！","又是新的一天呢，新的一天也要加油哦！"]
night = ["晚上好，禽兽们！","已经很晚了诶，该睡觉了哦！","今天又做了好多事情呢，明天也要继续努力哦！","今晚月色真美啊，能和大家一起看真的很开心呢！","这就晚上了？www我还没玩够啊！！！"]

def main(bot):
    @bot.on(Startup)
    async def start(event:Startup):
        group_list_temp = await bot.group_list()
        group_list=[]
        for i in group_list_temp:
            group_list.append(i.id)
        now = datetime.now()
        day_morning_end = True
        if now.hour < 7:
            if now.minute < 30:
                day_morning_end=False
        day_night_end = True
        if now.hour < 21:
            if now.minute < 30:
                day_night_end=False        
        while True:
            while true:
                await asyncio.sleep(1)
                now = datetime.now()
                if now.hour == 7 and now.minute == 30 and day_morning_end == False:
                    for i in group_list:  
                        await bot.send_group_message(i,morning[random.randint(0,morning.__len__()-1)])
                    day_morning_end=True
                if now.hour == 21 and now.minute == 30 and day_night_end == False:
                    for i in group_list:  
                        await bot.send_group_message(i,night[random.randint(0,night.__len__()-1)])
                    day_night_end=True
                if now.hour < 7 and now.minute < 30:
                    day_morning_end=False
                if now.hour < 21 and now.minute < 30:
                    day_night_end=False
                
                    
            
