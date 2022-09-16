#!/usr/bin/env python3

from pytron43.common.model import Model, DataBaseHandle

project_ids = Model('project').field('id').where('sort', '<>', 100).select()

for project_id, in project_ids:
    shot_ids = Model('shot').field('id,field_id').where('project_id', '=', project_id).where('status', '<', 5).where(
        'is_show', '=', 2).select()
    for shot_id, field_id in shot_ids:
        check_relation = Model('res_relation').where('resource_id', '=', shot_id).where('resource_type', '=', 1).get()
        if check_relation == None:
            insert_sql = '''
                insert into oa_res_relation (field_id, resource_id, resource_type) values (%d, %d, %d)
            ''' % (field_id, shot_id, 1)
            db = DataBaseHandle()
            db.insertDB(insert_sql)
            print("relation 表增加 resource_id：%d 成功" % shot_id)

print('完成')
