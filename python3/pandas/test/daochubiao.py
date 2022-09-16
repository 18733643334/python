import pandas as pd
import requests as re

column = ['a', 'b', 'c', 'd']

column.insert(0, '项目名称')
column.insert(1, '环节名称')

print(column)
df = pd.DataFrame(columns=column)

# df.to_excel('abc.xlsx', index=False)