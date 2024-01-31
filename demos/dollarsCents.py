#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ab Mosca
01.31.24

Sum input prices
"""

import math 

# Get input from user
price1 = eval(input("Enter a price "))
price2 = eval(input("Enter a price "))
price3 = eval(input("Enter a price "))

# Sum input prices
total = price1 + price2 + price3

# Print our formatted answer
dollars = math.floor(total)
cents = total - dollars
cents = round(cents,2)

print("Your total is", dollars,
      "dollars and", cents, "cents")

