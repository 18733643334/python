from database.DataBaseHandle import DataBaseHandle as DB
import pandas as pd

db = DB()

def main():
    project_sql = '''
        select `id`,`project_byname` from oa_project where `is_show` = %d
    ''' % (1)
    project_data = db.selectDb(project_sql)
    new_data = []

    for p_item in project_data:
        shot_sql = '''
            select `alled_name`,`clip_frame_length` from oa_shot where `project_id` = %s and `is_show` = %d
        ''' % (p_item['id'], 2)
        shot_data = db.selectDb(shot_sql)

        for s_item in shot_data:
            arr = []
            arr.append(p_item['project_byname'])
            arr.append(s_item['alled_name'])
            arr.append(s_item['clip_frame_length'])
            new_data.append(arr)

    df = pd.DataFrame(new_data, columns=['项目简称', '场号镜头号', '剪辑帧长'])
    df.to_excel('project_shot.xlsx', index=False)

if __name__ == '__main__':
    main()
