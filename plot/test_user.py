import pandas as pd
from tron_py.common.model import Table
import datetime, calendar, time

from dateutil.relativedelta import relativedelta
import matplotlib.pyplot as plt

today = datetime.datetime.today()
before_date = today - relativedelta(months=2)

submit_n = []
feedback_n = []
index_arr = []
data = []
while before_date <= today:
    start_date = before_date.strftime('%Y-%m-01 00:00:01')
    time_arr = time.strptime(start_date, '%Y-%m-%d %H:%M:%S')
    month_day_n = calendar.monthrange(time_arr.tm_year, time_arr.tm_mon)[1]
    end_date = before_date.strftime('%Y-%m-{} 23:59:59'.format(month_day_n))
    index_arr.append(datetime.datetime.strftime(before_date, '%Y-%m'))
    start_stamp = int(time.mktime(time_arr))
    end_stamp = int(time.mktime(time.strptime(end_date, '%Y-%m-%d %H:%M:%S')))
    submit_daily_n = Table('approvals').where('create_timestamp', '>', start_stamp).where(
        'create_timestamp', '<', end_stamp).count()
    feedback_num = Table('approvals').where('status', 'in', '10, 15, 18, 25').where('update_timestamp', '>',
                                                                                    start_stamp).where(
        'update_timestamp',
        '<',
        end_stamp).count()
    success_num = Table('approvals').where('status', 'in', '17, 20, 23, 27').where('update_timestamp', '>',
                                                                                   start_stamp).where(
        'update_timestamp',
        '<',
        end_stamp).count()
    arr = []
    arr.append(submit_daily_n['num'])
    arr.append(success_num['num'])
    arr.append(feedback_num['num'])
    data.append(arr)
    before_date = before_date + relativedelta(months=1)

df = pd.DataFrame(data, index=index_arr, columns=['submit', 'success', 'feedback'])
print(df)
df.plot.bar()
plt.savefig('123.jpg')
