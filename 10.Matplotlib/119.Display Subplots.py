# -*- coding: utf-8 -*-
"""
Created on Sun Apr 13 16:57:58 2025

@author: Admin
"""

import matplotlib.pyplot as mp
import pandas as pd

df = pd.read_csv('D:\STUDENT MARKS2.csv')

x = df['ROLL.NO']
y1 = df['TAMIL']
y2 = df['ENGLISH']
y3 = df['MATHS']
y4 = df['SCIENCE']
y5 = df['SOCIAL']

mp.subplot(2, 3, 1) # 3 Rows * 2 Cols
mp.plot(x, y1)

mp.subplot(2, 3, 2)
mp.plot(x, y2)

mp.subplot(2, 3, 3)
mp.plot(x, y3)

mp.subplot(2, 3, 4)
mp.plot(x, y4)

mp.subplot(2, 3, 5)
mp.plot(x, y5)


mp.show()
