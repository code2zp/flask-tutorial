from flasker.util.db import OperationMysql
import json
import base64
import jwt
import os


class LoginService:
    def __init__(self):
        self.opera_db = OperationMysql()

    # 获取用户信息
    def get_user_data(self, login_param):
        try:
            sql_str = "select username," \
                      "CAST(create_date AS char) as create_date," \
                      "fone_number from flask_project.user where username = '{}' and password = '{}'".\
                format(login_param['username'], str(base64.b64decode(login_param['password']),encoding='utf-8'))
            # sql_str = "select * from flask_project.user"
            result = self.opera_db.select_mysql(sql_str)
            print(result)
        except Exception as e:
            result = []
        finally:
            return result

    def set_jwt_cookie(self, user_data):
        secret_key = os.environ.get('jwt_key')
        encoded = jwt.encode(user_data, secret_key, algorithm='HS256')
        return str(encoded,encoding='utf-8')