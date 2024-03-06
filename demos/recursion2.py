#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Recursion day 2 class notes

Ab Mosca 
03/06/24
"""

# recursive function for computing 
#   the sum of a list of numbers
def recursiveSum(lst):
    # base case
    if len(lst) == 1:
        return lst[0]
    # recursive step 
    else:
        return lst[0] + recursiveSum(lst[1:])
    
total = recursiveSum(range(0, 5))
print(total)
