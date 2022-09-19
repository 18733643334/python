#!/usr/bin/env python3

import pymysql, sys


db = pymysql.connect(host='192.168.100.247', user='root', password='king9188YJQ@', database='revision_tron')
cursor = db.cursor()

version_sql = '''
	select id,res_type,res_id from oa_version where alled_name = ''
'''
cursor.execute(version_sql)
version_data = cursor.fetchall()

def dd(d):
	print(d)
	sys.exit()
	
dd(version_data)

for val in version_data:
	if val[1] == 1:
		sql = '''
			select alled_name from oa_shot where id = %s
		''' % (val[2])
	elif val[1] == 2:
		sql = '''
			select alled_name from oa_asset where id = %s
		''' % (val[2])
	print(sql)
	cursor.execute(sql)
	resource_data = cursor.fetchone()
	if not resource_data:
		continue
	alled_name = resource_data[0]
	
	update_version_alled_name_sql = '''
		update oa_version set alled_name = '%s' where id = %s
	''' % (alled_name, val[0])
	
	cursor.execute(update_version_alled_name_sql)
	print(update_version_alled_name_sql)
	db.commit()
	

print('ok')