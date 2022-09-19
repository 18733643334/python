import pandas as pd
import pymysql
import numpy as np
import sys

db = pymysql.connect(host='192.168.100.201', user='root', password='king9188YJQ@', database='new_tron')
cursor = db.cursor()

sql = '''
SELECT
	project_name,
	scene_producer,
	scene_director,
	visual_effects_boss,
	visual_effects_producer,
	second_company_producer,
	inside_coordinate 
FROM
	oa_project 
WHERE
	id IN (
		6,
		13,
		15,
		21,
		24,
		28,
		30,
		31,
		33,
		34,
		37,
		38,
		39,
		41,
		43,
		45,
		46,
		47,
		48,
		50,
		55,
		56,
		57,
		58,
		59,
	60,
	65)
'''
cursor.execute(sql)
data = cursor.fetchall()
data = np.array(data)

def dd(d):
    print(d)
    sys.exit()

user_ids = ''
for item in data:
    for a in range(1 ,6):
        user_ids = user_ids + item[a].rstrip(',')
user_ids = user_ids.strip(',')
user_ids = user_ids.split(',')
user_ids = dict().fromkeys(user_ids)
user_ids = list(user_ids.keys())
new_data = []
for user_id in user_ids:
    user_sql = '''
        select realname,status from oa_admin_user where id = %s
    ''' % (user_id)
    cursor.execute(user_sql)
    user_data = np.array(cursor.fetchone())
    user_name = user_data[0]
    status = int(user_data[1])
    print(status)
    s1 = ''
    if status == 1:
        s1 = '否'
    if status == 0:
        s1 = '是'
    for item in data:
        position = ''
        if user_id in item[1]:
            position = position + '现场制片人' + ','
        if user_id in item[2]:
            position = position + '现场指导人' + ','
        if user_id in item[3]:
            position = position + '视效总监' + ','
        if user_id in item[4]:
            position = position + '视效总制片' + ','
        if user_id in item[5]:
            position = position + '外包协调制片' + ','
        if user_id in item[6]:
            position = position + '内部协调制片' + ','
        if position:
            position = position.strip(',')
            arr = []
            arr.append(user_name)
            arr.append(item[0])
            arr.append(position)
            arr.append(s1)
            new_data.append(arr)

df = pd.DataFrame(new_data, columns=['姓名', '项目名称', '项目任职', '是否离职'])
df.to_excel('z.xlsx', index=False)
