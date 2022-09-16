import sys
from database.DataBaseHandle import DataBaseHandle


def dd(d=''):
    print(d)
    sys.exit()


def main(type):
    pass


def list_of_groups(init_list, childern_list_len):
    list_of_groups = zip(*(iter(init_list),) * childern_list_len)
    end_list = [list(i) for i in list_of_groups]
    count = len(init_list) % childern_list_len
    end_list.append(init_list[-count:]) if count != 0 else end_list
    return end_list


if __name__ == '__main__':
    resource_type = 1
    if type == 1:
        shot_sql = '''
            SELECT id FROM oa_shot WHERE is_show = 2
        '''
        resource = DataBaseHandle.selectDb(shot_sql)
        dd(resource)
    main(resource_type)
