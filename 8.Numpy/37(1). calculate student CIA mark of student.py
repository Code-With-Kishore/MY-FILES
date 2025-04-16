# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 21:46:01 2025

@author: Admin
"""

import numpy as np

f1 = open("D:\\m1","r")
f2 = open("D:\\m2","r")
f3 = open("D:\\seminarfile","r")
f4 = open("D:\\attendencefile","r")

m1 = np.fromfile(f1,dtype=np.uint8)
m2 = np.fromfile(f2,dtype=np.uint8)
seminar = np.fromfile(f3,dtype=np.uint8)
attendence = np.fromfile(f4,dtype=np.uint8)

avg=(m1+m2)/2
cia=(avg*0.6)+(seminar*0.2)+(attendence*0.2)

print('Mark1: ',m1)
print('Mark2: ',m2)
print('Seminar: ',seminar)
print('Attendence: ',attendence)
print('Average of Mark1 and Mark2: ',avg)
print('Overall CIA Mark: ',cia)