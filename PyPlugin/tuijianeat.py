from mirai import GroupMessage
import random
def main(bot):
    @bot.on(GroupMessage)
    async def tuiJian(event:GroupMessage):
        if str(event.message_chain) == "推荐吃什么":
            arr = ["馄饨","拉面","烩面","热干面","刀削面","油泼面","炸酱面","炒面","重庆小面","米线","酸辣粉","土豆粉","螺狮粉","凉皮儿","麻辣烫肉夹馍","羊肉汤","炒饭","盖浇饭","卤肉饭","烤肉饭","黄焖鸡米饭","驴肉火烧","川菜","麻辣香锅","火锅","酸菜鱼","烤串","披萨","烤鸭","汉堡","炸鸡","寿司","蟹黄包","粽子","煎饼果子","生煎","炒年糕"]
            return bot.send(event,arr[random.randint(0,arr.__len__()-1)])