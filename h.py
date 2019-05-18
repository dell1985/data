import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
import re


#本程序处理用scrapy 爬回的交易信息 h.csv

#-------------数据清理--------------

df = pd.read_csv('data_input/h.csv')
print(df.index)

print(df.shape)  # 查看维度

print(df.columns)  # 查看列名
print(df.info())  # 查看数据类型和内存信息




df=df.replace(" ","")
df['名次']=df['名次'].str.replace("-","")

df['成交量（手）']=df['成交量（手）'].str.replace(",","")
df['成交量（手）']=df['成交量（手）'].str.replace("-","0")

df['增减量0']=df['增减量0'].str.replace(",","")
df['增减量0']=df['增减量0'].str.replace("-","0")

df['持买仓量']=df['持买仓量'].str.replace(",","")
df['持买仓量']=df['持买仓量'].str.replace("-","0")
df['增减量1']=df['增减量1'].str.replace(",","")
df['增减量1']=df['增减量1'].str.replace("-","0")
df['持卖仓量']=df['持卖仓量'].str.replace(",","")
df['持卖仓量']=df['持卖仓量'].str.replace("-","0")
df['增减量2']=df['增减量2'].str.replace(",","")
df['增减量2']=df['增减量2'].str.replace("-","0")

# 改列名称
# new_names = {'日期': '日期', '期货品种': '期货品种', '名次': '名次', '会员简称0': '会员简称', '成交量（手）': '成交量', '增减量0': '增减量', '会员简称1': '会员简称',
#              '持买仓量': '持买仓量', '增减量1': '增减量', '会员简称2': '会员简称', '持卖仓量': '持卖仓量', '增减量2': '增减量'}
# df.rename(columns=new_names, inplace=True)

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


print(df)
df = df.infer_objects()

df.apply(pd.to_numeric, errors='ignore')
print(df.dtypes)
print(df.head(100))
print(df.dtypes)
#-------------数据清理完成--------------

print(df.columns)
df['名次']= df['名次'].astype(np.int)
df['成交量（手）']= df['成交量（手）'].astype(np.int)
df['增减量0']= df['增减量0'].astype(np.int)
df['持买仓量']= df['持买仓量'].astype(np.int)
df['增减量1']= df['增减量1'].astype(np.int)
df['持卖仓量']= df['持卖仓量'].astype(np.int)
df['增减量2']= df['增减量2'].astype(np.int)
print(df.dtypes)
# 改列名称
new_names = {'日期': '日期', '期货品种': '期货品种', '名次': '名次', '会员简称0': '会员简称', '成交量（手）': '成交量', '增减量0': '增减量', '会员简称1': '会员简称',
             '持买仓量': '持买仓量', '增减量1': '增减量', '会员简称2': '会员简称', '持卖仓量': '持卖仓量', '增减量2': '增减量'}
df.rename(columns=new_names, inplace=True)
print(df.head())
#-------------存入文件--------------
df.to_csv('data_input/H_good_1.csv')
