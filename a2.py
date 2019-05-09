import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt
import datetime
import re

# data = pd.read_csv('data.csv', encoding='gbk') #因为数据中含有中文数据
# df = pd.read_csv('data_input/data_lx.csv', header=0, nrows=1000)
# df = pd.read_csv('data_input/h.csv',usecols=['日期','期货品种','名次','会员简称0','成交量(手)'])
df = pd.read_csv('data_input/h.csv')
print(df.index)

print(df.shape)  # 查看维度

print(df.columns)  # 查看列名
print(df.info())  # 查看数据类型和内存信息
# df.drop('合计',axis=1,inplace=True)
# df = sort_index(axis=0, level=None, ascending=True, inplace=False, kind='quicksort', na_position='last',
# sort_remaining=True, by=None)


# 改列名称
new_names = {'日期': '日期', '期货品种': '期货品种', '名次': '名次', '会员简称0': '会员简称', '成交量（手）': '成交量', '增减量0': '增减量', '会员简称1': '会员简称',
             '持买仓量': '持买仓量', '增减量1': '增减量', '会员简称2': '会员简称', '持卖仓量': '持卖仓量', '增减量2': '增减量'}
df.rename(columns=new_names, inplace=True)

# df.columns = ['a', 'b', 'c', 'd', 'e','1','2','3','4','5','6','7']
# print(df)
# 日期	期货品种	名次	会员简称0	成交量（手）	增减量0	会员简称1	持买仓量	增减量1	会员简称2	持卖仓量	增减量2'
print(df.head())
# loandata['term']=loandata['term'].map(str.strip)
print(df.sort_values(by="名次"))
# chooses = df['名次'].drop_duplicates().index
df[df['名次'] == '合计']

print(df.head())
print(df.duplicated())
print(df.dtypes)
# df['成交量']=df['成交量'].astype(np.int64)

df['日期'] = pd.to_datetime(df['日期'])
# df=pd.DataFrame(df, columns=['名次'])
df = df[~df['名次'].isin(['合计'])]
df = df[~df['持卖仓量'].isin(['持卖仓量'])]
# df[['名次', '成交量']] = df[['名次', '成交量']].astype(float)
print(df)
df = df.infer_objects()
df.to_csv('data_input/H_good_1.csv')
df.dtypes
df.apply(pd.to_numeric, errors='ignore')
print(df.dtypes)
print(df.head(100))
print(df.dtypes)
#print(df)
# df = pd.DataFrame(df)
# df = df.infer_objects()
#
# # df[['成交量', '名次']] = df[['成交量', '名次']].astype(float)
# print(df.info())
# df.to_csv("pandas_data.csv", encoding="utf-8")
# aa = df.sort_values(by="期货品种")
# aa = df.loc[df["期货品种"] == "苹果AP"]
# # cc=aa.DataFrame.sort_values(by=‘会员简称’,axis=1,ascending=True, inplace=False, na_position=‘last’)
# aa.to_csv("appl1_1.csv", encoding="utf-8")
# print(df.dtypes)
# print(aa)
# cc = df.loc[df["期货品种"] == "AP905"]
# print(cc)
# print(cc.duplicated())
