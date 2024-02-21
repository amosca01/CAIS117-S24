#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ab Mosca
02.20.2024

Main function and importing notes 
"""

import salutations
import friday 

def talkToUser(start):
    if start:
        print("Welcome to my program! ")
        salutations.hello()
    else:
        salutations.goodbye()
    
def main():
     talkToUser(0)
    
if __name__ == "__main__":
     main()
    

