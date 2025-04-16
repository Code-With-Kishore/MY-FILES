# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 06:21:27 2025

@author: Admin
"""

from pgm426 import A3nos

class Op3nos(A3nos):
    def __init__(self, x=10, y=20, z=30):
        super().__init__(x, y, z)

    def summ(self):
        return self.getx() + self.gety() + self.getz()

    def difference(self):
        return self.getx() - self.gety() - self.getz()

    def product(self):
        return self.getx() * self.gety() * self.getz()

    def mod(self):
        return self.getx() % self.gety() % self.getz()

    def big(self):
        x, y, z = self.getx(), self.gety(), self.getz()
        return max(x, y, z)

    def small(self):
        x, y, z = self.getx(), self.gety(), self.getz()
        return min(x, y, z)

    def display(self):
        print(self.getx(), self.gety(), self.getz())


# Main
d = Op3nos()
d.display()

ad = d.summ()
su = d.difference()
p = d.product()
m = d.mod()
b = d.big()
s = d.small()

print(ad)
print(su)
print(p)
print(m)
print(b)
print(s)
