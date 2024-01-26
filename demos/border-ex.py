# -*- coding: utf-8 -*-
"""
Ab Mosca

01.26.24

Program to print a banner around CAIS117 
"""

# Modify this to print a banner around ANY word 


word = input("Enter any text ")
border_word = "# " + word + " #"
hash_len = len(border_word)

hash_border = "#"*hash_len

print(hash_border)
print(border_word)
print(hash_border)


