import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
import datetime
import re
#本文件处理期货名称和各交割月份的代码
df = pd.read_csv('data_output/h_good.csv',usecols=[2])


print(df)
df.drop_duplicates(subset=None,inplace=True)# 去重
print(df)
df.sort_values("期货品种",inplace=True)#重新排序
print(df)
df = df.reset_index(drop=True)#重新索引
print(df)

print(df.head(222))
#-----------------end-----------------------