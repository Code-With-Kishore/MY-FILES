# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 21:26:00 2025

@author: Admin
"""

class person():
    _Name=None
    _Age=None
    _Location=None
    _Pincode=None
    
    def __init__(self, Name='krish', Age=22, Location='Trichy', Pincode=620003):
        self._Name=Name
        self._Age=Age
        self._Location=Location
        self._Pincode=Pincode
        
    def setname(self, Name):
        self._Name=Name
        
    def setage(self, Age):
        self._Age=Age
        
    def setlocation(self, Location):
        self._Location=Location
        
    def setpincode(self, Pincode):
        self._Pincode=Pincode
        
    def setall(self, Name, Age, Location, Pincode):
        self._Name=Name
        self._Age=Age
        self._Location=Location
        self._Pincode=Pincode
        
    def reset(self):
        self._Name='kishore'
        self._Age=24
        self._Location='tiruchirappalli'
        self._Pincode=620003
        
    def setobject(self, a):
        self._Name=a._Name
        self._Age=a._Age
        self._Location=a._Location
        self._Pincode=a._Pincode
        
    def getname(self):
        return self._Name
    def getage(self):
        return self._Age
    def getlocation(self):
        return self._Location
    def getpincode(self):
        return self._Pincode
    def getall(self):
        return self._Name, self._Age, self._Location, self._Pincode
    def getobject(self):
        return self
    def display(self):
        print(self._Name, self._Age, self._Location, self._Pincode)
        
#main
#c=person()
#c.display()

#c.setname('venkat')
#c.display()

#c.setage(25)
#c.display()

#c.setlocation('chennai')
#c.display()

#c.setpincode(600023)
#c.display()
 
#c.setall('kumar', 30, 'kerala', 12456)
#c.display()

#c.reset()
#c.display()

#d=person()
#c.setobject(d)

#a=c.getname()
#b=c.getage()
#e=c.getlocation()
#f=c.getpincode()
#d=c.getall()
#print(a)
#print(b)
#print(e)
#print(f)
#print(d)

#y=c.getobject()
#y.display()
