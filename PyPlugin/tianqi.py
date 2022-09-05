from mirai import GroupMessage
from .import toInt
import requests
def getWeather(city):
    url = 'http://autodev.openspeech.cn/csp/api/v2.1/weather?openId=aiuicus&clientType=android&sign=android&city='
    try:
        content = requests.get(url=url+city)
    except requests.exceptions.Timeout:
        return 'TimeoutError'
    except requests.exceptions.ConnectionError:
        return 'ConnectionError'
    except requests.exceptions.HTTPError:
        return 'HTTPError'
    except requests.exceptions.TooManyRedirects:
        return 'TooManyRedirects'
    except:
        return 'OtherError'
    else:
        if content.status_code == 200 and content.json():
            return content.json()
        else:
            return ''

def main(bot):
    @bot.on(GroupMessage)
    async def tianQiSearch(event:GroupMessage):
        s = str(event.message_chain).split('/')
        if "查询天气" in s:
            try:
                city = s[1]
            except IndexError:
                return
            times = toInt.toint(s[2])
            if times == 'error':
                return bot.send(event,"输入错误！")
            if times <= 0:
                return bot.send(event,"请输入正确天数！")
            if times>4:
                return bot.send(event,"最多查四天的信息哦！")
            demo = getWeather(city)
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