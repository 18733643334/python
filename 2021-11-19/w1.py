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

def arr_ex(arr):
    data = ''
    for i in arr:
        realname = i[0].strip()
        data = data + realname + ','
    return data

new_data = []
for item in data:
    scene_producer = ''
    scene_producer_ids = item[1]
    if scene_producer_ids:
        scene_producer_ids = scene_producer_ids.strip(',')
        scene_producer_sql = '''
            select realname from oa_admin_user where id in (%s)
        ''' % (scene_producer_ids)
        cursor.execute(scene_producer_sql)
        scene_producer_data = np.array(cursor.fetchall())
        scene_producer_data = arr_ex(scene_producer_data)
        scene_producer = scene_producer_data.strip(',')
    #2
    scene_director = ''
    scene_director_ids = item[2]
    if scene_director_ids:
        scene_director_ids = scene_director_ids.strip(',')
        scene_director_sql = '''
                select realname from oa_admin_user where id in (%s)
            ''' % (scene_director_ids)
        cursor.execute(scene_director_sql)
        scene_director_data = np.array(cursor.fetchall())
        scene_director_data = arr_ex(scene_director_data)
        scene_director = scene_director_data.strip(',')

    # 3
    visual_effects_boss = ''
    visual_effects_boss_ids = item[3]
    if visual_effects_boss_ids:
        visual_effects_boss_ids = visual_effects_boss_ids.strip(',')
        visual_effects_boss_sql = '''
                select realname from oa_admin_user where id in (%s)
            ''' % (visual_effects_boss_ids)
        cursor.execute(visual_effects_boss_sql)
        visual_effects_boss_data = np.array(cursor.fetchall())
        visual_effects_boss_data = arr_ex(visual_effects_boss_data)
        visual_effects_boss = visual_effects_boss_data.strip(',')

    # 4
    visual_effects_producer = ''
    visual_effects_producer_ids = item[4]
    if visual_effects_producer_ids:
        visual_effects_producer_ids = visual_effects_producer_ids.strip(',')
        visual_effects_producer_sql = '''
                   select realname from oa_admin_user where id in (%s)
               ''' % (visual_effects_producer_ids)
        cursor.execute(visual_effects_producer_sql)
        visual_effects_producer_data = np.array(cursor.fetchall())
        visual_effects_producer_data = arr_ex(visual_effects_producer_data)
        visual_effects_producer = visual_effects_producer_data.strip(',')

    # 5 second_company_producer
    second_company_producer = ''
    second_company_producer_ids = item[5]
    if second_company_producer_ids:
        second_company_producer_ids = second_company_producer_ids.strip(',')
        second_company_producer_sql = '''
                       select realname from oa_admin_user where id in (%s)
                   ''' % (second_company_producer_ids)
        cursor.execute(second_company_producer_sql)
        second_company_producer_data = np.array(cursor.fetchall())
        second_company_producer_data = arr_ex(second_company_producer_data)
        second_company_producer = second_company_producer_data.strip(',')

    #6  inside_coordinate
    inside_coordinate = ''
    inside_coordinate_ids = item[6]
    if inside_coordinate_ids:
        inside_coordinate_ids = inside_coordinate_ids.strip(',')
        inside_coordinate_sql = '''
                           select realname from oa_admin_user where id in (%s)
                       ''' % (inside_coordinate_ids)
        cursor.execute(inside_coordinate_sql)
        inside_coordinate_data = np.array(cursor.fetchall())
        inside_coordinate_data = arr_ex(inside_coordinate_data)
        inside_coordinate = inside_coordinate_data.strip(',')

    arr = []
    arr.append(item[0])
    arr.append(scene_producer)
    arr.append(scene_director)
    arr.append(visual_effects_boss)
    arr.append(visual_effects_producer)
    arr.append(second_company_producer)
    arr.append(inside_coordinate)

    new_data.append(arr)

df = pd.DataFrame(new_data, columns=['项目名称', '现场制片人', '现场指导人', '视效总监', '视效总制片', '外包协调制片', '内部协调制片'])
df.to_excel('z.xlsx', index=False)
