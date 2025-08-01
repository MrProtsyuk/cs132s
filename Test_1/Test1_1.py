# TEST1_1 for CS132SP_2025

import random 

# Checks for repetition within the list
def repetitionCheck(randomList):
    # Sorts list so that the smallest value will be first
    randomList.sort()
    firstVal = randomList[0]

    for i in randomList[1:]:
        # if the first value - i is == 0 then that means they are the same
        # returns right away saying that it has repeated elements
        temp_diff = firstVal - i
        if temp_diff == 0:
            return f"{randomList} has repeated elements."

    # if it goes through the list and none are the same then it returns this  
    return f"{randomList} has no repeated elements"

# Creates random list using user inputs
def createList(minRange, maxRange, listLength):
    ranList = []
    for i in range(listLength):
        randomNum = random.randrange(minRange, maxRange+1)
        ranList.append(randomNum)
    
    return ranList

# Main function, asks for user inputs
def main():
    # Print statement given in test criteria
    print("""This program finds (the more efficiently, the more credit)
whether or not a random list has any repeated elements.\n""")
    
    # User inputs
    minRange = int(input("Enter random minrange: "))
    maxRange = int(input("Enter random maxrange: "))
    listLength = int(input("Enter length of list: "))

    # Calls the create list function
    randomList = createList(minRange, maxRange, listLength)

    # Calls the repetition check function
    deliverable = repetitionCheck(randomList)

    # Prints final output
    print(deliverable)
main()