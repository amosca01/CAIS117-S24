#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
04.17.24
Ab Mosca

File to demo reading txt files 
"""

def main():
    # open my file for reading 
    file = open("text.txt", "r")
    
    # read the file, and print contents
    text = file.readlines()
    print(text)
    
    # close my file
    file.close()
    
if __name__ == "__main__":
    main()

