from tron_py.common.model import Model


class User(Model):
    def __init__(self):
        super().__init__()
        self.table_name = "admin_user"
        self.table()
