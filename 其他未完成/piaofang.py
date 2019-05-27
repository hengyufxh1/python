# -*- coding: utf-8 -*-
"""
Created on Tue May 21 18:04:21 2019

@author: YZLC004
"""
import pandas as pd

#列表
liebiao=[1,2.223,-3,'刘强东','章泽天','周杰伦','昆凌',['微博','B站','抖音']]

#ist是一个可变的有序表，所以，可以往list中追加元素到末尾：
liebiao.append('瘦')
print(liebiao)
# 插入到 0位
liebiao.insert(0, '胖')
print(liebiao)

#字典
zidian={'刘强东':'46','章泽天':'36','周杰伦':'40','昆凌':'26'}

zidian['周杰伦']


zidian={'刘强东':'46','章泽天':'36','周杰伦':'40','昆凌':'26'}
for key in zidian:
        print(key)
        

df=pd.DataFrame.from_dict(zidian,orient='index',columns=['age'])#注意DataFrame的D和F是大写
df=df.reset_index().rename(columns={'index':'name'})#给姓名加上字段名

url_df = pd.DataFrame({'urls':['http://www.cbooo.cn/BoxOffice/getWeekInfoData?sdate=' for i in range(5)],'date' :pd.date_range(20190114,freq = 'W-MON',periods = 5)})
import pandas as pd
data = pd.read_csv(url_df,engine='python')
data[data['平均上座人数']>20]['电影名']
#计算周票房第一随时间变化的结果，导入数据，并选择平均上座人数在20以上的电影为有效数据

dataTop1_week = data[data['排名']==1][['电影名','周票房']]
#取出周票房排名为第一名的所有数据，并保留“电影名”和“周票房”两列数据

dataTop1_week = dataTop1_week.groupby('电影名').max()['周票房'].reset_index()
#用“电影名”来分组数据，相同电影连续霸榜的选择最大的周票房保留，其他数据删除

dataTop1_week = dataTop1_week.sort_values(by='周票房',ascending=False)
#将数据按照“周票房”进行降序排序

dataTop1_week.index = dataTop1_week['电影名']
del dataTop1_week['电影名']
#整理index列，使之变为电影名，并删掉原来的电影名列

dataTop1_week
#查看数据