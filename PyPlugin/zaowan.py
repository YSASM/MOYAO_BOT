from datetime import datetime
import random
import asyncio
from base.PluginBase import PluginBase
from mirai import Startup

class Zaowan(PluginBase):
    def __init__(self,bot):
        @bot.on(Startup)
        async def Zaowan(event:Startup):
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
                while True:
                    await asyncio.sleep(1)
                    now = datetime.now()
                    if now.hour == 7 and now.minute == 30 and day_morning_end == False:
                        morning = self.get_sql("SELECT morning FROM zaowan;")
                        for i in group_list:  
                            await bot.send_group_message(i,morning[random.randint(0,morning.__len__()-1)])
                        day_morning_end=True
                    if now.hour == 21 and now.minute == 30 and day_night_end == False:
                        evening = self.get_sql("SELECT evening FROM zaowan;")
                        for i in group_list:  
                            await bot.send_group_message(i,evening[random.randint(0,evening.__len__()-1)])
                        day_night_end=True
                    if now.hour < 7 and now.minute < 30:
                        day_morning_end=False
                    if now.hour < 21 and now.minute < 30:
                        day_night_end=False
                    
                        
            
