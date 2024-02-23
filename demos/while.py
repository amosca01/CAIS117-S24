# -*- coding: utf-8 -*-
"""
Ab Mosca
02.23.24

While loop class notes
"""

# # while loop with counter
# x = 16 
# while (x <= 26):
#     print(x)
#     x += 1

# # collecting user input
# phrase = input("Input a phrase or STOP: ")
# phrase = phrase.upper()

# while (phrase != "STOP"):
#     print(phrase)
#     phrase = input("Input a phrase or STOP: ")
#     phrase = phrase.upper()

# # memory game
# stillPlaying = 1
# animals = []


# while stillPlaying:
#     newAnimal = input("Input a new animal ")
#     if newAnimal in animals:
#         print("You lose!")
#         stillPlaying = 0 
#     else:
#         animals.append(newAnimal)

# memory game
animals = []
newAnimal = input("Input a new animal ")
ind = newAnimal in animals

while (ind == False):
    animals.append(newAnimal)
    newAnimal = input("Input a new animal ")
    ind = newAnimal in animals
    
print("you lose!")
    

    



















 
    



