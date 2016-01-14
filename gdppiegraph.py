# -*- coding: utf-8 -*-
# 十大城市GDP饼图

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# quants: GDP
# labels: city name
labels   = []
quants   = []


#读取数据
homedir = os.getcwd()
pd = pd.read_csv(homedir + '\CityGDP.csv')
for i in range(len(pd['City'])):
    labels.append(pd['City'][i])
    quants.append(pd['GDP'][i])

 
#画图
plt.figure(1, figsize=(6,6))
def explode(label, target='Shanghai'):
    if label == target: return 0.1
    else: return 0
expl = map(explode,labels)
colors  = ["pink","coral","yellow","orange"]
plt.pie(quants, explode=expl, colors=colors, labels=labels, autopct='%1.1f%%',pctdistance=0.8, shadow=True)
plt.title('Top 10 GDP Cities', bbox={'facecolor':'0.8', 'pad':5})
plt.show()
