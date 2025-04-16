# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 07:16:57 2024

@author: Admin
"""
import random
n=int(input('Enter n value:'))
x=[random.randint(1,10000)for i in range(n)]
def single(num):
    if num>=0 and num<=9:
        return True
    else:
        return False
def two(num):
    if num>=10 and num<=99:
        return True
    else:
        return False
def three(num):
    if num>=100 and num<=999:
        return True
    else:
        return False
def four(num):
    if num>=1000 and num<=9999:
        return True
    else:
        return False
    
a=filter(single,x)
b=filter(two,x)
c=filter(three,x)
d=filter(four,x)

print(list(a))
print(list(b)) 
print(list(c))
print(list(d))   