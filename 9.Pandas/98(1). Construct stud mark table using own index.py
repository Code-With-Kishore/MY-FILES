# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 19:14:12 2025

@author: Admin
"""

import pandas as pd
import numpy as np

s=np.random.randint(50,100,(20,5), dtype=np.uint8)
rollnum=[225214201+i for i in range(20)]
subject=['Tamil', 'Englist', 'Maths', 'Science', 'Social']
x=pd.DataFrame(s, index=rollnum, columns=subject)
print(x)

