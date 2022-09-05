# -*- coding: utf-8 -*
import json
import os
from mirai import GroupMessage
import requests
import wenxin_api # 可以通过"pip install wenxin-api"命令安装
from wenxin_api.tasks.text_to_image import TextToImage
from mirai.models import Image as mImage
wenxin_api.ak = "AN6PuWOB09Cg4nGBPZ47SLn5TG0qWtyN"
wenxin_api.sk = "bbG0V3HrnIqvknePFG7HhzxcMNxsMOBg"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0',
    'Accept': 'image/avif,image/webp,*/*',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Referer': 'https://wenxin.baidu.com/moduleApi/ernieVilg?uid=1662278145110_557&traceid=&qq-pf-to=pcqq.group',
    'Sec-Fetch-Dest': 'image',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Site': 'same-origin',
}
def main(bot):
    @bot.on(GroupMessage)
    async def wenxin(event:GroupMessage):
        text = '睡莲'
        style = '油画'
        config=str(event.message_chain).split('/')
        if config[0] != '文生图':
            return
        text = config[1]
        style = config[2]
        input_dict = {
            "text": text,
            "style": style
        }
        rst = TextToImage.create(**input_dict)
        img_urls = json.loads(rst)['imgUrls']
        for url in img_urls:
            req1 = requests.get(url, headers=headers)
            f=open('wenxin_temp.webp','wb')
            f.write(req1.content)
            f.close()
            await bot.send(event,[    
                mImage(path='wenxin_temp.webp')
            ])    
            os.remove('wenxin_temp.webp')
    

# {'imgUrls': ['https://wenxin.baidu.com/younger/file/ERNIE-ViLG/2f890ea721755035b52206ed50fb5592ex', 'https://wenxin.baidu.com/younger/file/ERNIE-ViLG/2f890ea721755035b52206ed50fb5592i4', 'https://wenxin.baidu.com/younger/file/ERNIE-ViLG/2f890ea721755035b52206ed50fb55925q', 'https://wenxin.baidu.com/younger/file/ERNIE-ViLG/2f890ea721755035b52206ed50fb559230', 'https://wenxin.baidu.com/younger/file/ERNIE-ViLG/2f890ea721755035b52206ed50fb5592v9', 'https://wenxin.baidu.com/younger/file/ERNIE-ViLG/2f890ea721755035b52206ed50fb5592a2']}
# PS C:\Users\Administrator\Desktop\MoYao-Bot-2.0>
