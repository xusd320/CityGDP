# -*- coding: utf-8 -*-
# 十大城市GDP柱形图

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
width = 0.4
ind = np.linspace(0.5,9.5,10)
fig = plt.figure(1, figsize=(12,6))
ax  = fig.add_subplot(111)
ax.bar(ind-width/2,quants,width,color='coral')
ax.set_xticks(ind)
ax.set_xticklabels(labels)
ax.set_xlabel('City')
ax.set_title('Top 10 GDP Cities', bbox={'facecolor':'0.8', 'pad':5})
plt.show()
