#这是苹果AP的筛选程序



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

#重新排序
# print(df)
df = df.reset_index(drop=True)#重新索引

df.sort_values(['会员简称'])#按会员简称
df.sort_values(["会员简称","日期"],ascending=[1,0],inplace=True)#排序，paascending=[1,0]1降序，0升序
print(df.head(1000))
#-----------------end-----------------------

new_names = {'日期': '日期', '期货品种': '期货品种', '名次': '名次', '会员简称.2': '会员简称', '成交量（手）': '成交量', '增减量.2': '增减量', '会员简称1': '会员简称',
             '持买仓量': '持买仓量', '增减量1': '增减量', '会员简称2': '会员简称', '持卖仓量': '持卖仓量', '增减量2': '增减量'}
df.rename(columns=new_names, inplace=True)

print(df.index)
df.to_csv('data_input/apple_h_m1.csv',index=None)