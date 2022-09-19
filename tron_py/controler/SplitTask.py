from tron_py.common.model import Table
from tron_py.common.model import MainTask
from tron_py.common.model import ChildTask
from tron_py.common.model import Version

fields = MainTask().get_columns()
fields.pop(0)
child_task_columns = ChildTask().get_columns()
child_task_columns.pop(0)

from tron_py.common.model import VersionStatusRecord
from tron_py.common.model import TaskStatusRecord


def clen_project_task(project_id):
    master_data = Table('task').where('project_id', '=', project_id).where('category', '=', 0).where('is_show', '=',
                                                                                                     2).select()
    total_num = len(master_data)
    c_num = 1
    for master_task in master_data:
        new_master_data = []
        old_master_id = master_task['id']
        for field in fields:
            old_field = field
            if old_field == 'res_id':
                old_field = 'resource_id'
            if old_field == 'actually_start_time':
                old_field = 'actually_start_timestamp'
            if old_field == 'actually_end_time':
                old_field = 'actually_end_timestamp'
            if not old_field in master_task.keys():
                continue
            elif master_task[old_field] == None:
                master_task[old_field] = ''
            t_list = (field, master_task[old_field])
            new_master_data.append(t_list)
        new_master_data = dict(new_master_data)
        new_master_task_id = MainTask().create(new_master_data)
        TaskStatusRecord().update_task_id(old_master_id, new_master_task_id, 1)
        # print("原主任务id：%s 新主任务id：%s 更改完成" % (old_master_id, new_master_task_id))
        sub_task_data = Table('task').where('pid', '=', old_master_id).where('is_show', '=', 2).select()
        for sub_task in sub_task_data:
            new_child_data = []
            old_child_id = sub_task['id']
            for child_task_column in child_task_columns:
                old_child_filed = child_task_column
                if old_child_filed == 'res_id':
                    old_child_filed = 'resource_id'
                if old_child_filed == 'actually_start_time':
                    old_child_filed = 'actually_start_timestamp'
                if old_child_filed == 'actually_end_time':
                    old_child_filed = 'actually_end_timestamp'
                if not old_child_filed in sub_task.keys():
                    continue
                elif sub_task[old_child_filed] == None:
                    sub_task[old_child_filed] = ''
                ct_list = (child_task_column, sub_task[old_child_filed])
                new_child_data.append(ct_list)
            new_child_data = dict(new_child_data)
            new_child_data['pid'] = new_master_task_id
            new_child_task_id = ChildTask().create(new_child_data)
            TaskStatusRecord().update_task_id(old_child_id, new_child_task_id, 2)
            # print("原子任务id：%s 新子任务id：%s 更改完成" % (old_master_id, new_master_task_id))
            Version().update_task_id(old_child_id, new_child_task_id)
            VersionStatusRecord().update_task_id(old_child_id, new_child_task_id)
        proportion = round(c_num / total_num, 2) * 100
        proportion_num = int(proportion)
        print("\r项目id：%s|%s|%s%%" % (project_id, "#" * proportion_num, proportion), end="")
        c_num += 1


if __name__ == '__main__':
    project_ids = Table('project').where('is_show', '=', 1).field('id').select()
    for i in project_ids:
        project_id = i['id']
        clen_project_task(project_id)

print("执行完毕~!")
