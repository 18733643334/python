#!/usr/bin/env python3

#import pymysql
#import pandas as pd
#import numpy as np
#
#db = pymysql.connect(host='192.168.100.201', database='new_tron', user='root', password='king9188YJQ@')
#
#cursor = db.cursor()
#
#task_sql = '''
#	SELECT
#		A.project_id,
#		A.tache_id,
#		A.company_id,
#		B.project_name,
#		A.alled_name,
#		C.`explain`,
#		D.company_name 
#	FROM
#		oa_task AS A
#		LEFT JOIN oa_project AS B ON A.project_id = B.id
#		LEFT JOIN oa_tache AS C ON A.tache_id = C.id
#		LEFT JOIN oa_company AS D ON A.company_id = D.id 
#	WHERE
#		A.task_type = 1 
#		AND A.category = 1 
#		AND A.is_show = 2 
#		AND A.is_test = 2 
#		AND A.company_id > 1 
#	ORDER BY
#		A.project_id ASC
#'''
#		
#cursor.execute(task_sql)
#task_data = np.array(cursor.fetchall())
#
#new_data = []
#
#for task_item in task_data:
#	arr = []
#	arr.append(task_item[3])
#	arr.append(task_item[4])
#	arr.append(task_item[5])
#	arr.append(task_item[6])
#	new_data.append(arr)
#	
#df = pd.DataFrame(new_data, columns=['项目名称', '镜头号', '环节', '公司名称'])
#df.to_excel('123.xlsx', index=False)
#print('程序结束')