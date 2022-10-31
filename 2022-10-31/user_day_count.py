from tron_py.common.model import Table
import time, pandas as pd


def get_user_submit_task(user_id, day_num):
    start_time = '2022-10-{} 00:00:01'.format(day_num)
    end_time = '2022-10-{} 23:59:59'.format(day_num)
    start_array = time.strptime(start_time, "%Y-%m-%d %H:%M:%S")
    start_stamp = int(time.mktime(start_array))
    end_array = time.strptime(end_time, "%Y-%m-%d %H:%M:%S")
    end_stamp = int(time.mktime(end_array))
    get_submit_task_sql = '''
        SELECT
            count( DISTINCT task_id ) as submit_num
        FROM
            oa_approvals
        WHERE
            user_id = %s
            AND create_timestamp > %s
            AND create_timestamp < %s
            AND submit_status = 2
            AND is_show = 2
            AND is_test = 2
    ''' % (user_id, start_stamp, end_stamp)
    submit_num = Table().query(get_submit_task_sql)['submit_num']
    return submit_num


if __name__ == '__main__':
    user_data_sql = '''
        SELECT
            U.id,U.realname
        FROM
            oa_admin_user AS U
            INNER JOIN oa_admin_access AS A ON U.id = A.user_id 
        WHERE
            A.group_id in (6, 7)
            AND U.`status` = 1
            AND U.id NOT IN (139,249)
    '''
    user_data = Table().query(user_data_sql)
    day = 31
    columns = ['']
    for d in range(1, day + 1):
        column_day = '10月{}日'.format(d)
        columns.append(column_day)
    data = []
    for u in user_data:
        user_id = u['id']
        user_name = u['realname']
        arr = []
        arr.append(user_name)
        for i in range(1, day + 1):
            num = get_user_submit_task(user_id, i)
            arr.append(num)
        data.append(arr)

    df = pd.DataFrame(data, columns=columns)
    df.to_excel('2022-10-1至2022-10-31.xlsx', index=False)
