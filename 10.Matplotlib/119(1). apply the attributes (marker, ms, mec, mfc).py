# -*- coding: utf-8 -*-
"""
Created on Sun Apr 13 17:14:00 2025

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

mp.subplot(3, 2, 1)
mp.plot(x, y1, marker='o', ms=5, mec='red', mfc='yellow')

mp.subplot(3, 2, 2)
mp.plot(x, y2, marker='s', ms=5, mec='blue', mfc='green')

mp.subplot(3, 2, 3)
mp.plot(x, y3, marker='^', ms=5, mec='purple', mfc='orange')

mp.subplot(3, 2, 4)
mp.plot(x, y4, marker='D', ms=5, mec='black', mfc='pink')

mp.subplot(3, 2, 5)
mp.plot(x, y5, marker='*', ms=8, mec='brown', mfc='cyan')

mp.show()

