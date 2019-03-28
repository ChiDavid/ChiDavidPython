%matplotlib inline

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import locale
import time
from ipywidgets import interact

path = ('http://datacenter.taichung.gov.tw/swagger/OpenData/d9cad116-1255-4e97-94fc-d8dc58cd9ff9')
df = pd.read_csv(path)

mpl.rc('font', family='Noto Sans CJK TC')

df2 = df[(df.肇事逃逸.str.contains('否')) | (df.酒駕案件.str.contains('是'))]
df3 = df2.sort_values(by = ['事故類別'], ascending=False)
df3.hist(bins=30)
df3.mean()
