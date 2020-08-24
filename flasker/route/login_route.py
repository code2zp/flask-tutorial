from flask import Blueprint,request,make_response
from flasker.service.login_service import LoginService
import json
from flasker.util.jwt_util import JwtLib

# 定义蓝图
login = Blueprint('login', __name__)


# 在这里临时写route ==> 等以后学了可插拔route在修改
@login.route('/hello')
def hello():
    return 'hello flask'


@login.route('/get_user_data', methods=['GET','POST'])
def get_user_data():
    print(request.data)
    user_data = LoginService().get_user_data(json.loads(str(request.data,encoding='utf-8')))
    result = {}
    jwt_cookie = ''
    if len(user_data) == 0:
        # 表示密码验证未通过
        result['resp_state'] = 'error'
        result['resp_result'] = '输入的账号或密码不正确'
    elif len(user_data) > 1:
        result['resp_state'] = 'error'
        result['resp_result'] = '用户名密码重复'
    else:
        result['resp_state'] = 'success'
        result['resp_result'] = '登录成功'
        # 设置jwt-key为环境变量
        JwtLib().set_jwt_key()
        # 获取jwtcookie
        jwt_cookie = LoginService().set_jwt_cookie(user_data[0])

    # 设置响应内容
    resp = make_response(json.dumps(result))
    # 判断是否设置cookie
    if jwt_cookie != "":
        resp.set_cookie('jwt_token', jwt_cookie, max_age=7200)
    else:
        resp.delete_cookie('jwt_token')
        resp.status = "601 loginError"
    return resp
