# HOMEWORK01 for CS132SP_2025

import random
import time

# First smallest difference algorithm
def algoOne(rL):
    # Start Timer
    start = time.time()
    
    # Takes the first value and assigns it
    firstVal = rL[0]

    # Setting difference to 0
    difference = 0

    # Loops for each value after the first in the list
    for i in rL[1:]:
        # Takes the absolute value of the first value - the item in the loop
        temp_diff = abs(firstVal - i)
        # if the difference is 0 then there is no difference to then it is assigned the temp_diff value
        if difference == 0:
            difference = temp_diff
        # If the temp_diff is < than the difference then it is assigned the value of temp_diff
        elif temp_diff < difference:
            difference = temp_diff
    
    # End timer
    end = time.time()
    return end - start, difference

# Same as the algorithm above except this one is sorted before the loops begins
def algoTwo(rL):
    start = time.time()
    sorted(rL)
    firstVal = rL[0]
    difference = 0
    for i in rL[1:]:
        temp_diff = abs(firstVal - i)
        if difference == 0:
            difference = temp_diff
        elif temp_diff < difference:
            difference = temp_diff
    end = time.time()
    return end - start, difference

def main():
    # Start of program, prompting user for inputs
    print("This program finds the smallest difference between any two elements in a randomly generated list of integers, using two different algorithms with different Big-O efficiency.\n")
    minRange = int(input("Enter a random min range: "))
    maxRange = int(input("Enter a random max range: "))
    listLen = int(input("Enter length of list: "))

    # Initalizing randomList
    randomList = []

    # For loop that will append random numbers to randomList
    for i in range(listLen):
        randomNumber = random.randrange(minRange, maxRange+1)
        randomList.append(randomNumber)

    # Initializing variables to be returned from algoOne and algoTwo functions
    timeOne, diffOne = algoOne(randomList)
    timeTwo, diffTwo = algoTwo(randomList)

    # Simple check to see if the algorithms are both calculating the same thing
    if diffOne == diffTwo:
        print(f'Smallest difference: {diffOne}')
    else:
        print("Error calculating smallest difference.")

    # Checks to see if list length is greater that 100, if so then it will print the squeezed text option
    if listLen > 100:
        print(f'Squeezed text (lines).')
    else:
        print(f'List: {randomList}')
    print(f'List length: {listLen}')
    print(f'Algorithm 1 Time: {timeOne}')
    print(f'Algorithm 2 Time: {timeTwo}')
  
main()