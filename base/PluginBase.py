from functools import reduce
from service.MysqlServer import mysqlserver
import requests
import urllib3
from urllib3.exceptions import InsecureRequestWarning

class PluginBase(object):
    db,cursor = mysqlserver()
    def __init__(self,bot):
        self.GET = 'get'
        self.POST = 'post'
        self.OPTIONS = 'options'
        self.HEAD = 'head'
        self.PUT = 'put'
        self.PATCH = 'patch'
        self.DELETE = 'delete'
        
    def toint(self,s):
        try:
            a = reduce(lambda x,y:x*10+y, map(lambda s:{'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}[s], s))
        except KeyError:
            a = 'error'
        return a

    # retries:错误重连次数
    # pass_status_code:正确status_code会返回'ok',response
    # remove_status_code:忽略的status_code会返回'pass',None
    # verify:是否使用证书,默认为False
    def request(self, method, url, retries=1, pass_status_code=[200, 201], remove_status_code=[], verify=False, **kwargs):
        if not verify:
            # 禁用安全请求警告
            urllib3.disable_warnings(InsecureRequestWarning)
        while retries!=0:
            retries -= 1
            try:
                response = requests.request(
                    method=method, url=url, verify=verify, **kwargs)
                status_code = response.status_code
                if isinstance(remove_status_code, list) and status_code in remove_status_code:
                    return 'pass', None
                if isinstance(pass_status_code, list) and response.status_code not in pass_status_code:
                    return 'bad', url+'\n'+str(status_code)+'\n'+response.reason
                response.encoding = 'utf-8'
                return 'ok', response
            except Exception as e:
                if retries == 0:
                    return 'bad', url+'\n'+str(e)

    def get_sql(self,string):
        # 执行sql语句
        self.cursor.execute(string)
        # 获取执行结果
        rows = self.cursor.fetchall()
        arr = []
        temp = []
        # 数据处理并返回一个数组
        for row in rows:
            for r in row:
                temp.append(str(r))
            arr.append(temp)
        return arr
    def write_sql(self,string):
        try:
            # 执行sql语句
            self.cursor.execute(string)
            # 提交到数据库执行
            self.db.commit()
            return True
        except:
            self.db.rollback()
            return False