from database.DataBaseHandle import DataBaseHandle
import time,sys

db = DataBaseHandle()


def task_main():
    task_sql1 = '''
        SELECT T.*,P.pj_name AS project_name,U.NAME AS user_name FROM task AS T LEFT JOIN project AS P ON T.pj_id = P.pj_id LEFT JOIN userdata AS U ON T.uid = U.uid WHERE T.pj_id = 326 AND U.uid <> ''
    '''
    data = db.selectDb(task_sql1)
    for d in data:
        print(d['tk_type'])
        sys.exit()

if __name__ == '__main__':
    now = 1604458264
    print(type(now))
    timeArray = time.localtime(now)
    print(type(now))
    date = time.strftime('%Y-%m-%d %H:%M:%S', timeArray)
    print(date)
    print(type(date))

    task_main()
