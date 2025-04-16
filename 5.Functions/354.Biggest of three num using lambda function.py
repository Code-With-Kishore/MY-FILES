# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 05:42:00 2024

@author: Admin
"""

x=lambda a,b,c: (a if a>c else c) if a>b else (b if b>c else c)
a=int(input('Enter a value:'))
b=int(input('Enter b value:'))
c=int(input('Enter c value:'))
y=x(a,b,c)
print(y)