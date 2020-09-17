# 获取国家统计局的各项指标
import requests
import json,time
from flasker.util.db import OperationMysql


# 获取数据的类
class MakeData:
    def __init__(self):
        self.opera_db = OperationMysql()

    # post请求
    def get_post_data(self, url, pyload, headers):
        resp = requests.post(url=url, data=pyload, headers=headers, verify=False)
        return resp.text

    # 将数据存入数据库
    def insert_db(self, sql_str, value, lastid=False):
        return self.opera_db.insert_mysql(sql_str, value , lastid)

    # 制作用于存入数据库的数据
    def make_insert_data(self, value):
        insetdata = []
        for i in json.loads(value):
            i['isParent'] = str(i['isParent'])
            insetdata.append(tuple(i.values()))
        return tuple(insetdata)

    # 获取数据请求数据的流程
    def get_insert_data(self, url, headers, pyload, sql_str):
        # 获取响应数据
        resp_text = self.get_post_data(url, pyload, headers)
        # 将响应数据做成可以存入数据库的数据
        insert_data = self.make_insert_data(resp_text)
        # 存入数据库
        result = self.insert_db(sql_str, insert_data, False)
        if result['state'] == 'success':
            return insert_data
        else:
            return 'error'

if __name__ == '__main__':
    url = 'https://data.stats.gov.cn/easyquery.htm'
    # 请求头
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'cookie': '_trs_uv=kf5kezab_6_e2cd; u=5; JSESSIONID=QSOcL77UzexmE4BU3n5q5DSgjYtfiDZVc3ibq753swyAmbCViWrW!1786728056',
        'Host': 'data.stats.gov.cn',
        'Origin': 'https://data.stats.gov.cn',
        'Referer': 'https://data.stats.gov.cn/easyquery.htm?cn=A01',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }
    # 请求参数
    pyload = {
        'id': 'zb',
        'dbcode': 'hgyd',
        'wdcode': 'zb',
        'm': 'getTree'
    }

    sql_str = "insert into zb_table(dbcode, id, isParent, zb_name, pid, wdcode) values (%s,%s,%s,%s,%s,%s)"
    makedata = MakeData()

    result = makedata.get_insert_data(url, headers, pyload, sql_str)
    def callback_inserdata(result):
        if result != 'error':
            for i in result:
                print(time.time())
                time.sleep(3)
                print(time.time())
                pyload['id'] = i[1]
                newresult = makedata.get_insert_data(url, headers, pyload, sql_str)
                callback_inserdata(newresult)
        else:
            print(result)


    callback_inserdata(result)


