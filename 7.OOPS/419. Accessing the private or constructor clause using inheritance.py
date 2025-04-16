# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 04:28:58 2024

@author: Admin
"""

from pgm417 import A2nos
class point(A2nos):
    def __init__(self, a=10, b=20):
        super().__init__(a,b)
        
        
#main
c=A2nos()
c.display()

c.setx(500)
c.display()

c.sety(100)
c.display()
 
c.setxy(100, 200)
c.display()

c.reset()
c.display()

d=A2nos()
c.setobject(d)

a=c.getx()
b=c.gety()
e=c.getxy()
print(a)
print(b)
print(e)

y=c.getobject()
y.display()