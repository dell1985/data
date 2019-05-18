import pandas as pd
import numpy as np



#本程序处理用scrapy 爬回的交易信息 h.csv

#-------------数据清理--------------

df = pd.read_csv('data_input/h.csv')
df=df.replace(" ","")
df['名次']=df['名次'].replace("-","")
df['会员简称0']=df['会员简称0'].replace("-","")
df['会员简称1']=df['会员简称1'].replace("-","")
df['会员简称2']=df['会员简称2'].replace("-","")
df['成交量（手）']=df['成交量（手）'].str.replace(",","")
df['成交量（手）']=df['成交量（手）'].replace("-","0")

df['增减量0']=df['增减量0'].str.replace(",","")
df['增减量0']=df['增减量0'].replace("-","0")

df['持买仓量']=df['持买仓量'].str.replace(",","")
df['持买仓量']=df['持买仓量'].replace("-","0")
df['增减量1']=df['增减量1'].str.replace(",","")
df['增减量1']=df['增减量1'].replace("-","0")
df['持卖仓量']=df['持卖仓量'].str.replace(",","")
df['持卖仓量']=df['持卖仓量'].replace("-","0")
df['增减量2']=df['增减量2'].str.replace(",","")
df['增减量2']=df['增减量2'].replace("-","0")


df[df['名次'] == '合计']
df = df[~df['名次'].isin(['合计'])]
df = df[~df['持卖仓量'].isin(['持卖仓量'])]



df['日期'] = pd.to_datetime(df['日期'])
df['名次']= df['名次'].astype(np.int)
#df['名次']= df['名次'].astype(int),也可以用这个方法
df['成交量（手）']= df['成交量（手）'].astype(np.int)
df['增减量0']= df['增减量0'].astype(np.int)
df['持买仓量']= df['持买仓量'].astype(np.int)
df['增减量1']= df['增减量1'].astype(np.int)
df['持卖仓量']= df['持卖仓量'].astype(np.int)
df['增减量2']= df['增减量2'].astype(np.int)


#-------------存入文件--------------

df.to_csv('data_output/h_good.csv')
print(df.info())
print(df.dtypes)