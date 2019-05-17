import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
import datetime
import re


#本程序处理用scrapy 爬回的交易信息 h.csv

#-------------数据清理--------------

df = pd.read_csv('data_input/h.csv')
print(df.index)
#df['成交量','增减量.1', '持买仓量','增减量1','持卖仓量','增减量2'] = df['成交量','增减量.1', '持买仓量','增减量1','持卖仓量','增减量2'].str.replase(",","")
#df=df.replace(",","")
#df['持卖仓量'] = df['持卖仓量'].astype(int)
df['成交量（手）']=df['成交量（手）'].str.replace(",","")
df['增减量0']=df['增减量0'].str.replace(",","")
df['持买仓量']=df['持买仓量'].str.replace(",","")
df['增减量1']=df['增减量1'].str.replace(",","")
df['持卖仓量']=df['持卖仓量'].str.replace(",","")
df['增减量2']=df['增减量2'].str.replace(",","")
df = df.infer_objects()
#df[['持卖仓量']] = df[['持卖仓量']].astype('int')

#df[["持卖仓量"]] = df[["持卖仓量"]].astype("int")
#df['持卖仓量']=pd.to_numeric(df['持卖仓量'])
#df[['持卖仓量']] = df[['持卖仓量']].apply(pd.to_numeric)
print(df.head(1000))
print(df.dtypes)
print(df.info())
#df["持卖仓量"]=pd.to_numeric(df["持卖仓量"])
df.apply(pd.to_numeric, errors='ignore')
print(df.dtypes)