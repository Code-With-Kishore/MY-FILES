# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 05:06:40 2024

@author: Admin
"""

from pgm417 import A2nos
class point(A2nos):
    pass

#main
c=point()
c.display()

c.setx(500)
c.display()

c.sety(100)
c.display()
 
c.setxy(100, 200)
c.display()

c.reset()
c.display()

d=point()
c.setobject(d)

a=c.getx()
b=c.gety()
e=c.getxy()
print(a)
print(b)
print(e)

y=c.getobject()
y.display()
