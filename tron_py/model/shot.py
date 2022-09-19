#!/usr/bin/env python3

from tron_py.common.model import Model


class Shot(Model):
    def __init__(self):
        super().__init__()
        self.table_name = "shot"
        self.table()
