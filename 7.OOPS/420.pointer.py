# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 21:46:16 2024

@author: Admin
"""

from pgm417 import A2nos

class point(A2nos):    
    def __init__(self, x=5, y=10):
        super().__init__(x, y)
    
    def move_right(self, dx):
        cur_x = self.getx()
        right = cur_x + dx
        self.setx(right)
    
    def move_left(self, dx):
        cur_x = self.getx()
        left = cur_x - dx
        self.setx(left)
        
    def move_up(self, dy):
        cur_y = self.gety()
        up = cur_y + dy
        self.sety(up)
        
    def move_down(self, dy):
        cur_y = self.gety()
        down = cur_y - dy
        self.sety(down)
        
    def move_random(self, dx, dy):
        curx = self.getx()  
        cury = self.gety()  
        
        random_x = curx + dx
        random_y = cury + dy     
        
        self.setx(random_x)
        self.sety(random_y)
        
    def display(self):
        print(self.getx(), self.gety())
        
# Main
c = point()
c.display()

c.move_right(10)
c.display()

c.move_left(20)
c.display()

c.move_up(30)
c.display()

c.move_down(40)
c.display()

c.move_random(50, 60)
c.display()
