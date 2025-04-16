# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 04:58:43 2024

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
print(a)

x=y=z=0
for i in a:
    if i>=0 and i<=9:
        x=x+1
    elif i>=10 and i<=99:
        y=y+1
    elif i>=100 and i<=999:
        z=z+1
    else:
        pass
print('Single digit count:', x)
print('Two digit count:',y)
print('Three digit count:',z)
f.close()

