# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 05:47:50 2025

@author: Admin
"""

import numpy as np
f=open('C:\power bi\Hey Minnale.mp3','rb')
x=np.fromfile(f, dtype='uint8')
print(x)
f.close()