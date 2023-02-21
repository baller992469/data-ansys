# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 16:28:47 2020

@author: Liu Yu

通过卷积确定两组相关信号的时间差
"""

import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
import pandas as pd
'''
t = np.linspace(0,127,128)*0.02
f = 1.0
s1 = np.sin(2*3.14*f*t)
s2 = np.sin(2*3.14*f*(t-0.35))
'''
#df = pd.read_csv("data/survey_2013.txt",skiprows=7)
plt.rcParams['font.sans-serif'] = ['SimHei']   #显示中文
plt.rcParams['axes.unicode_minus']=False       #显示负号
Fs=2560 #采样频率
file = 'DA015#18.TXT'    #第一列为数据y
#file = 'dandiaolan3#8.TXT'    #第一列为数据y
file2 = 'DA014#18out.TXT'    #第一列为数据y
#file3 = 'dandiaolan3#18.TXT' 
s1 = np.loadtxt(file,skiprows=3)
s2 = np.loadtxt(file2,skiprows=3)
#s3 = np.loadtxt(file3,skiprows=3)
t=np.arange(0,len(s1)/Fs,1/Fs) # 根据采样频率生成时间数据

s1=s1[0:min(len(s1),len(s2))]
s2=s2[0:min(len(s1),len(s2))]
#s3=s3[0:min(len(s1),len(s3))]
t=t[0:min(len(s1),len(s2))]

plt.plot(t,s1,label='data1')
plt.plot(t,s2,label='data2')
#plt.plot(t,s3,label='data3')
plt.legend()
plt.show()
corr = signal.correlate(s1, s2, mode='full')
tx = np.append(np.sort(-t), np.delete(t, 0));
plt.figure
plt.plot(tx,corr,label='co互相关函数')
index_dt=np.argmax(corr)   #根据互相关函数得到的两曲线的时间差
plt.legend()
plt.show()
print("两曲线的时间相位（相同峰值的时差）为%8.5fs"%(tx[index_dt]))
#return tx[index_dt]
'''
import numpy as np
import matplotlib.pyplot as plt

x=np.arange(0,2*np.pi,0.01)
y=np.sin(x)

plt.plot(x,y)
plt.show()
'''