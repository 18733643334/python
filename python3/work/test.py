
import pandas as pd

data = pd.read_html('index.html', header=0)

print(data)