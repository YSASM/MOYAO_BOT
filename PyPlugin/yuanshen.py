from functools import reduce
from itsdangerous import json
from mirai import GroupMessage
import random
import json
import urllib.request#黑名单
group_hide=[""]
qq_hide=[""]

def get_url_data(url):
    content = urllib.request.urlopen(url).read()  
    return json.loads(content)
def get_cardAll():
    gacha_json_url = "https://webstatic.mihoyo.com/hk4e/gacha_info/cn_gf01/gacha/list.json"
    url = "https://webstatic.mihoyo.com/hk4e/gacha_info/cn_gf01//zh-cn.json"
    gacha_list = get_url_data(gacha_json_url)
    gacha_id_url = []
    for i in gacha_list['data']['list']:
        gacha_id_url.append('https://webstatic.mihoyo.com/hk4e/gacha_info/cn_gf01/'+i['gacha_id']+'/zh-cn.json')
    gacha_card_list=[]
    for i in gacha_id_url:
        gacha_card_list.append(get_url_data(i))
    return gacha_card_list

def get_k_random(k):
    return random.choices([3,4,5],weights=[96,3,1],k=k)

def get_10_random():
    arr = get_k_random(9)
    arr.append(4)
    return arr

def get_random(k):
    t = k
    arr=[]
    while(k>=10):
        arr += get_10_random()
        k -= 10
    if k!=0:
        arr+=get_k_random(k)
    if t>=90:
        arr[89]=5
    return arr




# print(gacha_card_list)


changzhu_list = ""
wuqi_list = ""
juese_list_1 = ""
juese_list_2 = ""
gacha_card_list = ""
def update_gacha():
    global changzhu_list,wuqi_list,juese_list_1,juese_list_2,gacha_card_list
    gacha_card_list = get_cardAll()
    juesecount = 0
    for i in gacha_card_list:
        if "常驻" in i['title']:
            changzhu_list = i
            # print("这里是常驻池")
            # print(changzhu_list)
            # print("\n\n\n\n")
        elif "活动" in i['title']:
            if "神铸" in i['title']:
                wuqi_list = i
            else:
                if juesecount==0:
                    juese_list_1 = i
                    juesecount+=1
                    # print("这里是角色池")
                    # print(juese_list_1)
                    # print("\n\n\n\n")
                else:
                    juese_list_2 = i 
    print("更新卡池成功！")
update_gacha()

def toint(s):
    return reduce(lambda x,y:x*10+y, map(lambda s:{'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}[s], s))


def main(bot):
    @bot.on(GroupMessage)
    async def yuanshen_chouka(event:GroupMessage):
        if event.group.id in group_hide:
            return
        if event.sender.id in qq_hide:
            return
        def back_wkf():
                return bot.send(event,"这个池子未开放！")
        if str(event.message_chain) == "原神抽卡/help":
            return bot.send(event,"有三种卡池，常驻，武器和角色up，抽卡指令为：原神抽卡/(常驻/武器/角色1/角色2)/(要抽的次数)")
        if "原神抽卡/" in str(event.message_chain):
            string = str(event.message_chain).split('/')
            try:
                times = toint(string[2])
            except TypeError:
                return bot.send(event,"请输入正确的次数！")
            except KeyError:
                return bot.send(event,"请输入正确的次数！")
            if times>100:
                    return bot.send(event,"最多100抽！")
            if string[1]=="常驻":
                if changzhu_list == "":
                    return back_wkf()
                list_card = changzhu_list
            elif string[1]=="武器":
                if wuqi_list == "":
                    return back_wkf()
                list_card = wuqi_list
            elif string[1]=="角色1":
                if juese_list_1 == "":
                    return back_wkf()
                list_card = juese_list_1
            elif string[1]=="角色2":
                if juese_list_2 == "":
                    return back_wkf()
                list_card = juese_list_2
            else:
                list_card = "error"
            if list_card == "error":
                return bot.send(event,"请输入正确的卡池！")
            if list_card == "error":
                return bot.send(event,"请输入正确的卡池！")
            arr = get_random(times)
            jieguo = []
            def random_back(k):
                return random.randint(0,k)
            for i in arr:
                if i == 5:
                    l = list_card['r5_prob_list'].__len__()
                    jieguo.append("5⭐"+str(list_card['r5_prob_list'][random_back(l-1)]['item_name'])+"\n")
                elif i == 4:
                    l = list_card['r4_prob_list'].__len__()
                    jieguo.append("4⭐"+str(list_card['r4_prob_list'][random_back(l-1)]['item_name'])+"\n")
                elif i == 3:
                    l = list_card['r3_prob_list'].__len__()
                    jieguo.append("3⭐"+str(list_card['r3_prob_list'][random_back(l-1)]['item_name'])+"\n")
            s = ''
            for i in jieguo:
                s+=i
            return bot.send(event,s)

        if  "原神卡池查询/" in str(event.message_chain):
            string = str(event.message_chain).split('/')
            if string[1]=="常驻":
                if changzhu_list == "":
                    return back_wkf()
                list_card = changzhu_list
            elif string[1]=="武器":
                if wuqi_list == "":
                    return back_wkf()
                list_card = wuqi_list
            elif string[1]=="角色1":
                if juese_list_1 == "":
                    return back_wkf()
                list_card = juese_list_1
            elif string[1]=="角色2":
                if juese_list_2 == "":
                    return back_wkf()
                list_card = juese_list_2
            else:
                list_card = "error"
            if list_card == "error":
                return bot.send(event,"请输入正确的卡池！")
            r3 = []
            r4 = []
            r5 = []
            for i in range(0,list_card['r3_prob_list'].__len__()-1):
                r3.append(str(list_card['r3_prob_list'][i]['item_name'])+"\n")
            for i in range(0,list_card['r4_prob_list'].__len__()-1):
                r4.append(str(list_card['r4_prob_list'][i]['item_name'])+"\n")
            for i in range(0,list_card['r5_prob_list'].__len__()-1):
                r5.append(str(list_card['r5_prob_list'][i]['item_name'])+"\n")
            s3=''
            s4=''
            s5=''
            for i in r3:
                s3+=i
            for i in r4:
                s4+=i
            for i in r5:
                s5+=i
            return bot.send(event,string[1]+"池中：\n五星：\n"+s5+"\n四星：\n"+s4+"\n三星：\n"+s3)
        if str(event.message_chain) == "更新原神卡池/":
            update_gacha()
            return bot.send(event,"更新卡池成功！")
                
                


                
            
