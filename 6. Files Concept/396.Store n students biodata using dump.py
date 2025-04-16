# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 04:18:19 2024

@author: Admin
"""

import pickle
f=open('biodata','wb')
n=int(input('Enter n value:'))
for i in range(n):
    a=input('Enter name:')
    b=int(input('Enter age:'))
    c=input('Enter qualification:')
    d=input('Enter location:')
    x=[a,b,c,d]
    pickle.dump(x, f)
f.close()

