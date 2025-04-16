# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 19:34:29 2025

@author: Admin
"""

import pandas as pd
d={'Name':['krish', 'venkat', 'albert', 'john', 'hari'],
   'Age':[22, 23, 24, 25, 22],
   'Qualification':['M.sc', 'MCA', 'BE', 'B.tech', 'Bio'], 
   'Gender':['male', 'male', 'male', 'male', 'male'],
   'Location':['trichy', 'karur', 'salem', 'madurai', 'chennai']}
x=pd.DataFrame(d)
print(x)