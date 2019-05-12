import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
import datetime
import re
'日期','期货品种','名次','会员简称0','成交量（手）','增减量0'
#data = pd.read_csv('data.csv', encoding='gbk') #因为数据中含有中文数据
#df = pd.read_csv('data_input/data_lx.csv', header=0, nrows=1000)
#df = pd.read_csv('data_input/h.csv',usecols=['日期','期货品种','名次','会员简称0','成交量(手)'])
df = pd.read_csv('data_input/h.csv')
print(df.index)

df.duplicated()    #       返回各行是否是上一行的重复行
df.drop_duplicates()

print(df.head(100))
# #保存到文件
# #df.to_csv('data_input/1.csv')
# print(df.shape)  # 查看维度
# #
# print(df.columns)  # 查看列名
# print(df.info())  # 查看数据类型和内存信息
# #df.drop('合计',axis=1,inplace=True)
#
# # #df = sort_index(axis=0, level=None, ascending=True, inplace=False, kind='quicksort', na_position='last',
# #                 #sort_remaining=True, by=None)
# #
# #
# #改列名称
# #1、建立老-新列名的列表
# new_names={'日期':'日期','期货品种':'期货品种','名次':'名次','会员简称0':'会员简称','成交量（手）':'成交量','增减量0':'增减量','会员简称1':'会员简称','持买仓量':'持买仓量','增减量1':'增减量','会员简称2':'会员简称','持卖仓量':'持卖仓量','增减量2':'增减量'}
# print(df.columns)
# #替换列名
# df.rename(columns=new_names,inplace=True)
#
# #日期	期货品种	名次	会员简称0	成交量（手）	增减量0	会员简称1	持买仓量	增减量1	会员简称2	持卖仓量	增减量2'
# print(df.head())
# # #loandata['term']=loandata['term'].map(str.strip)
# # print(df.sort_values(by="名次"))
# chooses = df['名次'].drop_duplicates().index
# df[ df['名次'] =='合计']
# print(df)
# print(df.head())
# print(df.duplicated())
# print(df.dtypes)
# # #df['成交量']=df['成交量'].astype(np.int64)
# #修改日期格式
# df['日期']=pd.to_datetime(df['日期'])
# print(df.dtypes)
# #df=pd.DataFrame(df, columns=['名次'])
# df=df[~df['名次'].isin(['合计'])]
# print(df)
# df=df[~df['持卖仓量'].isin(['持卖仓量'])]
# # #df[['名次', '成交量']] = df[['名次', '成交量']].astype(float)
# print(df)
# # df = df.infer_objects()
# # df.dtypes
# # df.apply(pd.to_numeric, errors='ignore')
# # print(df.dtypes)
# # print(df.head())
# #
# # df = pd.DataFrame(df)
# # df = df.infer_objects()
# #
# # #df[['成交量', '名次']] = df[['成交量', '名次']].astype(float)
# # print(df.info())
# # df.to_csv("pandas_data.csv",encoding="utf-8")
# # aa=df.sort_values(by="期货品种")
# # aa=df.loc[df["期货品种"] == "苹果AP"]
# # #cc=aa.DataFrame.sort_values(by=‘会员简称’,axis=1,ascending=True, inplace=False, na_position=‘last’)
# #
# #
# # print(aa)
# # #bb=aa.sort_values(by="会员简称")df[(df.D>0)&(df.C<0)]
# # #aa=aa[(aa.f.期货品种=='苹果AP')]
# # # ww=df.DataFrame.isDataFrame.isnull
# # # print(df.)
# # print(aa)
# # # print(df.loc[:,'会员简称0':'持买仓量'])  # 筛选列
# # print(df.loc['20181026':'20181022', :])  # 筛选行