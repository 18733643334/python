from tron_py.common.model import Model


class ChildTask(Model):
    def __init__(self):
        super().__init__()
        self.table_name = "child_task"
        self.table()

