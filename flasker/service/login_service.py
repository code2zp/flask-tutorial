from flasker.util.db import OperationMysql
import json


class LoginService:
    def __init__(self):
        self.opera_db = OperationMysql()

    # 获取用户信息
    def get_user_data(self):
        sql_str = 'select * from flask_project.user'
        result = self.opera_db.select_mysql(sql_str)
        return json.dumps(result)