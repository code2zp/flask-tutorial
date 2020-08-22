import flasker
app = flasker.create_app()

app.run(host='127.0.0.1',port=8888,debug=True)