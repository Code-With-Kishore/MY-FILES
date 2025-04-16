# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 01:04:53 2024

@author: Admin
"""

a=[]
n=5
i=0
while i<n:
    b=int(input('Enter the b value:'))
    a.append(b)
    i=i+1


biggest=0
smallest=0
ln=len(a)
i=0
while i<=ln-1:
    if a[i]>biggest:
        biggest=a[i]
    elif a[i]<smallest:
        smallest=a[i]
    else:
        pass
    i=i+1

x=0
sb=0
i=0
while i<=ln-1:
    if biggest!=a[i]:
        if a[i]>sb:
            sb=a[i]
            x=i
        else:
            pass
    i=i+1

y=0
sm=0
i=0
while i<=ln-1:
    if smallest!=a[i]:
        if a[i]<sm:
            sm=a[i]
            y=i
        else:
            pass
    i=i+1
    a[x]=sm
    a[y]=sb
print(sb)
print(sm)

