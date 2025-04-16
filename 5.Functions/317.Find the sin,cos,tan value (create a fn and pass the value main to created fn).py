# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 22:59:46 2024

@author: Admin
"""

import math
def sin_cos_tan_val(y,x):
    z=y(x)
    return(z)
    
#main
x=int(input('Enter n value:'))
calculate1=sin_cos_tan_val(math.sin, x)
calculate2=sin_cos_tan_val(math.cos, x)
calculate3=sin_cos_tan_val(math.tan, x)

print('Given value of sin value is:',calculate1)
print('Given value of cos value is:',calculate2)
print('Given value of tan value is:',calculate3)