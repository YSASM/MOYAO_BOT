from mirai import GroupMessage
from mirai.exceptions import ApiError

admin = ["1613921123","1270145391"]
root_group=["917706233"]

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
    async def kick(event:GroupMessage):
        msg = str(event.message_chain)
        if "踢人/" in msg:
            arr = msg.split('/')
            if arr.__len__()==2:
                id = get_Id(arr[1])
                group = event.group.id
                if (str(event.sender.id) in admin) and (str(group) in root_group):
                    name = await bot.member_profile(member_id=id,target=group)
                    name = name.nickname
                    try:
                        await bot.kick(member_id=id,target=group)
                    except ApiError as e:
                        await bot.send(event,repr(e))
                    await bot.send(event,'已将"'+name+'"踢出群聊！')