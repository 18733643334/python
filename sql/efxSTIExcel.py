#!/usr/bin/env python3


#出一份这个的表格， 特效的 三体的，  镜头，   镜头时长， 难度 D，  环节，   制作人,     提交次数      状态
#				      30 STI   001001     213	     D   23 efx	  张三  		  3         不通过


import pandas as pd
import numpy as np
import pymysql

db = pymysql.connect(user='root', password='king9188YJQ@', host='192.168.100.30', database='new_tron')
cursor = db.cursor()

task_sql = '''
	select distinct resource_id from oa_task where project_id = 30 and tache_id = 23 and task_type = 1 and category = 0 and status != 35 and create_time >= 1654790401 and create_time <= 1659283201
'''
	
# 项目帧率 1:24fps 2:25fps 3:29.98 4:50fps

project_rate = [0, 24, 25, 29.98, 50]

# 镜头难度1D 2C 3B 4A 5S
shot_difficulty = ['', 'D', 'C', 'B', 'A', 'S']

#1待制作 5制作中 10待审核 15修改反馈 17组内通过 18 修改总监反馈 20内部通过 23客户待审 25修改客户反馈 27客户通过 30提交发布 35暂停
status_arr = {1 :'等待中', 5 : '制作中', 10 : '待审核', 15 : '反馈中', 20 : '审核通过', 23 : '客户待审核', 25 : '客户已反馈', 27 : '客户通过', 30 : '完成'}

cursor.execute(task_sql)
task_data = np.array(cursor.fetchall())

data = []
for shot_id, in task_data:
	arr = []
	shot_id = int(shot_id)
	arr = []
	shot_sql = '''
		SELECT
			S.alled_name,
			S.difficulty,
			S.clip_frame_length,
			P.frame_rate
		FROM
			oa_shot AS S
			INNER JOIN oa_project AS P ON S.project_id = P.id
		where S.id = %d
	''' % (shot_id)
	cursor.execute(shot_sql)
	shot_data = cursor.fetchone()
	
	alled_name,difficulty,clip_frame_length,frame_rate = shot_data
	rate = project_rate[frame_rate]
	frame_length = clip_frame_length / rate
	new_difficulty = shot_difficulty[difficulty]
	tache_name = 'EFX 特效'
	
	# 制作人  dailies提交次数 
	user_sql = '''
			SELECT
				realname 
			FROM
				oa_admin_user 
			WHERE
				id IN (
				SELECT DISTINCT
					user_id 
				FROM
					oa_approvals 
				WHERE
					resource_id = %s 
					AND resource_type = 1 
					AND tache_id = 23 
				AND is_show = 2 
				AND is_test = 2)
	''' % (shot_id)
	cursor.execute(user_sql)
	user_name = cursor.fetchall()
	user_names = ''
	if user_name:
		for u in user_name:
			user_names += u[0] + ','
			
		user_names = user_names[:-1]
	else:
		continue
	
	# dailies 提交次数
	dailies_sql = '''
		SELECT
			count( id ) 
		FROM
			oa_approvals 
		WHERE
			resource_id = %s 
			AND resource_type = 1 
			AND tache_id = 23 
			AND is_show = 2 
			AND is_test = 2
	''' % (shot_id)	
	cursor.execute(dailies_sql)
	submit_num = cursor.fetchone()[0]
	# 主任务状态
	master_status_sql = '''
		SELECT
			`status` 
		FROM
			oa_task 
		WHERE
			resource_id = %s 
			AND task_type = 1 
			AND category = 0
			AND tache_id = 23
	''' % (shot_id)
	cursor.execute(master_status_sql)
	master_status = cursor.fetchone()[0]
	master_status = status_arr[master_status]
	
	arr.append('STI')
	arr.append(alled_name)
	arr.append(frame_length)
	arr.append(new_difficulty)
	arr.append(tache_name)
	arr.append(user_names)
	arr.append(submit_num)
	arr.append(master_status)
	
	data.append(arr)
	
column = ['三体', '镜头', '镜头时长', '难度', '环节', '制作人', '提交次数', '状态']

df = pd.DataFrame(data=data, columns=column)
df.to_excel('出一份这个的表格， 特效的 三体的.xlsx', index=False)
