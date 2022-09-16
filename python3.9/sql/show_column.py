#!/usr/bin/env python3

import pymysql, numpy as np

connect = pymysql.connect(host='192.168.100.247', user='root', password='king9188YJQ@', database='revision_tron')
cursor = connect.cursor()

sql = 'show full columns from oa_admin_user'
cursor.execute(sql)
data = cursor.fetchall()
data = np.array(data)
print(data)