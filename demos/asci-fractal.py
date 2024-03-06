#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 07:13:31 2024

@author: abmosca
"""

# def fractal(width, height, count):
#     if count == 1:
#         for i in range(height):
#             print("-"*width + " "*width)
#     else:
#         for i in range(count):
#             fractal(width, height, 1)
#             fractal(width, height, 1)

#fractal(3, 3, 1)

width = 2
height = 2
count = 2
for i in range(count):
    for i in range(count):
        print("*"*width + " "*width, end="")
        print("*"*width + " "*width, end="")
        print("*"*width + " "*width, end="")
    print("\n")
