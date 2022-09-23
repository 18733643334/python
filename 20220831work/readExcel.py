#!/usr/bin/env python3


import sys, os, pandas as pd
import numpy as np
import re, time

extensions = ['xlsx', 'xls']


class Excel:
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

    def get_field_num(self, e_file):
        e_file_name = os.path.basename(e_file)
        result = re.findall(r"_\d{3}", e_file_name)
        result = result[0]
        field = result[1:]
        return field

    def set_field_color(self, col):
        u_field = self.get_u_field()
        if col in u_field:
            return "background-color: #FFFF2E"

    def create_file_path(self):
        t = time.gmtime()
        date = time.strftime("%m-%d", t)
        name = 'outsource' + str(date)
        self.new_file_path = self.save_path + '%s.xlsx' % name

    def set_percentage_color(self, x):
        val = float(x[:-1])
        if (val > 0) and (val <= 20):
            color = '#BFE2AF'
        elif (val > 20) and (val <= 40):
            color = '#a3ebaa'
        elif (val > 40) and (val <= 60):
            color = '#70f3ff'
        elif (val > 60) and (val <= 80):
            color = '#44cef6'
        elif (val > 80) and (val <= 100):
            color = '#00FF00'
        else:
            color = '#ffffff'
        return "background-color: {}".format(color)

    def checkout_f_n(self):
        files = os.listdir(self.file_path)
        for f in files:
            re_str1 = '^[a-z]{3}_[a-z]{3}_[a-zA-Z]+_[0-9]{3}shotInfo_v[0-9]{4}.+xlsx'
            if re.match(re_str1, f):
                rrr = '^[a-z]{3}_[a-z]{3}_[a-zA-Z]+_[0-9]{3}shotInfo_v[0-9]{4}'
                rr = re.findall(rrr, f)
                o_f = os.path.join(self.file_path, f)
                n_f_n = os.path.join(self.file_path, '%s.xlsx' % rr[0])
                os.rename(o_f, n_f_n)

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
            rr = "^%s[a-z]{3}_[a-z]{3}_[a-zA-Z]+_%sshotInfo_v[0-9]{4}[.]{1}xlsx$" % (self.file_path, field)
            for f in self.excel_files:
                if re.match(rr, f):
                    ff = '/Volumes%s' % f
                    self.frame_data._set_value(index_val, '场号', '=HYPERLINK("{}", "{}")'.format(ff, field))
            index_val += 1
        return self

    def company_names(self, c_data):
        company = list(set(c_data))
        new_company = []
        for c in company:
            if not pd.isna(c):
                new_company.append(c)
        return new_company

    def create_data_frame(self):
        if self.company_data:
            data = []
            shot_total_num = 0
            shot_adopt_num = 0
            shot_fail_num = 0
            shot_submit_num = 0
            shot_not_submit_num = 0
            for i in self.company_data:
                arr = []
                arr.append(i['field'])
                arr.append(i['company_name'])
                shot_total_num += i['total_num']
                shot_adopt_num += i['adopt_num']
                shot_fail_num += i['fail_num']
                arr.append(i['total_num'])
                shot_submit_num += i['submit_num']
                arr.append(i['submit_num'])
                arr.append(i['adopt_num'])
                arr.append(i['fail_num'])
                shot_not_submit_num += i['not_submit']
                arr.append(i['not_submit'])
                progress = int((i['adopt_num'] / i['total_num']) * 10000) / 100
                if int(progress) == 100:
                    progress = 100
                progress = "%s%%" % progress
                arr.append(progress)
                data.append(arr)
            arr = []
            arr.append('总')
            arr.append('')
            arr.append(shot_total_num)
            arr.append(shot_submit_num)
            arr.append(shot_adopt_num)
            arr.append(shot_fail_num)
            arr.append(shot_not_submit_num)
            shot_progress = round(shot_adopt_num / shot_total_num, 2) * 100
            shot_progress = int(shot_progress)
            shot_progress = "%s%%" % shot_progress
            arr.append(shot_progress)
            data.append(arr)
            self.new_data = data

    def data_to_ex(self):
        if self.new_data:
            self.frame_data = pd.DataFrame(self.new_data,
                                           columns=['场号', '公司名称', '镜头总数', '已提交数', '通过数', '未通过数', '未提交数',
                                                    '完成进度']).sort_values(
                by='场号')
            self.set_column_link()
            df = self.frame_data.style.applymap(self.set_field_color, subset=['场号']).set_properties(subset=['镜头总数'], **{
                "background-color": "#FED563"}).set_properties(subset=['已提交数'], **{
                "background-color": "#98FB98"}).set_properties(subset=['未通过数'], **{
                "background-color": "#555555"}).set_properties(subset=['未提交数'], **{
                "background-color": "#A020F0"
            }).set_properties(**{"background-color": "#7FFF00"}, subset=['通过数']).applymap(self.set_percentage_color,
                                                                                          subset=[
                                                                                              '完成进度']).set_properties(
                **{"font-size": "30px", "border-color": '#FFFF2E', "color": '#ec0790'})
            df.to_excel(self.new_file_path, index=False)
        else:
            return False


class ReadExcel(Excel):
    def __init__(self):
        super().__init__()

    def read_file(self):
        file_names = os.listdir(self.file_path)
        if file_names:
            for file in file_names:
                file_list = file.split('.')
                extension = file_list[-1]
                if extension in extensions:
                    re_str1 = '^[a-z]{3}_[a-z]{3}_[a-zA-Z]+_[0-9]{3}shotInfo_v[0-9]{4}[.]{1}xlsx$'
                    if re.match(re_str1, file):
                        self.excel_files.append(os.path.join(self.file_path, file))
        else:
            self.excel_files = []
        self.read_excel()

    def read_excel(self):
        if not self.excel_files:
            self.company_data = []
        for excel_file in self.excel_files:
            excel_data = pd.read_excel(excel_file, header=10, dtype=object)
            excel_data = excel_data.dropna(axis=0, how='all')
            excel_array = np.array(excel_data)[:-1]
            if len(excel_array) == 0:
                continue
            field_num = self.get_field_num(excel_file)
            company_names = self.get_company(excel_array)
            if len(company_names) == 0:
                continue
            for company in company_names:
                total_num = 0
                adopt_num = 0
                fail_num = 0
                for e in excel_array:
                    if e[17] == company:
                        if e[18] == 'omit':
                            continue
                        total_num += 1
                        if e[18] in ['pass', 'ok']:
                            adopt_num += 1
                        elif e[18] == 'fix':
                            fail_num += 1
                company = str(company)
                company_arr = {
                    'company_name': company,
                    'total_num': total_num,
                    'submit_num': adopt_num + fail_num,
                    'adopt_num': adopt_num,
                    'fail_num': fail_num,
                    'not_submit': total_num - (adopt_num + fail_num),
                    'field': field_num
                }
                self.company_data.append(company_arr)

    def get_company(self, e_data):
        company = e_data[:, 17]
        return self.company_names(company)

    def run(self, byname: {str}):
        self.set_file(byname)
        self.read_file()
        self.create_data_frame()
        self.create_file_path()
        self.data_to_ex()


class Mob(Excel):
    def __init__(self):
        super().__init__()

    def read_file(self):
        self.checkout_f_n()
        file_names = os.listdir(self.file_path)
        if file_names:
            for file in file_names:
                file_list = file.split('.')
                extension = file_list[-1]
                if extension in extensions:
                    re_str1 = '^[a-z]{3}_[a-z]{3}_[a-zA-Z]+_[0-9]{3}shotInfo_v[0-9]{4}[.]{1}xlsx$'
                    if re.match(re_str1, file):
                        self.excel_files.append(os.path.join(self.file_path, file))
        else:
            self.excel_files = []
        self.read_excel()

    def read_excel(self):
        if not self.excel_files:
            self.company_data = []
        for excel_file in self.excel_files:
            excel_data = pd.read_excel(excel_file, header=8, dtype=object)
            excel_data = excel_data.dropna(axis=0, how='all')
            excel_array = np.array(excel_data)[:-1]
            if len(excel_array) == 0:
                continue
            field_num = self.get_field_num(excel_file)
            company_names = self.get_company(excel_array)
            if len(company_names) == 0:
                continue
            for company in company_names:
                total_num = 0
                adopt_num = 0
                fail_num = 0
                for e in excel_array:
                    if e[16] == company:
                        if e[5] == 'omit':
                            continue
                        total_num += 1
                        if e[5] in ['pass', 'ok']:
                            adopt_num += 1
                        elif e[5] == 'fix':
                            fail_num += 1
                company = str(company)
                company_arr = {
                    'company_name': company,
                    'total_num': total_num,
                    'submit_num': adopt_num + fail_num,
                    'adopt_num': adopt_num,
                    'fail_num': fail_num,
                    'not_submit': total_num - (adopt_num + fail_num),
                    'field': field_num
                }
                self.company_data.append(company_arr)

    def get_company(self, e_data):
        company = e_data[:, 16]
        return self.company_names(company)

    def run(self, byname: {str}):
        self.set_file(byname)
        self.read_file()
        self.create_data_frame()
        self.create_file_path()
        self.data_to_ex()


if __name__ == "__main__":
    project_byname = ['XYL', 'MOB']
    for byname in project_byname:
        if byname == 'MOB':
            Mob().run(byname)
        else:
            ReadExcel().run(byname)
    print('complete')
