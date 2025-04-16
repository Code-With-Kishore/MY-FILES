# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 06:31:21 2025

@author: Admin
"""

from pgm433 import person

class staff(person):
    _Accno = None
    _Dept = None
    _Salary = None

    def __init__(self, Name='krish',Age=23, Location='Trichy', Pincode=620003, Accno=12345678910, Dept='MSc', Salary=15000):
        super().__init__(Name, Age, Location, Pincode)
        self._Accno = Accno
        self._Dept = Dept
        self._salary = Salary

    def setaccno(self, Accno):
        self._Accno = Accno
        
    def setdept(self, Dept):
        self._Dept = Dept
        
    def setsal(self, Salary):
        self._Salary = Salary

    def setall(self, Name, Age, Location, Pincode, Accno, Dept, Salary):
        self._Name = Name
        self._Age = Age
        self._Location = Location
        self._Pincode = Pincode
        self._Accno = Accno
        self._Dept = Dept
        self._Salary = Salary

    def reset(self):
        super().reset()
        self._Accno = 1020304050
        self._Dept = "MCA"
        self._Salary = 200000

    def setobject(self, d):
        super().setobject(d)
        self._Accno = d._Accno
        self._Dept = d._Dept
        self._Salary = d._Salary  

    def getaccno(self):
        return self._Accno
    
    def getdept(self):
        return self._Dept
    
    def getsal(self):
        return self._Salary

    def getall(self):
        return self._Name, self._Age, self._Location, self._Pincode, self._Accno, self._Dept, self._Salary  

    def getobject(self):
        return self

    def display(self):
        super().display()
        print(self._Accno, self._Dept, self._Salary)


# Main
c = staff()
c.display()

c.setaccno(12345678910)
c.display()

c.setdept('MBA')
c.display()

c.setsal(500000)
c.display()

c.setall('Karnan', 24, 'Trichy', 620003, 102030405060708090100, 'M.phil', 500000)
c.display()

c.reset()
c.display()

d = staff()
c.setobject(d)

f = c.getobject()
f.display()

a = c.getaccno()
b = c.getdept()
z = c.getsal()
xyz = c.getall()
print(a)
print(b)
print(xyz)
print(z)