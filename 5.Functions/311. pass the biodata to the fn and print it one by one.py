# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 06:04:15 2024

@author: Admin
"""

def Biodata(**x):
    for i in x:
        print(i, x[i])

#main
Biodata(Name='kishore', Age=23, Gender='male', Qualification='m.sc', Contact=8608649691, Location='trichy')
