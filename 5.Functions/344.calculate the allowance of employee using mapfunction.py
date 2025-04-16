# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 10:40:44 2024

@author: Admin
"""
n=int(input('Enter n value:'))
basicpay=[int(input('Enter basicpay value:'))for i in range(n)]
def allowance(basicpay):
    x=basicpay*0.08
    y=basicpay*0.05
    total=x+y
    return total
#main
x=map(allowance,basicpay)
y=list(x)
print(y)

    