# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 21:42:53 2024

@author: Admin
"""

import pickle
a=input('Enter name:')
b=int(input('Enter age:'))
c=input('Enter qualification:')
d=input('Enter location:')
x=[a,b,c,d]

f=open('biodata','wb')
pickle.dump(x, f)
f.close()

f1=open('biodata','rb')
y=pickle.load(f1)
print(y)
f.close()