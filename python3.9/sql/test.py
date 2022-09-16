
from pytron43.common.model import DataBaseHandle

get_user_sql = '''
    select * from oa_admin_user where is
'''
users = DataBaseHandle.selectDb()
