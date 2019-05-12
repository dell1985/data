import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
import datetime
import re
#本文件处理生成各期货品种
df = pd.read_csv('data_input/h_m1.csv')
df = df.reset_index(drop=True)#重新索引
df = df[~df['期货品种'].isin(['苹果AP'])]
print(df.head(222))
#-----------------end-----------------------