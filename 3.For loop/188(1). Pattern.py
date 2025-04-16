# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 07:52:23 2025

@author: Admin
"""

n=10
for i in range(n):
    if i%2==0:
        start='-'
        alter='*'
    else:
        start='*'
        alter='-'
        
    r=' '
    
    for j in range(i):
        if j%2==0:
            r=r+start
        else:
            r=r+alter
    print(r)
        
        