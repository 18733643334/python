#!/usr/bin/env python3
import pymysql, sys, re


def dd(d=''):
    print(d)
    sys.exit()


def clear_html(html_str):
    pre = re.compile('>(.*?)<')
    res = ''.join(pre.findall(html_str))
    return res


db = pymysql.connect(host='127.0.0.1', user='root', password='123456', database='revision_tron')
cursor = db.cursor()

task_sql = '''
    SELECT * FROM oa_task WHERE category = 1 AND is_show = 2
'''
cursor.execute(task_sql)
task_data = cursor.fetchall()

for val in task_data:
    val = list(val)
    id = str(val[0])
    if val[14] is None:
        val[14] = 1

    if val[33] is None:
        val[33] = ''

    if val[13]:
        val[13] = clear_html(val[13])

    child_sql = '''
        INSERT INTO oa_child_task (
            	`resource_id`,
	`alled_name`,
	`status`,
	`planned_time`,
	`tache_id`,
	`field_id`,
	`project_id`,
	`user_id`,
	`task_type`,
	`task_image`,
	`task_byname`,
	`make_demand`,
	`task_explain`,
	`difficulty`,
	`task_label`,
	`plan_start_time`,
	`plan_end_time`,
	`actually_start_timestamp`,
	`actually_end_timestamp`,
	`is_assets`,
	`is_prepare_synthe`,
	`is_template`,
	`is_highlight`,
	`company_id`,
	`pid`,
	`create_time`,
	`update_time`,
	`is_show`,
	`is_overdue`,
	`is_allot`,
	`approver`,
	`windows_publish`,
	`unix_publish`,
	`windows_work`,
	`unix_work`,
	`unix_screen_sequence`,
	`win_screen_sequence`
            ) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s','%s', '%s', '%s', '%s', '%s','%s', '%s', '%s', '%s', '%s','%s', '%s', '%s', '%s', '%s','%s', '%s', '%s', '%s', '%s','%s', '%s', '%s', '%s', '%s','%s', '%s')
    ''' % (val[1], val[2], val[3], val[4], val[5], val[6], val[7], val[9], val[10], val[11], val[12], val[13], val[33],
           val[14], val[15], val[16], val[17], val[18], val[19], val[20], val[21], val[22], val[23], val[24], val[25],
           val[27], val[28], val[29], val[30], val[31], val[32], val[34], val[35], val[36], val[37], val[38], val[39])

    res = cursor.execute(child_sql)
    db.commit()
    print('原id '+ id +' 添加成功')
