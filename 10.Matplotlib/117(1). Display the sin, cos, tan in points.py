# -*- coding: utf-8 -*-
"""
Created on Fri Apr 11 17:04:33 2025

@author: Admin
"""

import matplotlib.pyplot as mp
import math

n = 100

x = [2 * i for i in range(n)]

y = [math.sin(j) for j in x]
z = [math.cos(j) for j in x]
k = [math.tan(j) for j in x]

mp.plot(x, y)
mp.plot(x, z)
mp.plot(x, k)

mp.show()
