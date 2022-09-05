from mirai import Plain


admin_qq = 1613921123
async def send_text(bot,string):
    await bot.send_friend_message(1613921123, [Plain(string)])