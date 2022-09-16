from database.DataBaseHandle import DataBaseHandle as DB
import pandas as pd
import time

db = DB()

def main():
    sql = '''
        select P.project_name,P.project_byname,A.* from oa_asset as A left join oa_project as P on A.project_id = P.id where A.is_show = 2 and A.status != 35 and P.id != 17 order by P.id DESC
    '''
    data = db.selectDb(sql)
    new_data = []
    for item in data:
        arr = []
        arr.append(item['project_name'])
        arr.append(item['project_byname'])
        arr.append(item['alled_name'])
        # `difficulty` tinyint(3) DEFAULT '1' COMMENT '镜头难度1D 2C 3B 4A 5S',
        if item['difficulty'] == 1:
            arr.append('D')
        elif item['difficulty'] == 2:
            arr.append('C')
        elif item['difficulty'] == 3:
            arr.append('B')
        elif item['difficulty'] == 4:
            arr.append('A')
        elif item['difficulty'] == 5:
            arr.append('S')
        elif not item['difficulty']:
            arr.append('D')
        timeArr = time.localtime(item['create_time'])
        ctime = time.strftime("%Y-%m-%d", timeArr)
        arr.append(ctime)
        new_data.append(arr)
    df = pd.DataFrame(new_data, columns=['项目名称', '项目简称', '资产名称', '难度', '创建日期'])
    df.to_excel('asset_info.xlsx', index=False)



if __name__ == '__main__':
    main()
