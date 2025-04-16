# -*- coding: utf-8 -*-
"""
Created on Sun Apr 13 18:09:48 2025

@author: Admin
"""

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('D:\STUDENT MARKS2.csv')

x = df['ROLL.NO']
y = df['TAMIL']

plt.plot(x, y, '^--g' , mec='red', mfc='yellow' )
plt.xlabel('Roll.No of Student')
plt.ylabel('Marks of Student')
plt.title('Tamil Subject Mark')
plt.show()