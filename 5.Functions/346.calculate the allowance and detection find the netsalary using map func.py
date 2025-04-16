# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 22:58:40 2024

@author: Admin
"""

n=int(input('Enter the employee:'))
basicpay=[int(input('Enter basicpay:'))for i in range(n)]
def allowance(basicpay):
    x=basicpay*0.08
    y=basicpay*0.05
    total=x+y
    return total
def detection(basicpay):
    x=basicpay*0.04
    y=basicpay*0.03
    total=x+y
    return total

a=map(allowance,basicpay)
b=map(detection,basicpay)
x=list(a)
y=list(b)
calculate=[x[i]+y[i] for i in range(n)]
net_salary=[basicpay[i]-calculate[i]for i in range(n)]
print('allowance',x)
print('detection',y)
print('calculate allowance and detection',calculate)
print('Net_salary',net_salary)
