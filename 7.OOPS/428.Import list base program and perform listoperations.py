# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 01:00:08 2025

@author: Admin
"""

from pgm427 import my_list  

class listopr(my_list):
    def __init__(self, x):
        super().__init__(x)  

    def add(self, x):
        a=0
        for i in self._x:
            a=a+i
        return a

    def big(self):
        return max(self._x)

    def small(self):
        return min(self._x)

    def sin_two_thre(self):
        d = [i for i in self._x if i >= 0 and i <= 9]      
        e = [i for i in self._x if i >=10 and i <= 99]    
        f = [i for i in self._x if i >=99 and i<= 999]  
        return d, e, f

    def biggest_index(self):
        i = max(self._x)
        max_index = self._x.index(i)  
        return max_index

    def smallest_index(self):
        j = min(self._x)
        min_index = self._x.index(j) 
        return min_index

    def count(self):
        return len(self._x)

    def display(self):
        print(self._x)  

# Main

z = listopr(10)
z.display()

ad = z.add(0)
print("sum of all element in list:", ad)


b = z.big()
print("Biggest element:", b)


s = z.small()
print("Smallest element:", s)


t = z.sin_two_thre()
print("Single, two, three-digit numbers:", t)


bi = z.biggest_index()
print("Biggest element index:", bi)


si = z.smallest_index()
print("smallest element index:", si)


c = z.count()
print("Number of elements in the list:", c)
