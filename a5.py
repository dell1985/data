import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
import datetime
import re

df = pd.read_csv('data_input/h_good_1.csv',usecols=[2])


print(df)
df.drop_duplicates(subset=None,inplace=True)# 去重
print(df)
df.sort_values()

# df = df.reset_index(drop=True)#重新索引
# print(len(df))
# print(df)
