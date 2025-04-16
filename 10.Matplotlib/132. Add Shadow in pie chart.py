# -*- coding: utf-8 -*-
"""
Created on Tue Apr 15 11:18:47 2025

@author: Admin
"""

import numpy as np
import matplotlib.pyplot as plt

x=np.random.randint(10, 50, 5)

l=['Tamil', 'English', 'Maths', 'Science', 'Social']
e=[0.1,0,0.1,0,0]

plt.pie(x, labels = l, explode=e, shadow=True)
plt.show()