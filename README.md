# python-flask

1. 生成requirements.txt的两种方法
    - 使用与单虚拟环境的情况
        ```
        pip freeze > requirements.txt
        ```
    - 第二种：
        ```
        # 安装
        pip install pipreqs
        # 在当前目录生成
        pipreqs . --encoding=utf8 --force
        pip install -r requirements.txt
        ```