# coding:utf-8
import pymysql, sys,datetime
from concurrent.futures import ThreadPoolExecutor
from common.model import DataBaseHandle


# 获取项目ID return []
def ProjectIds(DB_Handle):
    project_ids = []
    project_ids_sql = 'select id from oa_project where sort < 100 order by sort asc'
    project_ids_rows = DB_Handle.selectDb(project_ids_sql)
    for project_id_row in project_ids_rows:
        project_ids.append(project_id_row['id'])
    return project_ids


# [1] 清洗子任务与主任务状态不一致，更新主任务状态
def update_task_status(common, DB_Handle, project_id):
    task_sql = "select * from oa_task where category = 0 and project_id = %s and is_show = 2 and is_test = 2 and status>=20" % project_id
    task_rows = DB_Handle.selectDb(task_sql)
    child_task_tmp = task_tmp = []
    for task_row in task_rows:
        task_status = int(task_row['status'])
        child_task_sql = "select * from oa_task where category = 1 and pid = %s" % task_row['id']
        child_task_rows = DB_Handle.selectDb(child_task_sql)
        if len(child_task_rows) == 1:
            child_task_status = int(child_task_rows[0]['status'])
            if task_status == child_task_status:
                continue
            else:
                # 子任务状态更新主任务状态
                print(task_row['id'])
                task_update_sql = "update oa_task set status = %s where id = %s" % (child_task_status, task_row['id'])
                task_update_exec = DB_Handle.updateDb(task_update_sql)
        else:
            continue
    print('ok')


# [2] 清洗状态记录表 status_record表补录approval_id
def clean_status_record(common, DB_Handle, project_id):
    # 检查项目
    task_ids_sql = 'select id,resource_id,create_timestamp from oa_status_record where project_id = %s and resource_type = 4 and approval_id = 0' % project_id
    task_status_rows = DB_Handle.selectDb(
        task_ids_sql)  # {'id':213,'resource_id': 38816, 'create_timestamp': 1571628195}
    for task_status_row in task_status_rows:
        # 根据任务匹配提交的版本ID
        version_id_sql = 'select id from oa_version where task_id = %s and create_time <= %s order by id asc limit 1' % (
            task_status_row['resource_id'], task_status_row['create_timestamp'])
        version_id_row = DB_Handle.selectDb(version_id_sql)
        if version_id_row:
            # 版本存在比修改版本的时间早的为版本提交时间，将该版本ID更新到status_record中
            version_id = int(version_id_row[0]['id'])
            # 补充approval_id
            update_version_status_sql = 'update oa_status_record set approval_id = %s where id = %s' % (
                version_id, task_status_row['id'])
            DB_Handle.updateDb(update_version_status_sql)
        else:
            continue
    print('项目ID:' + str(project_id) + ' 执行完毕')


# [3] 迁移版本状态记录表 version_record表根据第2步status_record approval_id不为空的迁移
def clean_version_record(common, DB_Handle, project_id):
    version_record_sql = 'select * from oa_status_record where project_id = %s and resource_type = 4 and approval_id != 0 order by resource_id asc' % project_id
    version_record_rows = DB_Handle.selectDb(version_record_sql)
    for version_record_row in version_record_rows:
        # common.dd(version_record_row) # {'id': 59193, 'resource_id': 38814, 'approval_id': 28860, 'resource_type': 4, 'status': 15, 'user_id': 2, 'project_id': 30, 'field_id': 335, 'shot_assets_id': 1141, 're_type': 2, 'tache_id': 18, 'create_timestamp': 1571715058, 'create_time': '2019-10-22 11:30:58'}
        # 获取版本提交人
        version_user_sql = 'select user_id from oa_version where id = %s' % version_record_row['approval_id']
        version_user_id_row = DB_Handle.selectDb(version_user_sql)
        if version_user_id_row:
            version_user_id = version_user_id_row[0]['user_id']
            # 获取版本审核人
            reviewer_sql = 'select realname from oa_admin_user where id = %s' % version_record_row['user_id']
            reviewer_row = DB_Handle.selectDb(reviewer_sql)
            if reviewer_row:
                reviewer_name = reviewer_row[0]['realname']
            else:
                reviewer_name = ''
            insert_sql = 'insert into oa_version_record(`project_id`,`version_id`,`status`,`user_id`,`task_id`,`reviewer`,`create_time`) value(%s,%s,%s,%s,%s,"%s",%s)' % (
                project_id, version_record_row['approval_id'], version_record_row['status'], version_user_id,
                version_record_row['resource_id'], reviewer_name, version_record_row['create_timestamp'])
            # common.dd(insert_sql)
            DB_Handle.insertDB(insert_sql)
        else:
            continue
    print('项目ID:' + str(project_id) + ' 执行完毕')


# [4] 迁移任务状态记录表 task_record表 根据status_record表 resource_type = 4
def move_task_record(common, DB_Handle, project_id):
    status_record_sql = 'select * from oa_status_record where resource_type = 4 and project_id = %s' % project_id
    status_record_rows = DB_Handle.selectDb(status_record_sql)
    if status_record_rows:
        for status_record_row in status_record_rows:
            # common.dd(status_record_row)
            child_task_id = status_record_row['resource_id']
            # 检测任务是否存在 is_show = 2 目前还没对任务表task拆分主子任务表
            check_task_sql = 'select id,pid from oa_task where is_show = 2 and id = %s' % child_task_id
            check_task_row = DB_Handle.selectDb(check_task_sql)
            if check_task_row:
                main_task_id = check_task_row[0]['pid']  # 主任务ID
                # 主任务如果不存在，子任务也就不用新增了
                check_main_task_sql = 'select id,status,update_time from oa_task where is_show = 2 and id = %s' % main_task_id
                check_main_task_row = DB_Handle.selectDb(check_main_task_sql)
                if check_main_task_row:
                    check_main_task_record_sql = 'select id from oa_task_record where task_id = %s' % main_task_id
                    check_main_task_record_row = DB_Handle.selectDb(check_main_task_record_sql)
                    if not check_main_task_record_row:
                        # 根据子任务加入一条主任务状态记录 只创建1次
                        insert_main_task_sql = 'insert into oa_task_record(`project_id`,`field_id`,`res_type`,`res_id`,`task_id`,`tache_id`,`tag`,`status`,`user_id`,`create_time`) value(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)' % (
                            status_record_row['project_id'], status_record_row['field_id'],
                            status_record_row['re_type'],
                            status_record_row['shot_assets_id'],
                            main_task_id, status_record_row['tache_id'], 1,
                            check_main_task_row[0]['status'],
                            status_record_row['user_id'], check_main_task_row[0]['update_time'])
                        DB_Handle.insertDB(insert_main_task_sql)
                    else:
                        # 子任务新增语句
                        insert_child_task_sql = 'insert into oa_task_record(`project_id`,`field_id`,`res_type`,`res_id`,`task_id`,`tache_id`,`tag`,`status`,`user_id`,`create_time`) value(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)' % (
                            status_record_row['project_id'], status_record_row['field_id'],
                            status_record_row['re_type'],
                            status_record_row['shot_assets_id'],
                            child_task_id, status_record_row['tache_id'], 2,
                            status_record_row['status'],
                            status_record_row['user_id'], status_record_row['create_timestamp'])
                        DB_Handle.insertDB(insert_child_task_sql)
                else:
                    continue
            else:
                continue
    else:
        return

# [5] 拆分任务表 main_task表 与 child_task表
# 同时修改task_status_record状态记录表的task_id按照主子任务两表自增ID进行更新task_id字段
# 并计算主任务中的制作人(json) producers
def clean_task(common,DB_Handle,project_id):
    task_sql = 'select * from oa_task where project_id = %s and is_show = 2' % project_id
    task_rows = DB_Handle.selectDb(task_sql)
    if task_rows:
        for task_row in task_rows:
            task_id = task_row['id'] # task表主键
            task_type = task_row['task_type']
            # 镜头 links alled_name | 资产 links asset_name
            if task_type == 1:
                links_sql = 'select alled_name from oa_shot where id = %s' % task_row['res_id']
            else:
                pass
            if task_row['pid'] == 0:# 主任务
                if task_row['status'] == 0:# 无子任务
                    insert_main_task_sql = 'insert into oa_main_task(``,) value()'
                else:#有子任务
                    pass

            else:#子任务
                pass
    else:
        return






if __name__ == '__main__':
    DB_Handle = DataBaseHandle()
    project_ids = ProjectIds(DB_Handle)
    if project_ids:
        print(project_ids)
        for project_id in project_ids:
            move_task_record('', DB_Handle, project_id)
    else:
        print('项目空')
    # threads = []
    # common = CommonObj()
    # a = 'art'
    # common.dd(a.lower())
    #
    # start = datetime.datetime.now()
    # print(start)
    # DB_Handle = DataBaseHandle('192.168.100.247', 'root', 'king9188YJQ@', 'revision_tron', 3306)
    # pool = ThreadPoolExecutor(max_workers=50)  # 建立线程池50个
    # project_ids = ProjectIds(DB_Handle)
    # if project_ids:
    #     print(project_ids)
    #     for project_id in project_ids:
    #         DB_Handle = DataBaseHandle('192.168.100.247', 'root', 'king9188YJQ@', 'revision_tron', 3306)
    #         # threads.append(pool.submit(update_task_status, common, DB_Handle, project_id))
    #         # threads.append(pool.submit(clean_status_record, common,DB_Handle,project_id))
    #         # threads.append(pool.submit(clean_version_record, common, DB_Handle, project_id))
    #         # move_task_record(common, DB_Handle, project_id)
    #         # threads.append(pool.submit(move_task_record, common, DB_Handle, project_id))
    #         clean_task(common, DB_Handle, project_id)
    #         # threads.append(pool.submit(clean_task, common, DB_Handle, project_id))
    # else:
    #     common.dd('项目空')
    #
    # # 获取线程返回值
    # for t in threads:
    #     t.result()
    # for t in threads:
    #     t.done()
    # end = datetime.datetime.now()
    # print('Running time: %s Seconds' % (end - start))
    # print('执行完毕')

