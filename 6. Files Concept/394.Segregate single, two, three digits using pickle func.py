# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 06:06:43 2024

@author: Admin
"""

import pickle
import random
n=int(input('Enter n value:'))
l=[random.randint(0,1000)for i in range(n)]
f=open('task','wb')
pickle.dump(l, f)

f=open('task', 'rb')
a=pickle.load(f)

x=[i for i in a if i>=0 and i<=9 ]
y=[i for i in a if i>=10 and i<=99]
z=[i for i in a if i>=100 and i<=999]

print('Original list:',a)
print('single digit:',x)
print('two digit:',y)
print('three digit:',z)
