# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 04:55:00 2025

@author: Admin
"""

from pgm433 import person

class student(person):
    _RollNum = None
    _Dept = None
    _Year = None
    _Marks = None

    def __init__(self, Name='krish',Age=23, Location='Trichy', Pincode=620003, RollNum=12345678910, Dept='MSc', Marks=100):
        super().__init__(Name, Age, Location, Pincode)
        self._RollNum = RollNum
        self._Dept = Dept
        self._Marks = Marks

    def setrollnum(self, RollNum):
        self._RollNUm = RollNum
        
    def setdept(self, Dept):
        self._Dept = Dept
        
    def setmarks(self, Marks):
        self._Marks = Marks

    def setall(self, Name, Age, Location, Pincode, RollNum, Dept, Marks):
        self._Name = Name
        self._Age = Age
        self._Location = Location
        self._Pincode = Pincode
        self._RollNum = RollNum
        self._Dept = Dept
        self._Marks = Marks

    def reset(self):
        super().reset()
        self._RollNum = 51015
        self._Dept = "MCA"
        self._Marks = 70

    def setobject(self, d):
        super().setobject(d)
        self._RollNum = d._RollNum
        self._Dept = d._Dept
        self._Marks = d._Marks  

    def getrollnum(self):
        return self._RollNum
    
    def getdept(self):
        return self._Dept
    
    def getmarks(self):
        return self._Marks

    def getall(self):
        return self._Name, self._Age, self._Location, self._Pincode, self._RollNum, self._Dept, self._Marks  

    def getobject(self):
        return self

    def display(self):
        super().display()
        print(self._RollNum, self._Dept, self._Marks)


# Main
c = student()
c.display()

c.setrollnum(123456)
c.display()

c.setdept('MBA')
c.display()

c.setmarks(90)
c.display()

c.setall('Karnan', 24, 'Trichy', 620003, 654321, 'M.phil', 95)
c.display()

c.reset()
c.display()

d = student()
c.setobject(d)

f = c.getobject()
f.display()

a = c.getrollnum()
b = c.getdept()
z = c.getmarks()
xyz = c.getall()
print(a)
print(b)
print(xyz)
print(z)