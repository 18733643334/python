import pymysql

res_type = int(input("请输入清洗镜头或资产 1 镜头 2 资产: "))
db = pymysql.connect(host='192.168.100.247', user='root', password='king9188YJQ@', database='revision_tron')
cursor = db.cursor()

res_relation_sql = '''
    select `id`,`res_id` from oa_res_relation where res_type = %s
''' % (res_type)

table = ''
if res_type == 1:
    table = 'oa_shot'
elif res_type == 2:
    table = 'oa_asset'
    

cursor.execute(res_relation_sql)
data = cursor.fetchall()
delete_num = 0
for i in data:
    delete_num += 1
    re_id = i[0]
    res_id = i[1]
    resource_sql = '''
        select id from %s where id = %s
    ''' % (table, res_id)
    cursor.execute(resource_sql)
    resource = cursor.fetchone()
    print(resource)
    if not resource:
        # 删除 没有的数据
        delete_sql = '''
            delete from oa_res_relation where id = %s
        ''' % (re_id)
        cursor.execute(delete_sql)
        db.commit()
        
print("删除了 %s 条数据" % (delete_num))
