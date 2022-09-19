#!/usr/bin/env python3

from common.model.shot import Shot
import pandas as pd
import numpy as np

data = pd.read_excel('xyl001.xlsx',header=0, dtype=str)
data = np.array(data)
project_id = 61
field_id = 1041
for i in data:
    shot_name = i[2]
    dst_in = i[8]
    dst_out = i[9]
    update = {
        "dst_in": dst_in,
        "dst_out": dst_out
    }
    Shot().where('project_id', '=', project_id).where('field_id', '=', field_id).where('alled_name', '=', shot_name).update(update)
