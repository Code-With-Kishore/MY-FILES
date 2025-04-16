# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 05:52:16 2024

@author: Admin
"""

n=int(input('enter n:'))
basicpay=[int(input('Enter basicpay value:'))for i in range(n)]
def detection(basicpay):
    x=basicpay*0.05
    y=basicpay*0.03
    total=x+y
    return total
#main

x=map(detection,basicpay)
y=list(x)
print(y)