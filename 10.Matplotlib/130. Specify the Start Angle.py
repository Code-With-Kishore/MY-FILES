# -*- coding: utf-8 -*-
"""
Created on Tue Apr 15 11:13:46 2025

@author: Admin
"""

import numpy as np
import matplotlib.pyplot as plt

x=np.random.randint(10, 50, 5)

l=['Tamil', 'English', 'Maths', 'Science', 'Social']

plt.pie(x, labels = l, startangle = 90)
plt.show()