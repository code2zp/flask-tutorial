# 操作mysql代码
import pymysql


# 创建操作mysql的类
class OperationMysql:
    def __init__(self):
        self.db = pymysql.connect('47.114.175.28', 'root', '123456', "flask_project")

    # 数据库查询
    def select_mysql(self, sql_str):
        try:
            # cursor=pymysql.cursors.DictCursor 获取字典形式的mysql数据
            cursor = self.db.cursor(cursor=pymysql.cursors.DictCursor)
            cursor.execute(sql_str)
            results = cursor.fetchall()
            # 关闭数据库
            cursor.close()
        except Exception as e:
            print(e)
        finally:
            return results


if __name__ == '__main__':
    sql_str = 'select * from flask_project.user'
    result = OperationMysql().select_mysql(sql_str)
    print(result)