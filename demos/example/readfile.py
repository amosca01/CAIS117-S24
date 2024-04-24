#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
04.17.2024
Ab Mosca

Read horizontal.txt into 
vertical.txt
"""
def main():
    # open 
    file = open("horizontal.txt", "r")
    
    # read 
    content = file.read().replace("\n", "")
    
    # close
    file.close()
    
    # split up my text around spaces 
    split_content = content.split(" ")
    
    # open file for writing
    w_file = open("vertical.txt", "w")
    
    # write to file 
    for word in split_content:
        w_file.write(word + "\n")
    
    # close 
    w_file.close()
    
if __name__ == "__main__":
    main()

