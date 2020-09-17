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

    # 数据库写入
    def insert_mysql(self, sql_str, val, lastid=False):
        try:
            result = {
                'state': 'success',
                'lastid': 0
            }
            cursor = self.db.cursor(cursor=pymysql.cursors.DictCursor)
            cursor.executemany(sql_str, val)
            # 判断是否需要获取最后一条数据的id
            if lastid:
                result['lastid'] = cursor.lastrowid
            # 关闭数据库
            self.db.commit()
            cursor.close()
        except Exception as e:
            print(e)
            result['state'] = 'error'
        finally:
            return result


if __name__ == '__main__':
    sql_str = 'select * from flask_project.user'
    result = OperationMysql().select_mysql(sql_str)
    print(result)
    sql_str = "insert into zb_table(dbcode, id, isParent, zb_name, pid, wdcode) values (%s,%s,%s,%s,%s,%s)"
    insert_data = (('hgyd', 'A01', 'aaa', '价格指数', '', 'zb'), ('hgyd', 'A0D', 'True', '金融', '', 'zb'))
    result = OperationMysql().insert_mysql(sql_str, insert_data)
    print(result)
