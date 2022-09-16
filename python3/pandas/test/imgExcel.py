import pandas as pd
import numpy as np
from PIL import Image
import json
import sys

fp = open('111.json', 'r')
data = fp.read()
fp.close()
data = np.array(json.loads(data))
new_data = []
img = Image.open('20200818/1596616898432.jpg')
print(img.size)
for d in data:
    arr = []
    arr.append(d['alled_name'])
    arr.append(d['content'])
    arr.append(d['field_name'])
    arr.append(d['tache_name'].lower())
    arr.append(d['company_name'])
    arr.append(d['realname'])
    arr.append(d['project_name'])
    arr.append(d['version'])
    new_data.append(arr)
df = pd.DataFrame(new_data, columns=['镜头号', '反馈内容', '场号', '环节简称', '公司名称', '用户名', '项目名', '版本号'])
df.to_excel('123.xlsx', index=False)
