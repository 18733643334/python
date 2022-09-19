#!/usr/bin/env python3


from PyQt5.QtWidgets import *
import sys, os, pandas as pd
import numpy as np
import re, time, subprocess, stat

extensions = ['xlsx', 'xls']


class ReadExcel:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.mainWindow = QMainWindow()
        self.new_file_path = ''
        self.file_path = ''
        self.excel_new_data = np.array([])
        self.excel_files = []
        self.company_data = []
        self.new_data = []
        self.frame_data = []
        self.root_path = ''

    def open_file(self):
        self.file_path = QFileDialog.getExistingDirectory(self.mainWindow)

    def read_file(self):
        for root, dirs, files in os.walk(self.file_path):
            self.root_path = root
            if files:
                for file in files:
                    file_list = file.split('.')
                    extension = file_list[-1]
                    if extension in extensions:
                        re_str1 = '^[a-z]{3}_[a-z]{3}_[a-zA-Z]+_[0-9]{3}shotInfo_v[0-9]{4}.xl'
                        # re_str2 = '^[a-z]{3}_[a-z]{3}_[a-zA-Z]+_000shotInfo_v[0-9]{4}.xl'
                        # if re.match(re_str1, file) and not re.match(re_str2, file):
                        #     self.excel_files.append(os.path.join(root, file))
                        if re.match(re_str1, file):
                            self.excel_files.append(os.path.join(root, file))

            else:
                self.message(False, '未找到文件~!')
                sys.exit()
        self.read_excel()

    # def read_excel(self):
    #     if not self.excel_files:
    #         self.message(False, '未找到Excel表格')
    #     for excel_file in self.excel_files:
    #         print(excel_file)
    #         excel_data = pd.read_excel(excel_file, header=10, dtype=object)
    #         excel_data = excel_data.dropna(axis=0, how='all')
    #         excel_data = excel_data.dropna(axis=1, how='all')
    #         excel_array = np.array(excel_data)[:-1]
    #         print(self.excel_new_data)
    #         print(excel_array)
    #         if len(self.excel_new_data) == 0:
    #             self.excel_new_data = excel_array
    #         else:
    #             self.excel_new_data = np.row_stack(self.excel_new_data, excel_array)
    #     print(self.excel_new_data)

    def read_excel(self):
        if not self.excel_files:
            self.message(False, '未找到Excel表格~!')
            sys.exit()
        self.message(True, '玩命加载中。。。。。')
        self.create_file_path()
        for excel_file in self.excel_files:
            excel_data = pd.read_excel(excel_file, header=10, dtype=object)
            excel_data = excel_data.dropna(axis=0, how='all')
            excel_array = np.array(excel_data)[:-1]
            if len(excel_array) == 0:
                continue
            # field_num = self.get_field_num(excel_array)
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

    def run(self):
        self.open_file()
        self.read_file()
        self.create_data_frame()
        self.data_to_ex()

    def message(self, m_type, message):
        if m_type:
            QMessageBox.information(self.mainWindow, '提示', message)
        else:
            QMessageBox.critical(self.mainWindow, '错误', message)

    def data_to_ex(self):
        self.frame_data = pd.DataFrame(self.new_data, columns=['场号', '公司名称', '镜头总数', '完成数', '未完成数', '占比']).sort_values(
            by='场号')
        df = self.frame_data.style.applymap(self.set_field_color, subset=['场号']).set_properties(subset=['镜头总数'], **{
            "background-color": "#FED563"}).set_properties(subset=['完成数'], **{
            "background-color": "#66A342"}).set_properties(subset=['未完成数'], **{
            "background-color": "#FED563"}).set_properties(subset=['占比'], **{
            "background-color": "#FFFF2E"})
        df.to_excel(self.new_file_path, index=False)
        self.complete()

    def dd(self, d=''):
        print(d)
        sys.exit()

    def complete(self):
        self.message(True, '处理完成~！')
        self.open_new_file()

    def open_new_file(self):
        os.chmod(self.new_file_path, stat.S_IRWXU)
        os.system('open %s' % self.root_path)
        os.system('open %s' % self.new_file_path)
        sys.exit('结束~!')

    def get_u_field(self):
        field = list(self.frame_data.loc[:, '场号'])
        s_field = set(field)
        u_field = []
        for s in s_field:
            if field.count(s) > 1:
                u_field.append(s)
        u_field = np.unique(np.array(u_field))
        return u_field

    def set_field_color(self, col):
        u_field = self.get_u_field()
        if col in u_field:
            return "background-color: #FFFF2E"

    def create_file_path(self):
        t = time.gmtime()
        date = time.strftime("%m-%d", t)
        name = 'outsource' + str(date)
        self.new_file_path = self.root_path + '/%s.xlsx' % name


if __name__ == "__main__":
    ReadExcel().run()
