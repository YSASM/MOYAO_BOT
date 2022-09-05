import MySQLdb
from mirai import Startup
from service.MessageServer import send_text
db = ''
cursor = ''
def mysqlserver(bot):
    @bot.on(Startup)
    async def mysqlserver(event:Startup):
        global db,cursor
        db = MySQLdb.connect("localhost", "root", "root", "qq_bot", charset='utf8' )
        cursor = db.cursor()
        await send_text(bot,'链接数据库成功！')
async def get_sql(string):
    # 执行sql语句
    cursor.execute(string)
    # 获取执行结果
    rows = cursor.fetchall()
    arr = []
    temp = []
    # 数据处理并返回一个数组
    for row in rows:
        for r in row:
            temp.append(str(r))
        arr.append(temp)
    return arr
async def write_sql(string):
    try:
        # 执行sql语句
        cursor.execute(string)
        # 提交到数据库执行
        db.commit()
        return True
    except:
        db.rollback()
        return False