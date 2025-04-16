# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 10:12:28 2024

@author: Admin
"""

c=d=0
a=1
while a<=10:
    b=int(input('Enter b:'))
    if b>c:
        c=b
    elif b<d:
        d=b
    else:
        print('not')
        a=a+1
    print(c)
    print(d)