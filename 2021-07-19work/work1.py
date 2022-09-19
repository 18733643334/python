import sys, pymysql, numpy as np
from threading import Thread


def dd(d=''):
    print(d)
    sys.exit()


host = '127.0.0.1'
username = 'root'
password = '123456'
database = 'zs_tron'
db = pymysql.connect(host=host, user=username, password=password, database=database)
cursor = db.cursor()


def getProgress_ByTacheTaskA1(task_type, id):
    tacheIds_arr = [14, 16, 18, 19, 20, 21, 22, 23, 24, 25, 29, 30]
    str = ''
    for tache_id in tacheIds_arr:
        task_sql = "SELECT `status` FROM oa_task WHERE category = 0 AND is_show = 2 AND is_test = 2 AND tache_id = %s AND task_type = %s AND resource_id = %s" % (
            tache_id, task_type, id)
        cursor.execute(task_sql)
        task_data = cursor.fetchone()
        # print(task_data)
        if task_data == None:
            str += '0,'
        else:
            # print(111)
            str += '%s,' % (task_data[0])
        # print(str)
    str = str.rstrip(',')
    return str


def main(type, ids):
    i = 1
    for id in ids:
        print(i)
        r = getProgress_ByTacheTaskA1(type, id)
        insert_sql = '''
            INSERT INTO oa_res_relation ( `resource_id`, `resource_type`, `art_status`, `rig_status`, `mod_status`, `mmv_status`, `dmt_status`, `tex_status`, `ani_status`, `efx_status`, `lgt_status`, `cmp_status`, `pre_status`, `env_status` ) VALUES (%s, %s, %s)
        ''' % (id, type, r)
        cursor.execute(insert_sql)
        db.commit()
        i += 1


if __name__ == '__main__':
    resource_type = 1
    list_spilt = []
    results = []
    if resource_type == 1:
        shot_sql = '''
            SELECT id FROM oa_shot WHERE is_show = 2
        '''
        cursor.execute(shot_sql)
        results = np.array(cursor.fetchall()).flatten()
    elif resource_type == 2:
        asset_sql = '''
                    SELECT id FROM oa_asset WHERE is_show = 2
                '''
        cursor.execute(asset_sql)
        results = np.array(cursor.fetchall()).flatten()
        # 3
    # t1 = Thread(target=main, args=(resource_type, results,))
    # t2 = Thread(target=main, args=(resource_type, list_spilt[1],))
    # t1.start()
    # t2.start()
    main(resource_type, results)
    db.close()
    print('---ok---')
    # t1 = _thread.start_new_thread(main, (resource_type, list_spilt[0],))
    