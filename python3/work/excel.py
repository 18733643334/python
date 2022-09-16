import pandas as pd
import numpy as np
import sys, time, datetime
from decimal import Decimal


def dd(d):
    print(d)
    sys.exit()


df = np.array(pd.read_excel('20201026.xlsx', sheet_name='汇总', parse_dates=True))
new_data = []

# [
#   'CPU'
#   'dmj010008_lgt_xufh_jiTaiYanShen_she_v0202.hip'
#  '/obj/ropnet1/dmj010008_lgt_xufh_yezi_dif_v0101'
#  '16核64G'
#  '成功'
#  5    Timestamp('2020-10-24 15:12:29')
#  6    Timestamp('2020-10-24 20:55:53')
#  191
#  78.7166666666667
#  191
#  '101-291'
#  0.412 24.72
#  78.72
#  ]

def dateToTime(t):
    timeArray = time.strptime(t, "%Y-%m-%d %H:%M:%S")
    timeStamp = int(time.mktime(timeArray))
    return timeStamp

for d in df:
    last_value = d[-1]
    if last_value != 0:
        str_arr = d[1].split('_')
        project_name = str_arr[0][0:3].upper()
        user_name = str_arr[2]
        # 渲染效率 = （结束时间 - 开始时间）/ 24
        start_time = pd.Timestamp(d[5]).strftime('%Y-%m-%d %H:%M:%S')
        start_timeStamp = dateToTime(start_time)
        end_time = pd.Timestamp(d[6]).strftime('%Y-%m-%d %H:%M:%S')
        end_timeStamp = dateToTime(end_time)
        efficiency = round((end_timeStamp - start_timeStamp) / 3600, 2)
        # 实际扣费 = 渲染时长 x 金额  (12H48 = 单卡   28H110 = 双卡 )
        d_type = d[0].upper()
        actual_deduction = 0
        if d_type == 'CPU':
            if d[3] == '16核64G':
                actual_deduction = round(d[8] * 1, 3)
        else:
            d_type_arr = d[3].split('核')
            d_type_str = d_type_arr[0].split('(')[1] + '核' + d_type_arr[1].split(')')[0]
            if d_type_str == '12核48G':
                actual_deduction = round(d[8] * 2.4, 3)
            elif d_type_str == '28核110G':
                actual_deduction = round(d[8] * 4.8, 3)
        # 差值  实际扣费 > 金额 = 1 否则 = 0
        difference = 0
        if actual_deduction >= float(last_value):
            difference = 0
        elif actual_deduction - float(last_value) < 0:
            difference = 0
        elif float(last_value) > actual_deduction:
            difference = float(last_value) - actual_deduction

        d = np.insert(d, 1, project_name)
        d = np.insert(d, 2, user_name)
        d = np.append(d, efficiency)
        d = np.append(d, actual_deduction)
        d = np.append(d, difference)
        new_data.append(d)

new_excel = pd.DataFrame(new_data ,columns=[
    '平台',
    '项目名称',
    '用户名称',
    '场景文件（任务名）',
    '层（镜头名）',
    '机型',
    '状态',
    '开始时间',
    '结束时间',
    '总帧数',
    '渲染时长',
    '完成帧',
    '帧序列',
    '平均单帧时长',
    '平均单帧时长（分钟）',
    '金额',
    '渲染效率',
    '实际扣费',
    '差值',
])
new_excel.to_excel('123.xlsx',sheet_name='s1', index=False)
