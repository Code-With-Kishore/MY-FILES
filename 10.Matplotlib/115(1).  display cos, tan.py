# -*- coding: utf-8 -*-
"""
Created on Fri Apr 11 11:29:28 2025

@author: Admin
"""
import numpy as np
import matplotlib.pyplot as plt
import math

x = np.linspace(0,2,5) 

cos_y = [math.cos(val) for val in x]
tan_y = [math.tan(val) for val in x]

plt.plot(x,cos_y)
plt.plot(x,tan_y)

plt.show()
