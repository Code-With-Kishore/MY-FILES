# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 14:28:16 2025

@author: Admin
"""
import numpy as np
f=open('C:\\aboutpy.txt', 'rb')
x=np.fromfile(f, dtype='uint8')

a=b=c=d=0

for i in x:
    print(chr(i), end='')
    
    if i>=65 and i<=90:
        a=a+1
    elif i>=97 and i<=122:
        b=b+1
    elif i>=0 and i<=9:
        c=c+1
    else:
        d=d+1

print('upper :',a)
print('lower :',b)
print('digits :',c)
print('special character :',d)
