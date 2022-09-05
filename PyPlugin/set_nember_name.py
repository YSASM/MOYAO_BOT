from mirai.models.entities import MemberInfoModel
from mirai import GroupMessage

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
    async def set_nember_name(event:GroupMessage):
        msg = str(event.message_chain)
        if "改名/" in msg:
            arr = msg.split('/')
            qq = get_Id(arr[2])
            group = str(event.group.id)
            member = await bot.member_info(member_id = qq,
            target = group).get()
            print(member)
            await bot.member_info(group,qq).set(member.modify(member_name=arr[1]))
            await bot.send(event,"改名成功！")
            