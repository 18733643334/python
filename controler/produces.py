from model.mainTask import MainTask
from common.model import Table
from model.childTask import ChildTask
from model.user import User
import json

# master_task = MainTask().where('produces', '=', "''").field('id').select()
main_task_sql = "SELECT id FROM oa_main_task WHERE produces IS NULL"
master_task = Table().query(main_task_sql)

j = 0
x = int(len(master_task))
for i in master_task:
    id = i['id']
    child_task = ChildTask().where('pid', '=', id).field('user_id,is_show').select()
    if child_task:
        produces_data = []
        for c in child_task:
            user_data = User().get(c['user_id'])
            if user_data:
                user_name = user_data['realname']
            else:
                break
            produces = {
                'name': user_name,
                'is_show': c['is_show']
            }
            produces_data.append(produces)
        produces_data = json.dumps(produces_data, ensure_ascii=False)
        MainTask().where('id', '=', id).update({"produces": produces_data})
    j += 1
