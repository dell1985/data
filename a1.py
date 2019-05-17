import pandas as pd
import numpy as np
df = pd.read_csv('data_input/data_lx.csv')
print(df)
print(df.index)


# df.sort_index(ascending=False)
# #自动索引
b=pd.Series([9,8,7,7,5])
print(b)
#指定索引
b=pd.Series([9,8,7,7,5],index=['a','b','c','d','e'])
print(b)
#指定索引在第二位时，可以省略掉index=
b=pd.Series([9,8,7,7,5],['a','b','c','d','e'])
print(b)
a=[1,2,3,4,5]
i=['a','b','c','d','e']
#可以通过列表来创建Series
b=pd.Series(a,i)
print(b)
s=pd.Series(100,index=[i])
print(s)
#可以通过字典来创建Series,键就是索引
s={'a':1,'b':2,"c":3,"d":4,"e":5}
s=pd.Series(s)
print(s)
#以新的索引替代原来的键
i=['e','d','c','b','a']
s=pd.Series(s,index=i)
print(s)
i=['f','e','d','c','b','a']
#如果指定索引个数大于原来值的个数，空的索引的值用"NaN"表示
s=pd.Series(s,index=i)
print(s)
#从ndarray创建Series
n=pd.Series(np.arange(5))
print(n)
n=pd.Series(np.arange(5),index=np.arange(9,4,-1))
print(n)
n=pd.Series(np.arange(5),index=np.arange(9,14))
print(n)

n=pd.Series(np.arange(10))#查看维度
print(n)
print(df.shape)
print(df.columns)#查看列名
print(df.info())#查看索引、数据类型、内存信息
print(df.describe())
df['持卖仓量']=df['持卖仓量'].str.replace(",","")
print(df.head(1000))