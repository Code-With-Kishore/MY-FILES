# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 05:27:46 2024

@author: Admin
"""


from pgm417 import A2nos

class Op2nos(A2nos):
    def __init__(self, x=10, y=20):
        super().__init__(x, y)

    def sum(self):
        x = self.getx()
        y = self.gety()
        add = x + y
        return add

    def difference(self):
        x = self.getx()
        y = self.gety()
        sub = x - y
        return sub

    def product(self):
        x = self.getx()
        y = self.gety()
        mul = x * y
        return mul

    def mod(self):
        x = self.getx()
        y = self.gety()
        m= x / y
        return m

    def quotient(self):
        x = self.getx()
        y = self.gety()
        q= x // y
        return q

    def biggest(self):
        x = self.getx()
        y = self.gety()
        b = x if x > y else y
        return b

    def smallest(self):
        x = self.getx()
        y = self.gety()
        sm = x if x < y else y
        return sm


c = Op2nos()
c.display()

print(c.sum())
print(c.difference())
print(c.product())
print(c.mod())
print(c.quotient())
print(c.biggest())
print(c.smallest())
