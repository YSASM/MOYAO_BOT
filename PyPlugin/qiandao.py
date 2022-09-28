import base64
from datetime import datetime
from mirai import GroupMessage
from sqlalchemy import false, true
from PIL import Image,ImageDraw,ImageFont
import os
import urllib.request, io
from mirai.models import Image as mImage

from base.PluginBase import PluginBase
img = Image.open(r'PyPlugin\config\qiandao.png')
class Qiandao(PluginBase):
    def makeImg(self,name,qq,group,time,times,historytimes):
        URL = 'http://qlogo.store.qq.com/qzone/'+qq+'/'+qq+'/100'
        with urllib.request.urlopen(URL) as url:
            f = io.BytesIO(url.read())
        ico = Image.open(f).convert('RGBA')
        img_cp = img.copy()
        position = ((30),(105))
        img_cp.paste(ico,position,ico)
        font=ImageFont.truetype('simfang.ttf',20)
        ImageDraw.Draw(img_cp).text((25,75),name,(0,0,0),font=font)
        ImageDraw.Draw(img_cp).text((200,100),"签到成功！\n已经连续签到第"+times+"天！\n累计签到了第"+historytimes+"天！\n\nqq："+qq+"\n群号："+group+"\n签到时间："+time,(0,0,0),font=font)
        rgb_img = img_cp.convert('RGB')
        return rgb_img
    async def send_img(self,bot,event,name,qq,group,now,times,historytimes,sqlstring):
        self.write_sql(sqlstring)
        img = self.makeImg(name,qq,group,str(now),times,historytimes)
        img.save('PyPlugin\image\qiandaoimg'+qq+'.png','png')
        await bot.send(event,[    
            mImage(path = 'PyPlugin\image\qiandaoimg'+qq+'.png')
        ])
        os.remove('PyPlugin\image\qiandaoimg'+qq+'.png')
        return
    async def pro_name(self,name):
        return base64.b64decode(bytes(name, 'utf8')).decode()
    def __init__(self,bot):
        @bot.on(GroupMessage)
        async def start(event:GroupMessage):
            if str(event.message_chain)=="签到/":
                qq = str(event.sender.id)
                name = str(event.sender.get_name())
                group = str(event.group.id)
                now = int(datetime.now().strftime('%Y%m%d'))
                info = self.get_sql("SELECT * FROM qiandao WHERE qiandao.`qq` = '"+qq+"';")
                if not info: 
                    # base64加密昵称防止特殊字符
                    nickname = str(base64.b64encode(name.encode("utf-8"))).replace('b','').replace('\'','')
                    return self.send_img(bot,event,name,qq,group,now,'1','1',"INSERT INTO qiandao VALUES ('%s','%s','%s','%s','%s','%s')" % (nickname,qq,group,now,'1','1'))
                info = info[0]
                info = {
                    'name' : await self.pro_name(info[0]),#qq昵称
                    'qq' : info[1],#qq号
                    'group' : info[2],#最后一次签到的群号
                    'time' : self.toint(info[3]),#最后一次签到的日期
                    'times' : self.toint(info[4]),#连续签到天数
                    'historytimes' : self.toint(info[5])#累计签到天数
                }
                if now - info['time'] == 1:
                    # base64加密昵称防止特殊字符
                    nickname = str(base64.b64encode(name.encode("utf-8"))).replace('b','').replace('\'','')
                    sqlstring = "UPDATE qiandao SET historytimes='"+str(info['historytimes']+1)+"',times='"+str(info['times']+1)+"',`name`='"+nickname+"',`time`='"+str(now)+"',`group`='"+group+"' WHERE qq='"+qq+"';"
                    return self.send_img(bot,event,name,qq,group,now,str(info['times']+1),str(info['historytimes']+1),sqlstring)
                elif now - info['time'] > 1:
                    # base64加密昵称防止特殊字符
                    nickname = str(base64.b64encode(name.encode("utf-8"))).replace('b','').replace('\'','')
                    sqlstring = "UPDATE qiandao SET historytimes='"+str(info['historytimes']+1)+"',times='"+'1'+"',`name`='"+nickname+"',`time`='"+str(now)+"',`group`='"+group+"' WHERE qq='"+qq+"';"
                    return self.send_img(bot,event,name,qq,group,now,'1',str(info['historytimes']+1),sqlstring)
                elif now - info['time'] == 0:
                    if group==info['group']:
                        return bot.send(event,"你今天已经在本群签过到了！")
                    else:
                        return bot.send(event,"你今天已经在其他群签过到了！")



