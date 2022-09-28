import MySQLdb
from service.MessageServer import send_text

def mysqlserver():
    db = MySQLdb.connect("localhost", "root", "root", "qq_bot", charset='utf8' )
    cursor = db.cursor()
    return db,cursor