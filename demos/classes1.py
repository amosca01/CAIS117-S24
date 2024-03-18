#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Classes Pt1 Notes
03/18/24

Ab Mosca
"""

class Playlist:
    
    def __init__(self):
        self.songs = []
        
    # ADD
    def add(self, song):
        self.songs.append(song)
    
    # REMOVE
    
    # PRINT
    
    # SEARCH 
    
def main():
    myPlaylist = Playlist()
    hbd = {"title": "Happy Birthday",
           "artist": "unknown",
           "album": "Birthday"}
    myPlaylist.add(hbd)
    
    
if __name__ == "__main__":
    main() 

