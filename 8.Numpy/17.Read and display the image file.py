# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 05:02:15 2025

@author: Admin
"""

import numpy as np
f=open('C:\power bi\grp.png', 'rb')
x=np.fromfile(f, dtype='uint8')
f.close()
print(x)