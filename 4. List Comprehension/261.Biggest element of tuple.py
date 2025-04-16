# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 06:18:08 2024

@author: Admin
"""

a=(1,2,3,4,5,6,7,8,9,10)
b=0
for i in a:
    b=i if i>b else b
print(b)
    