# 本项目中的相关状态码
# 601: 登录失败 loginError
# 602: 数据库查询报错 sqlError

from flask import Flask
from flasker.route import login_route


# 创建一个flask的工厂函数
def create_app():
    app = Flask(__name__, instance_relative_config=True)
    # 添加蓝图
    app.register_blueprint(login_route.login, url_prefix='/login')
    # app.config.from_mapping(SECRET_KEY='dev')
    return app



