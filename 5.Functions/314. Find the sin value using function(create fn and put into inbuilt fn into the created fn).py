# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 05:29:03 2024

@author: Admin
"""
import math
def calculate_sinvalue(x):
    y=math.sin(x)
    return(y)
#main
x=int(input('Enter int value:'))
sin_value=calculate_sinvalue(x)
print(sin_value)