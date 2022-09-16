#!/usr/bin/env python3

import pandas as pd

data = pd.read_excel('rzsj.xlsx')
data = data.dropna(how='all')
print(data)
