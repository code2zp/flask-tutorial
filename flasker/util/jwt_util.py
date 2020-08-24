# 设置jwt
import time
import os
from flasker.util.db import OperationMysql
import jwt

class JwtLib:
    def __init__(self):
        self.opera_db = OperationMysql()

    # 设置jwt-key为环境变量
    def set_jwt_key(self):
        sql_str = "select jwt_key from flask_project.jwt"
        jwt_key = self.opera_db.select_mysql(sql_str)[0]['jwt_key']
        os.environ['jwt_key'] = jwt_key

    # jwt解码
    def decode_jwt(self, encode_jwt):
        try:
            # 获取jwt-key
            secret_key = os.environ.get('jwt_key')
            jwt.decode(encode_jwt, secret_key, algorithms=['HS256'])
            result = True
        except Exception as e:
            print('jwt验证未通过')
            result = False
        finally:
            return result