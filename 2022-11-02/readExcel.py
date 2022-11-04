import os, re, pandas as pd
import numpy as np

extensions = ['xlsx', 'xls']


class ReadExcel():
    def __init__(self):
        self.status_data = ['客户通过', '客户反馈', '内部通过', '内部反馈', '送审提交', '正式提交']

    def read_file(self):
        file_names = os.listdir('linmh')
        if file_names:
            for file in file_names:
                file_list = file.split('.')
                extension = file_list[-1]
                if extension in extensions:
                    re_str1 = '^[a-z]{3}_[a-z]{3}_[a-zA-Z]+_[0-9]{3}shotInfo_v[0-9]{4}[.]{1}xlsx$'
                    if re.match(re_str1, file):
                        self.read_excel(file)

    def read_excel(self, file):
        path_file = 'linmh/{}'.format(file)
        excel_data = pd.read_excel(path_file, header=10, dtype=object)
        excel_data = excel_data.dropna(axis=0, how='all')
        excel_array = np.array(excel_data)[:-1]
        company_names = self.get_company(excel_array)
        field_num = self.get_field_num(path_file)
        for company in company_names:
            for status in self.status_data:
                rate_lenth = 0
                for i in excel_array:
                    pass
                # arr = {
                #     'field': field_num,
                #     'company_name': company,
                #     'status': status,
                # }

    def get_company(self, e_data):
        company = e_data[:, 17]
        return self.company_names(company)

    def company_names(self, c_data):
        company = list(set(c_data))
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

    def run(self):
        self.read_file()


if __name__ == '__main__':
    ReadExcel().run()
