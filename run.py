import flasker
from flasker.route import login_route

app = flasker.create_app()


# 这里临时注册蓝图
app.register_blueprint(login_route.login, url_prefix='/login')

app.run(host='0.0.0.0',port=8888,debug=True)
