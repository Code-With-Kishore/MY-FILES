# -*- coding: utf-8 -*-
"""
Created on Fri Apr 11 10:29:20 2025

@author: Admin
"""

import numpy as np
import matplotlib.pyplot as mp
import math

x=np.linspace(0,2,5)
y=[math.sin(j)for j in x]
mp.plot(x,y)
mp.show()