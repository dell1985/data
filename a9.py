import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
import datetime
import re
#本文件处理生成各期货品种
df = pd.read_csv('data_input/h_m1.csv')
df = df[df['期货品种'].isin(['苹果AP'])]
df[ df['期货品种'].str.contains('苹果AP') ]#从df中筛选出"苹果AP"
#df[df['期货品种'] == '苹果AP']

print(df)
#重新排序
# print(df)
df = df.reset_index(drop=True)#重新索引
print(df)

#print(df.head(1222))
#-----------------end-----------------------