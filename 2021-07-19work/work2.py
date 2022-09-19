import sys, pymysql, numpy as np
import time

def dd(d=''):
    print(d)
    sys.exit()


host = '127.0.0.1'
username = 'root'
password = '123456'
database = 'zs_tron'
db = pymysql.connect(host=host, user=username, password=password, database=database)
cursor = db.cursor()



def main():
    project_sql = '''
        SELECT id,tache_ids FROM oa_project ORDER BY id ASC
    '''
    cursor.execute(project_sql)
    project_data = np.array(cursor.fetchall())
    for i in project_data:
        tache_ids = i[1].strip(',')
        project_id = i[0]
        tache_sql = '''
            SELECT * FROM oa_tache WHERE id in (%s)
        ''' % (tache_ids)
        cursor.execute(tache_sql)
        tache_data = np.array(cursor.fetchall())
#                    $param['project_id'] = $project_id;
#                    $param['tache_id'] = $item->id;
#                    $param['tache_name'] = $item->tache_name;
#                    $param['tache_explain'] = $item->explain;
#                    $param['create_time'] = time();
#                    $this->create($param);
        for t in tache_data:
            time1 = time.time()
            time1 = int(time1)
            insert_sql = '''
                INSERT INTO oa_tache_cadre (project_id,tache_id,tache_name,tache_explain,create_time) VALUES (%s, %s, '%s', '%s', %s)
            ''' % (project_id, t[0], t[1], t[2], time1)
            cursor.execute(insert_sql)
            db.commit()
    return True
        
    
    

if __name__ == '__main__':
    main()
    print('-----ok-----')