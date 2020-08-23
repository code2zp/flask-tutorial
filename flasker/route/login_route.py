from flask import Blueprint,request
from flasker.service.login_service import LoginService
import json

# 定义蓝图
login = Blueprint('login', __name__)


# 在这里临时写route ==> 等以后学了可插拔route在修改
@login.route('/hello')
def hello():
    return 'hello flask'


@login.route('/get_user_data', methods=['GET','POST'])
def get_user_data():
    print(request.data)
    return LoginService().get_user_data(json.loads(str(request.data,encoding='utf-8')))