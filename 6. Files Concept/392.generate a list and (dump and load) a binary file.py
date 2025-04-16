# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 05:28:51 2024

@author: Admin
"""

import pickle
import random
n=int(input('Enter n value:'))
l=[random.randint(0,10000)for i in range(n)]
f=open('task','wb')
pickle.dump(l, f)

f=open('task', 'rb')
x=pickle.load(f)
print(x)
f.close()
