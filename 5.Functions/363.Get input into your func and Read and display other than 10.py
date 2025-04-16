# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 04:31:35 2024

@author: Admin
"""

def read_and_display():
    n=int(input('Enter n value:'))
    return n

#main
i=read_and_display()
while i!=10:
    print(i)
    i=int(input('Enter the value:'))
    