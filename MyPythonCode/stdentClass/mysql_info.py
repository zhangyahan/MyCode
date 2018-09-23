from pymysql import *
from mysql_config import *

'''
    学生管理系统连接mysql类
'''


class student_info_mysql(object):

    def __init__(self,database=database,
                      host=host,
                      port=port,
                      user=user,
                      password=password,
                      charset=charset):
        self.database = database
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.charset = charset

    def conn_database(self):
        self.db = connect(database=self.database,
                          host=self.host,
                          password=self.password,
                          port=self.port,
                          user=self.user,
                          charset=self.charset)
        self.cursor = self.db.cursor()

    def close_database(self):
        self.cursor.close()
        self.db.close()

    # 增
    def insert_data(self,name,age,score):
        sql = "insert into students_table values(null, '{}', {}, {});".format(name,age,score)
        try:
            self.conn_database()
            self.cursor.execute(sql)
            self.db.commit()
        except:
            print("学生信息添加失败")
            self.db.rollback()
        finally:
            self.close_database()
    # 查
    def show_all_data(self):
        sql = "select * from students_table;"
        try:
            self.conn_database()
            self.cursor.execute(sql)
            res = self.cursor.fetchall()
            return res
        except:
            return "查询失败"
        finally:
            self.close_database()

    # 改
    def update_data(self):
        pass

    # 删
    def delete_data(self):
        pass



# a = student_info_mysql()
# a.conn_database()

