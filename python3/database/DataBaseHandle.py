# -*- coding:utf-8 -*-

import pymysql, sys, numpy as np


# 定义一个 MySQL 操作类
class DataBaseHandle:

    def __init__(self):
        print(123)
        # 初始化数据库信息并创建数据库连接
        # 下面的赋值其实可以省略，connect 时 直接使用形参即可
        self.host = '127.0.0.1'
        self.username = 'root'
        self.password = '123456'
        self.database = 'new_tron'
        self.db = pymysql.connect(self.host, self.username, self.password, self.database, 3306, charset='utf8')

    # 插入数据库操作
    def insertDB(self, sql):
        self.cursor = self.db.cursor()
        try:
            # 执行sql
            self.cursor.execute(sql)
            self.db.commit()
        except:
            # 发生错误时回滚
            self.db.rollback()
        finally:
            self.cursor.close()

    # 操作数据库数据删除
    def deleteDB(self, sql):
        self.cursor = self.db.cursor()
        try:
            # 执行sql
            # 返回 删除数据 条数 可以根据 返回值 判定处理结果
            self.cursor.execute(sql)
            self.db.commit()
        except:
            # 发生错误时回滚
            self.db.rollback()
        finally:
            self.cursor.close()

    # 更新数据库操作
    def updateDb(self, sql):
        self.cursor = self.db.cursor()
        try:
            # 执行sql
            # 返回 更新数据 条数 可以根据 返回值 判定处理结果
            self.cursor.execute(sql)
            self.db.commit()
        except:
            # 发生错误时回滚
            self.db.rollback()
        finally:
            self.cursor.close()

    # 数据库查询 返回为字典
    def selectDb(self, sql):
        self.cursor = self.db.cursor(pymysql.cursors.DictCursor)
        try:
            # 返回 查询数据 条数 可以根据 返回值 判定处理结果
            self.cursor.execute(sql)
            # 返回所有记录列表
            data = self.cursor.fetchall()

            # print(data)
            return self.to_array(data)
        except:
            print('Error: unable to fecth data')
        finally:
            self.cursor.close()

    def to_array(self, list_data):
        return np.array(list_data)

    # 数据库连接关闭
    def closeDb(self):
        self.db.close()

    # 打印数据
    def dd(self, res):
        print(res)
        sys.exit()
