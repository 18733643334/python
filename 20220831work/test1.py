# dict1 = [{'XSJ': {'adopt_num': 19, 'fail_num': 135}, 'field': '004'},
#          {'金波': {'adopt_num': 0, 'fail_num': 3}, 'field': '004'},
#          {'JYXS': {'adopt_num': 0, 'fail_num': 16}, 'field': '006'},
#          {'HWKJ': {'adopt_num': 0, 'fail_num': 209}, 'field': '006'},
#          {'金波': {'adopt_num': 0, 'fail_num': 15}, 'field': '006'},
#          {'pass': {'adopt_num': 0, 'fail_num': 1}, 'field': '001'},
#          {'金波': {'adopt_num': 0, 'fail_num': 271}, 'field': '001'},
#          {'QY': {'adopt_num': 0, 'fail_num': 5}, 'field': '001'},
#          {'XSJ': {'adopt_num': 2, 'fail_num': 185}, 'field': '005'},
#          {'金波': {'adopt_num': 0, 'fail_num': 30}, 'field': '005'},
#          {'XSJ': {'adopt_num': 87, 'fail_num': 341}, 'field': '003'},
#          {'金波': {'adopt_num': 0, 'fail_num': 29}, 'field': '003'},
#          {'金波': {'adopt_num': 0, 'fail_num': 27}, 'field': '001'},
#          {'QY': {'adopt_num': 274, 'fail_num': 211}, 'field': '001'}]

# a1 = [{'company_name': 'XSJ', 'adopt_num': 19, 'fail_num': 135, 'field': '004'},
#       {'company_name': '金波', 'adopt_num': 0, 'fail_num': 3, 'field': '004'},
#       {'company_name': 'HWKJ', 'adopt_num': 0, 'fail_num': 209, 'field': '006'},
#       {'company_name': 'JYXS', 'adopt_num': 0, 'fail_num': 16, 'field': '006'},
#       {'company_name': '金波', 'adopt_num': 0, 'fail_num': 15, 'field': '006'},
#       {'company_name': 'XSJ', 'adopt_num': 2, 'fail_num': 185, 'field': '005'},
#       {'company_name': '金波', 'adopt_num': 0, 'fail_num': 30, 'field': '005'},
#       {'company_name': 'XSJ', 'adopt_num': 87, 'fail_num': 341, 'field': '003'},
#       {'company_name': '金波', 'adopt_num': 0, 'fail_num': 29, 'field': '003'},
#       {'company_name': 'QY', 'adopt_num': 274, 'fail_num': 211, 'field': '001'},
#       {'company_name': '金波', 'adopt_num': 0, 'fail_num': 27, 'field': '001'}]
#
# data = []
# shot_total_num = 0
# shot_adopt_num = 0
# shot_fail_num = 0
# for i in a1:
#     arr = []
#     arr.append(i['field'])
#     arr.append(i['company_name'])
#     total_num = i['adopt_num'] + i['fail_num']
#     shot_total_num += total_num
#     shot_adopt_num += i['adopt_num']
#     shot_fail_num += i['fail_num']
#     arr.append(i['adopt_num'])
#     arr.append(i['fail_num'])
#     progress = round(i['adopt_num'] / total_num, 2) * 100
#     progress = "%s%%" % progress
#     arr.append(progress)
#     data.append(arr)
# arr = []
# arr.append('总')
# arr.append('')
# arr.append(shot_total_num)
# arr.append(shot_adopt_num)
# arr.append(shot_fail_num)
# shot_progress = round(shot_adopt_num / shot_total_num, 2) * 100
# shot_progress = "%s%%" % shot_progress
# arr.append(shot_progress)
# data.append(arr)
# print(data)

# 274, 211

# a = [
#     'xyl_prd_wujh_004shotInfo_v0101.xlsx',
#     'xyl_prd_wujh_1-10shotInfo_v0101.xlsx',
#     'xyl_prd_wujh_006shotInfo_v0102.xlsx',
#     'xyl_prd_wujh_005shotInfo_v0101.xlsx',
#     'xyl_prd_wujh_003shotInfo_v0101.xlsx',
#     'xyl_prd_wujh_001shotInfo_v0102.xlsx'
# ]
#
# import re

#
# re_str = '^[a-z]{3}_[a-z]{3}_[a-zA-Z]+_[0-9]{3}shotInfo_v[0-9]{4}.xl'
# for i in a:
#     if re.match(re_str, i):
#         print(123)
#     else:
#         print(342)

# re_sttr = 'xyl_prd_wujh_003shotInfo_v0101.xlsx'
# retest = r"_\d{3}"
# for i in a:
#     result = re.findall(retest, i)
#     result = result[0]
#     field = result[1:]
#     print(field)

# a = [['002', 'QY', 122, 193, '39%'], ['002', '金波', 0, 24, '0%'], ['004', 'XSJ', 19, 135, '12%'], ['004', '金波', 0, 3, '0%'], ['006', '金波', 0, 15, '0%'], ['006', 'HWKJ', 0, 209, '0%'], ['006', 'JYXS', 0, 16, '0%'], ['005', '金波', 0, 30, '0%'], ['005', 'XSJ', 2, 185, '1%'], ['003', 'XSJ', 87, 341, '20%'], ['003', '金波', 0, 29, '0%'], ['001', 'QY', 274, 211, '56%'], ['001', '金波', 0, 27, '0%'],
#      ['总', '', 1922, 504, 1418, '26%']
#      ]

import time, datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re, os

# files = ['/Users/shihongxiao/Desktop/abc/shot/xyl_prd_wujh_031shotInfo_v0101.xlsx',
#          '/Users/shihongxiao/Desktop/abc/shot/xyl_prd_wujh_021shotInfo_v0101.xlsx',
#          '/Users/shihongxiao/Desktop/abc/shot/xyl_prd_wujh_011shotInfo_v0101.xlsx',
#          '/Users/shihongxiao/Desktop/abc/shot/xyl_prd_wujh_002shotInfo_v0101.xlsx',
#          '/Users/shihongxiao/Desktop/abc/shot/xyl_prd_wujh_012shotInfo_v0101.xlsx',
#          '/Users/shihongxiao/Desktop/abc/shot/xyl_prd_wujh_022shotInfo_v0101.xlsx',
#          '/Users/shihongxiao/Desktop/abc/shot/xyl_prd_wujh_032shotInfo_v0101.xlsx',
#          '/Users/shihongxiao/Desktop/abc/shot/xyl_prd_wujh_024shotInfo_v0101.xlsx',
#          '/Users/shihongxiao/Desktop/abc/shot/xyl_prd_wujh_029shotInfo_v0101.xlsx',
#          '/Users/shihongxiao/Desktop/abc/shot/xyl_prd_wujh_039shotInfo_v0101.xlsx',
#          '/Users/shihongxiao/Desktop/abc/shot/xyl_prd_wujh_034shotInfo_v0101.xlsx',
#          '/Users/shihongxiao/Desktop/abc/shot/xyl_prd_wujh_009shotInfo_v0101.xlsx',
#          '/Users/shihongxiao/Desktop/abc/shot/xyl_prd_wujh_004shotInfo_v0101.xlsx',
#          '/Users/shihongxiao/Desktop/abc/shot/xyl_prd_wujh_014shotInfo_v0101.xlsx',
#          '/Users/shihongxiao/Desktop/abc/shot/xyl_prd_wujh_019shotInfo_v0101.xlsx',
#          '/Users/shihongxiao/Desktop/abc/shot/xyl_prd_wujh_017shotInfo_v0101.xlsx',
#          '/Users/shihongxiao/Desktop/abc/shot/xyl_prd_wujh_007shotInfo_v0101.xlsx',
#          '/Users/shihongxiao/Desktop/abc/shot/xyl_prd_wujh_006shotInfo_v0102.xlsx',
#          '/Users/shihongxiao/Desktop/abc/shot/xyl_prd_wujh_037shotInfo_v0101.xlsx',
#          '/Users/shihongxiao/Desktop/abc/shot/xyl_prd_wujh_027shotInfo_v0101.xlsx',
#          '/Users/shihongxiao/Desktop/abc/shot/xyl_prd_wujh_016shotInfo_v0101.xlsx',
#          '/Users/shihongxiao/Desktop/abc/shot/xyl_prd_wujh_026shotInfo_v0101.xlsx',
#          '/Users/shihongxiao/Desktop/abc/shot/xyl_prd_wujh_036shotInfo_v0101.xlsx',
#          '/Users/shihongxiao/Desktop/abc/shot/xyl_prd_wujh_038shotInfo_v0101.xlsx',
#          '/Users/shihongxiao/Desktop/abc/shot/xyl_prd_wujh_035shotInfo_v0101.xlsx',
#          '/Users/shihongxiao/Desktop/abc/shot/xyl_prd_wujh_025shotInfo_v0101.xlsx',
#          '/Users/shihongxiao/Desktop/abc/shot/xyl_prd_wujh_028shotInfo_v0101.xlsx',
#          '/Users/shihongxiao/Desktop/abc/shot/xyl_prd_wujh_015shotInfo_v0101.xlsx',
#          '/Users/shihongxiao/Desktop/abc/shot/xyl_prd_wujh_018shotInfo_v0101.xlsx',
#          '/Users/shihongxiao/Desktop/abc/shot/xyl_prd_wujh_008shotInfo_v0101.xlsx',
#          '/Users/shihongxiao/Desktop/abc/shot/xyl_prd_wujh_005shotInfo_v0101.xlsx',
#          '/Users/shihongxiao/Desktop/abc/shot/xyl_prd_wujh_013shotInfo_v0101.xlsx',
#          '/Users/shihongxiao/Desktop/abc/shot/xyl_prd_wujh_003shotInfo_v0101.xlsx',
#          '/Users/shihongxiao/Desktop/abc/shot/xyl_prd_wujh_033shotInfo_v0101.xlsx',
#          '/Users/shihongxiao/Desktop/abc/shot/xyl_prd_wujh_040shotInfo_v0101.xlsx',
#          '/Users/shihongxiao/Desktop/abc/shot/xyl_prd_wujh_023shotInfo_v0101.xlsx',
#          '/Users/shihongxiao/Desktop/abc/shot/xyl_prd_wujh_020shotInfo_v0101.xlsx',
#          '/Users/shihongxiao/Desktop/abc/shot/xyl_prd_wujh_030shotInfo_v0101.xlsx',
#          '/Users/shihongxiao/Desktop/abc/shot/xyl_prd_wujh_001shotInfo_v0102.xlsx',
#          '/Users/shihongxiao/Desktop/abc/shot/xyl_prd_wujh_000shotInfo_v0101.xlsx',
#          '/Users/shihongxiao/Desktop/abc/shot/xyl_prd_wujh_010shotInfo_v0101.xlsx']

# columns = [r'场号', r'公司名称', r'镜头总数', r'完成数', r'未完成数', 'Test_3']
# 创建形状为（10，5） 的DataFrame 并设置二级标题
# data = [['002', 'QY', 315, 122, 193, 39.2], ['001', '金波', 24, 0, 24, 2.67]]

# df2 = pd.DataFrame(data, columns=columns)
# a1 = r'/Users/shihongxiao/www/python3.9/20220831work/aa.xlsx'

# index_val = 0
# for d in data:
#    field = d[0]
#    rr = "^/Users/shihongxiao/Desktop/abc/shot/[a-z]{3}_[a-z]{3}_[a-zA-Z]+_%sshotInfo_v[0-9]{4}.xl" % (field)
#    for i in files:
#        if re.match(rr, i):
#            df2._set_value(index_val, '场号', '=HYPERLINK("{}", "{}")'.format(i, field))
#    index_val += 1

# df2 = df2.style.set_properties(subset=['场号'], **{"background-color": "red"})
# df2 = df2.style.bar
# df2.to_excel('aaa.xlsx', index=False)

# index_val = 0
# field = '001'
# df2._set_value(index_val, '场号', '=HYPERLINK("{}", "{}")'.format(a1, field))
# df2.to_excel('aaa.xlsx', index=False)

# df2 = pd.DataFrame(data, columns=columns)
# df2 = pd.DataFrame(data, columns=columns)
# a1 = r'/Users/shihongxiao/www/python3.9/20220831work/aa.xlsx'
# df2._set_value(1, '场号', '=HYPERLINK("{}", "查看")'.format(a1))
# df2.to_excel('aaa.xlsx', index=False)

# df2 = df2.sort_values(by='场号')
# df2 = df2.style.set_properties(subset=columns, **{'width': '1000px'})
# df2.set_properties(subset=['Test_3'], **{'background-color': 'red'}).to_excel('aa.xlsx', index=False)

# style_df = demo_df.styldf2e.set_properties(subset=columns, **{'width': '1000px'})
# with pd.ExcelWriter('df_style.xlsx', engine='openpyxl') as writer:
#     style_df.to_excel(writer, index=False)

# file_names = os.listdir('/Users/shihongxiao/Desktop/abc/shot')
# print(file_names)


# a = ['mob_prd_lvbo_005shotInfo_v0102-20220806.xlsx', 'mob_prd_lvbo_002shotInfo_v0103-20220811.xlsx',
#      'mob_prd_lvbo_001shotInfo_v0103-2022\x1d0806.xlsx', 'mob_prd_lvbo_006shotInfo_v0102-20220810.xlsx',
#      'mob_prd_lvbo_003shotInfo_v0102-20220806\x1d\x1d.xlsx', 'mob_prd_lvbo_004shotInfo_v0102-20220\x1d806.xlsx']
#
# for i in a:
#     if "\x1d" in i:
#         print(1)
#         i.replace("\x1d", '')
# print(a)

# import seaborn as sns
#
#
# def set_background_color(col):
#     val = float(col[:-1])
#     color = ''
#     if (val > 0) and (val <= 20):
#         color = '#BFE2AF'
#     elif (val > 20) and (val <= 40):
#         color = '#a3ebaa'
#     elif (val > 40) and (val <= 60):
#         color = '#70f3ff'
#     elif (val > 60) and (val <= 80):
#         color = '#44cef6'
#     elif (val > 80) and (val <= 100):
#         color = '#93C2EA'
#     return "background-color: {}".format(color)
#
#
# cm = sns.light_palette('#FFFF2E', as_cmap=True)
#
# columns = ['场号', '公司名称', '镜头总数', '完成数', '未完成数', 'Test_3']
# data = [
#     ['002', 'QY', 315, 122, 193, 89.2],
#     ['001', '金波', 94, 23534, 344, 2.67],
#     ['003', '金波', 2, 234, 434, 26.7],
#     ['001', '金波', 44, 153254, 14, 47.67],
#     ['003', '金波', 54, 13, 244, 68.67],
#     ['002', '金波', 14, 564, 54764, 0],
# ]
# df3 = pd.DataFrame(data, columns=columns)

# df3 = df3.style.set_properties(
#     **{"border-color": "yellow", "width": "1000px", "font-size": "20px", "color": "red"})

# df3 = df3.style.set_properties(
#     **{"border-color": "yellow", "font-size": "20px", "color": "red"}).set_caption(
#     '测试21341').background_gradient(cmap=cm, subset=['Test_3'])


# df3.to_excel('aaa.xlsx', index=False, engine='openpyxl')
#
# print('ok')

# df3.plot(kind='bar')
# plt.show()

# -*-coding utf-8 -*-
# import matplotlib.pyplot as plt
#
# plt.rcParams['font.sans-serif'] = ['Simhei']
# plt.rcParams['axes.unicode_minus'] = False
#
# columns = [u'场号', u'公司名称', u'镜头总数', u'完成数', u'未完成数', u'Test_3']
# data = [
#     ['002', 'QY', 315, 122, 193, '89.2%'],
#     ['001', '金波', 94, 234, 344, '2.67%'],
#     ['003', '金波', 2, 234, 434, '26.7%'],
#     ['001', '金波', 44, 1554, 14, '47.67%'],
#     ['003', '金波', 54, 13, 244, '68.67%'],
#     ['002', '金波', 14, 564, 544, '0%'],
# ]
# df4 = pd.DataFrame(data, columns=columns)
# df4.plot(x='公司名称', y=['镜头总数', '完成数', '未完成数', 'Test_3'], kind='bar')
# plt.savefig('aaa.png')


import sys, os

files = os.listdir('/Users/shihongxiao/Desktop/All/MOB/Doc/shot')

# for f in files:
#     if '-' in f:
#         ff = f.split('-')
#         n_f_n = '{}.xlsx'.format(ff[0])
#         old_n = '/Users/shihongxiao/Desktop/All/MOB/Doc/shot/{}'.format(f)
#         new_n = '/Users/shihongxiao/Desktop/All/MOB/Doc/shot/{}'.format(n_f_n)
#         os.rename(old_n, new_n)

# [nan '002' '002003' '擦鱼线' nan 'ok' nan nan nan nan nan nan 'D' nan nan 60
#  '宇玺妍开' 'hd' nan nan nan '002_003316' 'mob002003_prd_hd_mov2k_v0101' nan
#  nan 'mob002003_cmp_yxyk_pre_v0101' 20220703 20220812 nan]
#
# [nan 1 '001003' '双枫崖场景延伸\n人物闪现威亚擦除' nan 'ok' nan nan nan nan nan nan 'C'
#  18 nan 18 '蝉影' nan nan nan '001_002718' 'mob001003_prd_cy_mov2k_v0101'
#  nan nan 'mob001003_cmp_CYDH_pre_v0011' 20220913 nan nan nan]

for f in files:
    rrr = '^[a-z]{3}_[a-z]{3}_[a-zA-Z]+_[0-9]{3}shotInfo_v[0-9]{4}'
    rr = re.findall(rrr, f)
    o_f = os.path.join('/Users/shihongxiao/Desktop/All/MOB/Doc/shot', f)
    n_f_n = os.path.join('/Users/shihongxiao/Desktop/All/MOB/Doc/shot', '%s.xlsx' % rr[0])
    os.rename(o_f, n_f_n)
