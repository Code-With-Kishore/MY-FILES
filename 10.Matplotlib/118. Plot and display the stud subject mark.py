# -*- coding: utf-8 -*-
"""
Created on Sat Apr 12 11:25:59 2025

@author: Admin
"""

import matplotlib.pyplot as mp
import pandas as pd

df = pd.read_csv('D:\STUDENT MARKS2.csv')

x = df['ROLL.NO']
y1 = df['TAMIL']

mp.plot(x, y1)

mp.show()
