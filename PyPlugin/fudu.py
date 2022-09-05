from mirai import GroupMessage
flage = 0
fudua = 0
fudub = 0
fuduc = 0
fudud = 0
def main(bot,groupid):
    @bot.on(GroupMessage)
    async def Fu_du(event: GroupMessage):
        if event.group.id == groupid:
            global fudua,fudub,flage,fuduc,fudud
            fudub = fudua
            fudud=event.sender.id
            fudua = str(event.message_chain)
            if fudud==fuduc:
                fudua=fudub
                return
            else:
                fuduc=fudud
                if fudua == fudub:
                    print(event.message_chain)
                    await bot.send(event,event.message_chain);fudua="";fudub=""
                    return
                else:
                    return