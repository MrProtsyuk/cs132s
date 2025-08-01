# HOMEWORK05 for CS132SP_2025

# This program efficiently computes the minimum total number of character 
# operations required to transform one string into another.
# The explaination for the code below is provided in the main function.
def store(string1, string2):
    if len(string1) == 0:
        return len(string2)
    elif len(string2) == 0:
        return len(string1)
    elif string1[-1] == string2[-1]:
        return store(string1[0:-1], string2[0:-1])
    else:
        return 1+min(store(string1[0:-1], string2), store(string1, string2[0:-1]), store(string1[0:-1], string2[0:-1]))
    
# This function prints the table of the store function, was struggling to figure
# out how to print the table with the correct numbers
def print_table(string1, string2):
    empty_string = "  "
    string1 = " " + string1
    string2 = " " + string2
    for i in string2:
        empty_string += i + " "
    empty_string += "\n"
    for j in string1:
        empty_string += j + " "
        for k in string2:
            empty_string += str(store(j, k)) + " "
        empty_string += "\n"
    
    print(empty_string)

# This function is the main function that prompts the user for input
def main ():
    print("""
This program efficiently computes the minimum total number of character 
insertion, deletion, and/or substitution operations required to transform 
one string into another.

The String Transformation Operations REquired (STORE) function can be 
defined recursively via the following pseudocode:

if len(string1) == 0:                      # base case: string1 empty
    store(string1, string2) = len(string2) # this many insertions to string 1 required
elif len(string2) == 0:                    # base case: string2 empty
    store(string1, string2) = len(string1) # this many deletions from string 1 required
elif string1[-1] == string2[-1]:           # last characters are the same
    store(string1, string2) = store(string1[0:-1], string2[0:-1]) # no operation needed
else:                                      # last characters differ
    store(string1, string2) = 1+min(store(string1[0:-1], string2      ), # insertion
                                    store(string1      , string2[0:-1]), # deletion
                                    store(string1[0:-1], string2[0:-1])) # substitution

Rather than computing overlapping subproblem answers repeatedly, this program 
computes each of them once, storing them into a table (dynamic programming).
          """)
    
    string1 = input("Enter string1: ")
    string2 = input("Enter string2: ")
    stored_value = store(string1, string2)

    string_array = print_table(string1, string2)

    print(f'\nstore("{string1}", "{string2}") = {stored_value}')

main()