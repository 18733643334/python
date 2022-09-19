#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pymysql, sys
import common.config as conf


class DataBaseHandle(object):
    instance = None

    def __init__(self):
        self.host = conf.host
        self.username = conf.username
        self.password = conf.password
        self.database = conf.database
        self.port = conf.port
        self.db = pymysql.connect(host=self.host, user=self.username, password=self.password, database=self.database,
                                  port=self.port, charset='utf8')
        self.cursor = self.db.cursor(cursor=pymysql.cursors.DictCursor)

    def __new__(cls, *args, **kwargs):
        if cls.instance == None:
            cls.instance = object.__new__(cls)
            return cls.instance
        else:
            return cls.instance

    def insertDB(self, sql):
        try:
            self.cursor.execute(sql)
            self.db.commit()
            return True
        except Exception as e:
            print(e)
            self.db.rollback()

    def deleteDB(self, sql):
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()

    def updateDb(self, sql):
        try:
            self.cursor.execute(sql)
            self.db.commit()
            return True
        except:
            self.db.rollback()
            # print("update function error：%s" % (sql))

    def selectDb(self, sql):
        try:
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
            return data
        except:
            return []

    def find(self, sql):
        self.cursor.execute(sql)
        data = self.cursor.fetchone()
        return data


class Model:
    def __init__(self, ):
        self.table_name = ""
        self.__table = ""
        self.db = DataBaseHandle()
        self.__where_str = ""
        self.field_str = " * "
        self.order_str = ""
        self.ex_type = ""
        self.update_str = ""
        self.__c_k = ""
        self.__c_v = ""
        self.limit = ""
        self.sql = ""

    def table(self):
        if len(self.table_name) > 0:
            if self.table_name[0:len(conf.table_prefix)] != conf.table_prefix:
                self.__table = conf.table_prefix + self.table_name

    def where(self, field, op, val):
        if self.__where_str:
            self.__where_str += " and `%s` %s '%s'" % (field, op, val)
        else:
            self.__where_str = "where `%s` %s '%s'" % (field, op, val)
        return self

    def field(self, field):
        self.field_str = " %s " % (field)
        return self

    def __createSql(self):
        if not self.__table:
            sys.exit('error：缺少表名称')
        if self.ex_type == 'create':
            self.sql = "insert into %s (%s) values (%s)" % (self.__table, self.__c_k, self.__c_v)
        else:
            if self.ex_type == 'select':
                self.sql = "select %s from %s" % (self.field_str, self.__table)
            elif self.ex_type == 'update':
                self.sql = "update %s set %s" % (self.__table, self.update_str)
            if self.__where_str:
                self.sql = "%s %s" % (self.sql, self.__where_str)
            if self.limit:
                self.sql += self.limit

    def page(self, page, limit):
        page = (page - 1) * limit
        self.limit = " limit %s, %s" % (page, limit)
        return self

    def select(self):
        self.ex_type = 'select'
        self.__createSql()
        return self.db.selectDb(self.sql)

    def get(self, id=''):
        self.ex_type = 'select'
        if id:
            self.__where_str = ""
            self.where('id', '=', id)
        self.__createSql()
        return self.db.find(self.sql)

    def update(self, data):
        self.ex_type = 'update'
        if not isinstance(data, dict):
            print("应当传入字典类型的参数")
            return False
        k_v_str = ''
        for i in data:
            k_v_str += "`%s` = '%s'," % (i, data[i])

        self.update_str = k_v_str[:-1]
        self.__createSql()
        print(self.sql)
        return self.db.updateDb(self.sql)

    def create(self, data):
        self.ex_type = 'create'
        if not isinstance(data, dict):
            print("应当传入字典类型的参数")
            return False
        k_str = ''
        v_str = ''
        for i in data:
            k_str += "%s, " % i
            v_str += "'%s', " % data[i]

        self.__c_k = k_str[:-2]
        self.__c_v = v_str[:-2]
        self.__createSql()
        self.db.insertDB(self.sql)
        return self.db.cursor.lastrowid

    def query(self, sql):
        self.db.cursor.execute(sql)
        data = self.db.cursor.fetchall()
        if len(data) > 1:
            return data
        elif len(data) == 1:
            return data[0]
        else:
            return []

    def get_columns(self):
        show_column = "show full columns from %s" % self.__table
        show_columns = self.query(show_column)
        columns = []
        for columns_type in show_columns:
            columns.append(columns_type['Field'])
        return columns


class Table(Model):
    def __init__(self, table_name=''):
        super().__init__()
        self.table_name = table_name
        self.table()
