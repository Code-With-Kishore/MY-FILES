# -*- coding: utf-8 -*-
"""
Created on Fri Apr 11 11:44:36 2025

@author: Admin
"""

import matplotlib.pyplot as mp
def expression(x):
    return 4*(x**2)+2

x=[i for i in range(-10,10)]
y=[expression(j) for j in x]

mp.plot(x,y)
mp.show()
