# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 05:35:27 2024

@author: Admin
"""

import random
n=int(input('Enter n numbers:'))
x=[random.randint(1,100)for i in range(n)]
def find_true(num):
    if num%2==0:
        return True
    else:
        return False
    
#main
a=filter(find_true,x)
b=list(a)
print(b)
        