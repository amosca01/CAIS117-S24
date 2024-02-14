"""
Ab Mosca
02.14.24

Function day 1 class notes 

"""

# Define a function that returns 
# "Happy Birthday to you"
def oneLine():
    return "Happy Birthday to you"

# Challenge: 
# Define a function that takes in an int
# And prints "Happy Birthday to you" 
# on separate lines that many times 

def happyBirthday(name = "Ab"):
    print(oneLine())
    print(oneLine())
    print("Happy Birthday dear " + name)
    print(oneLine())
    
# Let's sing happy birthday
userName = input("Type your name ")
happyBirthday(userName)

