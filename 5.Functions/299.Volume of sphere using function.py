# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 12:23:36 2024

@author: Admin
"""

def volume_of_sphere(r):
    v=4/3*22/7*r*r*r
    return v
#main
r=int(input('Enter the value of r:'))
v=volume_of_sphere(r)
print(v)
