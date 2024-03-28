#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 11:26:19 2024

Ab Mosca

Graphics Notes
"""

from graphics import *

def main():
    win = GraphWin("Practice", 500, 500)
    c = Circle(Point(250, 250), 100)
    c.setFill("red")
    c.draw(win)
    win.getMouse()
    win.close()
    
if __name__ == "__main__":
    main()

