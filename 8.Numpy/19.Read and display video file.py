# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 06:18:14 2025

@author: Admin
"""

import numpy as np
f=open('C:\power bi\WhatsApp Video 2025-02-15 at 6.27.28 AM.mp4','rb')
x=np.fromfile(f, dtype='uint8')
print(x)
f.close()