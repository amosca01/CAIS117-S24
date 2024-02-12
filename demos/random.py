#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ab Mosca
02.12.24

Class notes for Random Module
"""

import random

# num = random.random()

# if num <= 0.50:
#     print("HEADS")
# else:
#     print("TAILS")

# random.seed(1)
# num = random.random()
# print(num)

num = random.random()
if num <= 0.5:
    print(1)
else: 
    num = random.randint(2,6)
    print(num)



