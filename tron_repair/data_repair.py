# 1、检索镜头各个环节任务状态不同步

import pymysql, numpy as np
import tron_py.common.config as cf
from tron_py.common.model import Table

db = pymysql.connect(host=cf.host, user=cf.username, passwd=cf.password, port=cf.port, database=cf.database)
cursor = db.cursor(cursor=pymysql.cursors.DictCursor)

tache_ids = [14, 16, 18, 19, 20, 21, 22, 23, 24, 25, 29, 30]
tache_columns = {14: 'art_status', 16: 'rig_status', 18: 'mod_status', 19: 'mmv_status', 20: 'dmt_status',
                 21: 'tex_status', 22: 'ani_status',
                 23: 'efx_status', 24: 'lgt_status', 25: 'cmp_status', 29: 'pre_status', 30: 'env_status'}


def main(res_type):
    res_relation_sql = '''
        select * from oa_res_relation where resource_type = %s
    ''' % res_type
    data = Table().query(res_relation_sql)
    data = np.array(data)
    for d in data:
        shot_id = d['id']
        for tache_id in tache_ids:
            task_sql = '''
                SELECT
                    `status` 
                FROM
                    oa_task 
                WHERE
                    resource_id = %s
                    AND task_type = %s
                    AND tache_id = %s
                    AND category = 0
            ''' % (shot_id, res_type, tache_id)
            task_status = Table().query(task_sql)
            tache_status = tache_columns[tache_id]
            current_tache_status = d[tache_status]
            if task_status:
                if current_tache_status != tache_status:
                    print(tache_status)
                    raise SystemExit()


if __name__ == '__main__':
    main(1)
