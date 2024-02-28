#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ab Mosca
02.28.24

Dictionary class notes 
"""

def main(): 
    # friends = []
    # newFriend = input("Enter a friend or DONE: ")
    
    # while (newFriend != "DONE"):
    #     friends.append(newFriend)
    #     friends.sort()
    #     print(friends)
    #     newFriend = input("Enter a friend or DONE: ")
    
    # c = {"Ab":"Ab's number", "Sarah":"Sarah's number"}
    # for key, value in c.items():
    #     print(key, value)
    
    instructions = input("ADD or DONE? ")
    contacts = {}
    
    while (instructions != "DONE"):
        name = input("Name ")
        number = input("Number ")
        address = input ("Address ")
        
        contacts[name] = [number, address]
        instructions = input("ADD or DONE ")
        
    for name, info in contacts.items():
        print(name+"'s number is", info[0], "and they live at", info[1])
    
if __name__ == "__main__":
    main()

