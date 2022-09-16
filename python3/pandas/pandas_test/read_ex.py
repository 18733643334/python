import pandas as pd
import numpy as np
import sys


def dd(d):
    print(d)
    sys.exit()


df = pd.read_excel('032.xlsx', dtype=object)
data = np.array(df)

for index, item in enumerate(data):
    print(index)
    dd(item)
