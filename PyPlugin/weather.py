from mirai import GroupMessage
from base.PluginBase import PluginBase

class Weather(PluginBase):
    def getWeather(self,city):
        url = 'http://autodev.openspeech.cn/csp/api/v2.1/weather?openId=aiuicus&clientType=android&sign=android&city='+city
        back_code,content = self.request(self.GET,url)
        if back_code == 'ok':
            return content.json()
    def __init__(self,bot):
        @bot.on(GroupMessage)
        async def Weather(event:GroupMessage):
            s = str(event.message_chain)
            if s in ['查询天气','天气查询']:
                s = s.split('/')
                try:
                    city = s[1]
                except IndexError:
                    return
                times = (s[2])
                if times == 'error':
                    return bot.send(event,"输入错误！")
                if times <= 0:
                    return bot.send(event,"请输入正确天数！")
                if times>4:
                    return bot.send(event,"最多查四天的信息哦！")
                demo = self.getWeather(city)
                test = demo["data"]['list']
                # 获取城市
                if test == []:
                    await bot.send(event,"没有这个城市的信息")
                else:
                    for i in range(0,times):
                        temp = test[i]
                        thecity = temp['city']
                        weather = temp['weather']
                        high = str(temp['high'])
                        low = str(temp['low'])
                        wind = temp['wind']
                        humidity = str(temp['humidity'])
                        date = temp['date']
                        air = temp['airQuality']
                        windlevel = str(temp['windLevel'])
                        back = "日期："+date+"\n"+thecity+"天气:"+weather+"\n气温最高:"+high+"度\n气温最低:"+low+"度\n风向:"+wind+"\n风力："+windlevel+"级\n空气质量:"+air+"\n湿度："+humidity
                        await bot.send(event,back)