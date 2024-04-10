#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 12:11:22 2024

@author: abmosca
"""

from graphics import *

def main():
    width = 600
    height = 400
    win = GraphWin("Fish", width, height)
    
    # body is an oval
    p1 = Point(60, 80)
    p2 = Point(140, 120)
    body = Oval( p1, p2 )
    body.setFill("red")

    # tail is another oval
    p1 = Point(130, 70)
    p2 = Point(150, 130)
    tail = Oval( p1, p2 )
    tail.setFill( "black" )

    # eye
    center2 = Point(85, 95)
    eye = Circle(center2, 5)
    eye.setFill( "black" )
    
    # draw 
    body.draw( win )
    tail.draw( win )
    eye.draw( win )
    
if __name__ == "__main__":
    main()
    
    