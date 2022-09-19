#!/usr/bin/env python3


import sys, os, pandas as pd
import numpy as np
import re, time

extensions = ['xlsx', 'xls']


class ReadExcel:
    def __init__(self):
        self.new_file_path = ''
        self.file_path = ''
        self.excel_new_data = np.array([])
        self.excel_files = []
        self.company_data = []
        self.new_data = []
        self.frame_data = []
        self.root_path = ''
        self.save_path = ''

    def set_file(self, b_name):
        self.file_path = '/Users/shihongxiao/Desktop/All/%s/Doc/shot/' % b_name
        self.save_path = '/Users/shihongxiao/Desktop/All/%s/References/tmp/' % b_name

    def read_file(self):
        file_names = os.listdir(self.file_path)
        if file_names:
            for file in file_names:
                file_list = file.split('.')
                extension = file_list[-1]
                if extension in extensions:
                    re_str1 = '^[a-z]{3}_[a-z]{3}_[a-zA-Z]+_[0-9]{3}shotInfo_v[0-9]{4}.xl'
                    if re.match(re_str1, file):
                        self.excel_files.append(os.path.join(self.file_path, file))
        else:
            sys.exit()
        self.read_excel()

    def read_excel(self):
        if not self.excel_files:
            sys.exit()
        for excel_file in self.excel_files:
            excel_data = pd.read_excel(excel_file, header=10, dtype=object)
            excel_data = excel_data.dropna(axis=0, how='all')
            excel_array = np.array(excel_data)[:-1]
            if len(excel_array) == 0:
                continue
            field_num = self.get_field_num(excel_file)
            company_names = self.get_company(excel_array)
            for company in company_names:
                adopt_num = 0
                fail_num = 0
                for e in excel_array:
                    if e[17] == company:
                        if e[18] == 'pass':
                            adopt_num += 1
                        else:
                            fail_num += 1
                company = str(company)
                company_arr = {
                    'company_name': company,
                    'adopt_num': adopt_num,
                    'fail_num': fail_num,
                    'field': field_num
                }
                self.company_data.append(company_arr)

    def get_company(self, e_data):
        company = e_data[:, 17]
        company = list(set(company))
        new_company = []
        for c in company:
            if not pd.isna(c):
                new_company.append(c)
        return new_company

    def get_field_num(self, e_file):
        e_file_name = os.path.basename(e_file)
        result = re.findall(r"_\d{3}", e_file_name)
        result = result[0]
        field = result[1:]
        return field

    def create_data_frame(self):
        data = []
        shot_total_num = 0
        shot_adopt_num = 0
        shot_fail_num = 0
        for i in self.company_data:
            arr = []
            arr.append(i['field'])
            arr.append(i['company_name'])
            total_num = i['adopt_num'] + i['fail_num']
            shot_total_num += total_num
            shot_adopt_num += i['adopt_num']
            shot_fail_num += i['fail_num']
            arr.append(total_num)
            arr.append(i['adopt_num'])
            arr.append(i['fail_num'])
            progress = round(i['adopt_num'] / total_num, 2) * 100
            progress = int(progress)
            progress = "%s%%" % progress
            arr.append(progress)
            data.append(arr)
        arr = []
        arr.append('总')
        arr.append('')
        arr.append(shot_total_num)
        arr.append(shot_adopt_num)
        arr.append(shot_fail_num)
        shot_progress = round(shot_adopt_num / shot_total_num, 2) * 100
        shot_progress = int(shot_progress)
        shot_progress = "%s%%" % shot_progress
        arr.append(shot_progress)
        data.append(arr)
        self.new_data = data

    def run(self, byname: {str}):
        self.set_file(byname)
        self.read_file()
        self.create_data_frame()
        self.create_file_path()
        self.data_to_ex()

    def data_to_ex(self):
        self.frame_data = pd.DataFrame(self.new_data,
                                       columns=['场号', '公司名称', '镜头总数', '完成数', '未完成数', '完成进度']).sort_values(
            by='场号')
        self.set_column_link()
        df = self.frame_data.style.applymap(self.set_field_color, subset=['场号']).set_properties(subset=['镜头总数'], **{
            "background-color": "#FED563"}).set_properties(subset=['完成数'], **{
            "background-color": "#66A342"}).set_properties(subset=['未完成数'], **{
            "background-color": "#FED563"}).applymap(self.set_percentage_color, subset=['完成进度']).set_properties(**{"font-size": "30px", "border-color": '#FFFF2E'})
        df.to_excel(self.new_file_path, index=False)

    def get_u_field(self):
        field = list(self.frame_data.loc[:, '场号'])
        s_field = set(field)
        u_field = []
        for s in s_field:
            if field.count(s) > 1:
                u_field.append(s)
        u_field = np.unique(np.array(u_field))
        return u_field

    def set_column_link(self):
        index_val = 0
        for d in self.new_data:
            field = d[0]
            rr = "^%s[a-z]{3}_[a-z]{3}_[a-zA-Z]+_%sshotInfo_v[0-9]{4}.xl" % (self.file_path, field)
            for f in self.excel_files:
                if re.match(rr, f):
                    ff = '/Volumes%s' % f
                    self.frame_data._set_value(index_val, '场号', '=HYPERLINK("{}", "{}")'.format(ff, field))
            index_val += 1

    def set_field_color(self, col):
        u_field = self.get_u_field()
        if col in u_field:
            return "background-color: #FFFF2E"

    def create_file_path(self):
        t = time.gmtime()
        date = time.strftime("%m-%d", t)
        name = 'outsource' + str(date)
        self.new_file_path = self.save_path + '/%s.xlsx' % name

    def set_percentage_color(self, x):
        val = float(x[:-1])
        color = ''
        if (val > 0) and (val <= 20):
            color = '#BFE2AF'
        elif (val > 20) and (val <= 40):
            color = '#a3ebaa'
        elif (val > 40) and (val <= 60):
            color = '#70f3ff'
        elif (val > 60) and (val <= 80):
            color = '#44cef6'
        elif (val > 80) and (val <= 100):
            color = '#93C2EA'
        else:
            color = '#ffffff'
        return "background-color: {}".format(color)


if __name__ == "__main__":
    project_byname = ['XYL']
    for byname in project_byname:
        ReadExcel().run(byname)
    print('complete')
