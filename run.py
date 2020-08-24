import flasker


app = flasker.create_app()


def run_flask():
    app.run(host='0.0.0.0', port=8888, debug=True)


if __name__ == '__main__':
    run_flask()
