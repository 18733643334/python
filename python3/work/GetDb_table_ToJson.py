# coding = utf-8

import pymysql, json
import sys


class DbTable_toJson:
    def __init__(self):
        self.host = "192.168.100.247"
        self.user = "root"
        self.password = "king9188YJQ@"
        self.db = "new_tron"
        self.port = 3306

    def UserTableToJson(self):
        try:
            conn = pymysql.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.db,
                port=self.port
            )
            # 获取一个光杆，等待输入sql语句
            cursor = conn.cursor()
            # 备份专用 获取所有用户名
            # sql = "select username from oa_admin_user where id != 1 and department_id != 4"
            sql = "select username,realname,department_id from oa_admin_user where is_del = %s and id != %s and department_id != %s;" % (
                2, 1, 4)
            cursor.execute(sql)
            data = cursor.fetchall()
            cursor.close()
            conn.close()
            jsonData = []
            for row in data:
                result = {}
                if row[2] == 0:
                    result['department'] = '非制作部'
                else:
                    result['department'] = '制作部'
                result['username'] = row[0]
                result['realname'] = row[1]
                # 备份专用 获取所有用户名
                # result = []
                # result = row[0]
                jsonData.append(result)
        except:
            print("Mysql connet fail ....")
        else:
            # 使用json.dumps将数据转换为json格式，json.dumps方法默认会输出成这种格式"\u5377\u76ae\u6298\u6263"，加ensure_ascii=False，则能够防止中文乱码。
            # JSON采用完全独立于语言的文本格式，事实上大部分现代计算机语言都以某种形式支持它们。这使得一种数据格式在同样基于这些结构的编程语言之间交换成为可能。
            # json.dumps()是将原始数据转为json（其中单引号会变为双引号），而json.loads()是将json转为原始数据。
            format_json_data = json.dumps(jsonData, ensure_ascii=False)
            # 去除首尾的中括号
            # return format_json_data[1:len(format_json_data) - 1]
            return format_json_data

    def ProjectsTableToJson(self):
        try:
            conn = pymysql.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.db,
                port=self.port
            )
            # 获取一个光杆，等待输入sql语句
            cursor = conn.cursor()
            sql = "select project_byname,project_name from oa_project;"
            cursor.execute(sql)
            data = cursor.fetchall()
            cursor.close()
            conn.close()
            jsonData = []
            for row in data:
                result = {'project_byname': row[0].lower(), 'project_name': row[1]}
                jsonData.append(result)
        except:
            print("Mysql connet fail ....")
        else:
            # 使用json.dumps将数据转换为json格式，json.dumps方法默认会输出成这种格式"\u5377\u76ae\u6298\u6263"，加ensure_ascii=False，则能够防止中文乱码。
            # JSON采用完全独立于语言的文本格式，事实上大部分现代计算机语言都以某种形式支持它们。这使得一种数据格式在同样基于这些结构的编程语言之间交换成为可能。
            # json.dumps()是将原始数据转为json（其中单引号会变为双引号），而json.loads()是将json转为原始数据。
            format_json_data = json.dumps(jsonData, ensure_ascii=False)
            # 去除首尾的中括号
            # return format_json_data[1:len(format_json_data) - 1]
            return format_json_data


# 生成json文件
def createJsonFile():
    json_obj = DbTable_toJson()
    user_jsonData = json_obj.UserTableToJson()
    f = open('user_data.json', 'w+')
    f.write(user_jsonData)
    f.close()
    project_jsonData = json_obj.ProjectsTableToJson()
    f = open('project_data.json', 'w+')
    f.write(project_jsonData)
    f.close()


if __name__ == '__main__':
    createJsonFile()
