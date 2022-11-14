from tron_py.common.model import Table

get_sql = '''
    select id,resource_id,resource_type from oa_res_relation where field_id is null
'''
relation_data = Table().query(get_sql)
for rd in relation_data:
    resource_type = rd['resource_type']
    resource_id = rd['resource_id']
    relation_id = rd['id']
    print(relation_id, resource_id, resource_type)
    if resource_type == 1:
        get_shot_sql = '''
            select * from oa_shot where id = %s
        ''' % (resource_id)
        shot_data = Table().query(get_shot_sql)
        print(shot_data)
        raise SystemExit()
        field_id = shot_data['field_id']
    elif resource_type == 2:
        get_asset_sql = '''
            select * from oa_asset where id = %s
        ''' % (resource_id)
        asset_data = Table().query(get_asset_sql)
        field_id = asset_data['field_id']

    update_sql = '''
        update oa_res_relation set field_id = %s where id = %s
    ''' % (field_id, relation_id)
    print(update_sql)
