# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 12:27:10 2024

@author: Admin
"""

def area_of_circle(r):
    c=22/7*r*r
    return c
    
#main
r=int(input('Enter radius value:'))
c=area_of_circle(r)
print(c)