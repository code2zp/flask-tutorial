import flasker
app = flasker.create_app()

<<<<<<< HEAD
app.run(host='127.0.0.1',port=8888,debug=True)
=======

# 这里临时注册蓝图
app.register_blueprint(login_route.login, url_prefix='/login')

app.run(host='0.0.0.0',port=8888,debug=True)
>>>>>>> b6ada9888d54b3a22d0a311e211eb37aedcd37bb
