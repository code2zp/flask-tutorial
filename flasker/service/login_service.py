from flasker.util.db import OperationMysql
import json
import base64


class LoginService:
    def __init__(self):
        self.opera_db = OperationMysql()

    # 获取用户信息
    def get_user_data(self, login_param):
        sql_str = "select username,password," \
                  "CAST(create_date AS char) as create_date," \
                  "fone_number from flask_project.user where username = '{}' and password = '{}'".\
            format(login_param['username'], str(base64.b64decode(login_param['password']),encoding='utf-8'))
        # sql_str = "select * from flask_project.user"
        result = self.opera_db.select_mysql(sql_str)
        print(result)
        return json.dumps(result)

    def set_jwt_cookie(self, username):
        secret_key = ''