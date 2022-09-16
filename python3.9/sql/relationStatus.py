#!/usr/bin/env python3

import numpy as np
from pytron43.common.model import DataBaseHandle, Model
# from threading import Thread


class RelationStatus(DataBaseHandle):
    def __init__(self, project_id, res_type):
        super(RelationStatus, self).__init__()
        self.project_id = project_id
        self.res_type = res_type
        self.table_name = ''
        self.res_ids = []
        self.insert_key = ''
        self.insert_val = ''
        self.tache_key = ''
        self.insert_sql = ''
        self.tacheKey()
        self.getTable()

    def tacheKey(self):
        self.tache_key = [
            [14, "art_status"],
            [16, "rig_status"],
            [18, "mod_status"],
            [19, "mmv_status"],
            [20, "dmt_status"],
            [21, "tex_status"],
            [22, "ani_status"],
            [23, "efx_status"],
            [24, "lgt_status"],
            [25, "cmp_status"],
            [29, "pre_status"],
            [30, "env_status"]
        ]
        self.createSqlKey()

    def createSqlKey(self):
        self.insert_key = "insert into oa_res_relation (field_id, res_id, res_type"
        for i in self.tache_key:
            insert_key = i[1]
            self.insert_key += ", %s" % (insert_key)
        self.insert_key += ') VALUES ('

    def createSqlVal(self):
        for res_id, field_id in self.res_ids:
            values = "%s, %s, %s, " % (field_id, res_id, self.res_type)
            task_tache_val = ""
            for t in self.tache_key:
                tache_id = t[0]
                result = self.selectMasterTask(res_id, tache_id)
                task_tache_val += "'%s' ," % result
            values += task_tache_val
            self.insert_val = values[:-1]
            self.createIsertSql()

    def createIsertSql(self):
        self.insert_sql = self.insert_key + self.insert_val + ")"
        self.insertData()

    def insertData(self):
        print(self.insert_sql)
        self.insertDB(self.insert_sql)

    def getTable(self):
        if self.res_type == 1:
            self.table_name = 'oa_shot'
        else:
            self.table_name = 'oa_asset'
        self.createResId()

    def createResId(self):
        sql = '''
                select id,field_id from %s where project_id = %d and is_show = 2
            ''' % (self.table_name, self.project_id)
        res_ids = self.selectDb(sql)
        if res_ids:
            self.res_ids = np.array(res_ids)

    # 程序开始
    def run(self):
        self.createSqlVal()
        return True

    # 查询镜头或资产主任务的状态
    def selectMasterTask(self, res_id, tache_id):
        task_sql = "select `status` from oa_task where res_id = %s and task_type = %s and tache_id = %s and category = 0" % (res_id, self.res_type, tache_id)
        task_status = self.find(task_sql)
        if task_status is None:
            return '-'
        else:
            return task_status[0]


if __name__ == '__main__':
    # project_ids_sql = '''
    #     select id from oa_project where is_show = 1
    # '''
    project_ids = Model('oa_project').where('is_show', '=', 1).field('id').select()
    print(project_ids)
    # threads = []
    # pool = ThreadPoolExecutor(max_workers=100)
    # for project_id, in project_ids:
    #     threads.append(pool.submit(RelationStatus(project_id, 1).run()))
    #     threads.append(pool.submit(RelationStatus(project_id, 2).run()))
    # for t in threads:
    #     t.result()
    # for t in threads:
    #     t.done()
    # print("完成")
    # thread_ex = []
    # for project_id, in project_ids:
    #     resut1 = Thread(target=RelationStatus(project_id, 1).run()).start()
    #     print(resut1)
    #     thread_ex.append(resut1)
    #     resut2 = Thread(target=RelationStatus(project_id, 2).run()).start()
    #     print(resut2)
    #     thread_ex.append(resut2)
    #     print("项目id：%s 执行完成" % project_id)
