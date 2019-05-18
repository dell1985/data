import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
import re

#从经过整理后的 h_good_1.csv中分别生成 1、成交量，2、持买仓量，3、持卖仓量三个csv文件

#-------------------分段读取组成新文件-----------------
#data = pd.read_csv('data.csv', encoding='gbk') #因为数据中含有中文数据
#df = pd.read_csv('data_input/data_lx.csv', header=0, nrows=1000)
#df = pd.read_csv('data_input/h.csv',usecols=['日期','期货品种','名次','会员简称0','成交量(手)'])

#--------------------生成期货品种文件--------------------
df = pd.read_csv('data_input/h_good_1.csv',usecols=[2])
df.to_csv('data_input/name.csv',index=None)
print(df.head(100))
#--------------------生成成交量文件--------------------
df = pd.read_csv('data_input/h_good_1.csv',usecols=[1,2,3,4,5,6])
print(df.index)
df.to_csv('data_input/h_cjl.csv',index=None)
print(df.head(100))
#--------------------生成持买仓量文件--------------------
df = pd.read_csv('data_input/h_good_1.csv',usecols=[1,2,3,7,8,9])
new_names = {'日期': '日期', '期货品种': '期货品种', '名次': '名次', '会员简称.1': '会员简称', '成交量（手）': '成交量', '增减量.1': '增减量', '会员简称1': '会员简称',
             '持买仓量': '持买仓量', '增减量1': '增减量', '会员简称2': '会员简称', '持卖仓量': '持卖仓量', '增减量2': '增减量'}
df.rename(columns=new_names, inplace=True)

print(df.index)
print(df.dtypes)
df.to_csv('data_input/h_m1.csv',index=None)
print(df.head(100))

#--------------------生成持卖仓量文件--------------------
df = pd.read_csv('data_input/h_good_1.csv',usecols=[1,2,3,10,11,12])
new_names = {'日期': '日期', '期货品种': '期货品种', '名次': '名次', '会员简称.2': '会员简称', '成交量（手）': '成交量', '增减量.2': '增减量', '会员简称1': '会员简称',
             '持买仓量': '持买仓量', '增减量1': '增减量', '会员简称2': '会员简称', '持卖仓量': '持卖仓量', '增减量2': '增减量'}
df.rename(columns=new_names, inplace=True)

print(df.index)
df.to_csv('data_input/h_m2.csv',index=None)
print(df.head(100))



