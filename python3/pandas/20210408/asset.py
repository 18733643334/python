#!/usr/bin/env python3

from datetime.
from database.DataBaseHandle import DataBaseHandle as DB
import pandas as pd
import numpy as np

db = DB()

def main():
	asset_sql = '''
		select * from oa_asset where id = 1
	'''
	res = db.selectDb(asset_sql)
	print(res)
	
if __name__ == '__main__':
	main()
	
	