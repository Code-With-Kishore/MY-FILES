# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 23:14:45 2024

@author: Admin
"""
#find the second biggest element in list.
a=[]
n=5
i=0
while i<=n:
    b=int(input('Enter the b value:'))
    a.append(b)
    i=i+1


biggest=0
ln=len(a)
i=0
while i<=ln-1:
    if a[i]>biggest:
        biggest=a[i]
    else:
        pass
    i=i+1

    
sb=0
i=0
while i<=ln-1:
    if biggest!=a[i]:
        if a[i]>sb:
            sb=a[i]
        else:
            pass
    i=i+1
print(sb)