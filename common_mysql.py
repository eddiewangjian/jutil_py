#coding=utf8
import os
import sys
import pymysql

this_file_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(this_file_path + '/../')

from jutil_py.common_log import Log

class Mysql:
    # 静态单链接请求,如果失败返回None否则返回一个二维list
    @staticmethod
    def query(host, port, db, user, passwd, sql):
        '''
        function: 连接指定的mysql地址host:port,使用用户名user和密码passwd连接一个数据库db并发送一个sql请求
        '''
        try:
            conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset='utf8')
        except Exception as e:
            Log.error("common_mysql.Mysql.query failed to connect mysql. host={} port={} db={} user={} passwd={} sql={} error_msg={}".format(
                    host, port, db, user, passwd, sql, e))
            return None

        res = []
        try:
            cursor = conn.cursor()
            count = cursor.execute(sql)
            for item in cursor.fetchall():
                res.append(item)

        except Exception as e:
            Log.error("common_mysql.Mysql.query failed to execute sql. host={} port={} db={} user={} passwd={} sql={} error_msg={}".format(
                    host, port, db, user, passwd, sql, e))
            return None

        finally:
            cursor.close()
            conn.close()

        return res


if __name__ == '__main__':
    print("res={}".format(Mysql.query("127.0.0.1", 3306, "db_name", "work", "passwd@123", "select * from user_info")))
