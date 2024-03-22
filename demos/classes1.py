#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Classes Pt1 Notes
03/18/24

Ab Mosca
"""

import random 

class Playlist:
    
    def __init__(self):
        self.songs = []
        
    # ADD
    def add(self, song):
        self.songs.append(song)
    
    # PRINT
    def printSongs(self):
        for song in self.songs:
            print("Title:", song["title"],
                  "Artist:", song["artist"],
                  "Album:", song["album"])
            
# Radio 
class Radio(Playlist):
    
    def __init__(self, lib):
        numSongs = len(lib) - 1
        # randomly choose 10 songls from library 
        songs = []
        for i in range(0, 10):
            index = random.randint(0, numSongs)
            song = lib[index]
            songs.append(song)
        self.songs = songs
    
def main():
    myPlaylist = Playlist()
    hbd = {"title": "Happy Birthday",
           "artist": "unknown",
           "album": "Birthday"}
    myPlaylist.add(hbd)
    myPlaylist.printSongs()
    
    # make a library of 100 
    # pretend songs 
    library = []
    for i in range(0, 100):
        newSong = {
            "title": "title_"+str(i),
            "artist": "artist_"+str(i),
            "album": "album_"+str(i)
            }
        library.append(newSong)
    
if __name__ == "__main__":
    main() 

