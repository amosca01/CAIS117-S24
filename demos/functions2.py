"""
Ab Mosca
02.16.24

Functions day 2 class notes 

"""

# # return vs print 
# def printStr():
#     print("This function reutnrs nothing! ")
    
# r = printStr()
# print(r)

# def returnStr():
#     return "This function has a return"

# r = returnStr()
# print(r)

def addOne(x):
    return x + 1 

def doubleIt(x):
    return 2*x

def printWithStars(x):
    toPrint = "*"*x
    print(toPrint)
    
def woohoo():
    print("WOO HOO!")
    printWithStars(addOne(doubleIt(2)))

woohoo()

















