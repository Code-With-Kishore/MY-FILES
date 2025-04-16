# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 05:51:01 2024

@author: Admin
"""

def get():
    n=int(input('Enter value:'))
    return n

def one(x):
    print('one')
def two(x):
    print('two')
def three(x):
    print('three')
def four(x):
    print('four')
def five(x):
    print('five')
    
#main
x=get()
while x!=6:
    if x==1:
        one(x)
    elif x==2:
        two(x)
    elif x==3:
        three(x)
    elif x==4:
        four(x)
    elif x==5:
        five(x)
    else:
        pass
    x=get()
    
    