from flask import Flask


# 创建一个flask的工厂函数
def create_app():
    app = Flask(__name__, instance_relative_config=True)
    # app.config.from_mapping(SECRET_KEY='dev')
    return app

