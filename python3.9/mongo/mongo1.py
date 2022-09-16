#!/usr/bin/env python3

import pymongo

clint = pymongo.MongoClient('mongodb://127.0.0.1:27017/')

base = clint['tron']

tables = base.list_collection_names()

admin_user = base["admin_user"]

a = admin_user.find()
print(a)