# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 03:25:35 2024

@author: First build
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
  

data1 = pd.read_csv("Pori rautatieasema_ 1.9.2024 - 16.11.2024_cc88b7a9-511a-475b-8331-84eedd33d255.csv", usecols=[2,3])
data2 =  pd.read_csv("Pori rautatieasema_ 1.9.2024 - 16.11.2024_cc88b7a9-511a-475b-8331-84eedd33d255.csv", usecols=[5])


print(data1,data2)
AikaxPaiva = data1.apply(lambda row: '.'.join(map(str, row)), axis=1)
data1['AikaxPaiva'] = AikaxPaiva
data1 = data1['AikaxPaiva']
data1frame = pd.Series(data1,name='Dates').to_frame('Dates')

data3 = data1frame.join(data2)

print(data3)

data4 = pd.read_csv("Pori rautatieasema_ 1.9.2023 - 16.11.2023_12beb2ba-b8d4-439b-bb7f-af707b31453e.csv", usecols=[2,3])
data5 =  pd.read_csv("Pori rautatieasema_ 1.9.2023 - 16.11.2023_12beb2ba-b8d4-439b-bb7f-af707b31453e.csv", usecols=[5])


print(data4,data5)
AikaxPaiva = data4.apply(lambda row: '.'.join(map(str, row)), axis=1)
data4['AikaxPaiva'] = AikaxPaiva
data4 = data4['AikaxPaiva']
data4frame = pd.Series(data4,name='Dates').to_frame('Dates')

data6 = data4frame.join(data5)
print(data6)

x1 = data3['Dates']
x2 = data6['Dates']
y1 = data3['Lampotila']
y2 = data6['Lampotila']

plt.plot(x1,y1,label='2024',color='g')
plt.plot(x2,y2,label='2023',color='b')

plt.xticks(fontsize=8,rotation=90)
#plt.xticks(np.arange(0,1848,step=200))
plt.legend()
plt.show()

