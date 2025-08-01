# TEST1_2 For CS132SP_2025

# Stack Class borrowed from lecture notes
class Stack:
    """Stack implementation as a list"""

    def __init__(self):
        """Create new stack"""
        self._items = []

    # Added the abiliity to output string so it can print in the terminal
    def __str__(self):
        result = "".join(self._items)
        return f"{result}"

    def is_empty(self):
        """Check if the stack is empty"""
        return not bool(self._items)

    def push(self, item):
        """Add an item to the stack"""
        self._items.append(item)

    def pop(self):
        """Remove an item from the stack"""
        return self._items.pop()

    def peek(self):
        """Get the value of the top item in the stack"""
        return self._items[-1]

    def size(self):
        """Get the number of items in the stack"""
        return len(self._items)


# Prefix function, converts user postfix into prefix
def prefix(postFix):
    # Creates Stack
    prefix_stack = Stack()

    # Converts the string into a list
    token_list = postFix.split()

    # Iteration over postfix
    for i in token_list:
        # If i is an operator, pop from the postfix stack, add together with i and push result.
        if i in "+*/":
            operator1 = prefix_stack.pop()
            operator2 = prefix_stack.pop()
            result = operator1 + operator2 + i + " "
            prefix_stack.push(result)

        else:
            # If not operator, then push i to the stack
            prefix_stack.push(i + " ")


    # Creates Temporary List
    temp_list = []

    # Pops the items off the stack into temp list
    while not prefix_stack.is_empty():
        temp_list.append(prefix_stack.pop())

    # Converts Temporary List into string
    return "".join(temp_list)

    

# Main function, asks for user input
def main():
    postFix = str(input("Enter Postfix Expression: "))

    # Calls prefix function, passing in user value
    deliverable = prefix(postFix)

    # Prints prefix deliverable reversed
    print(f"Converted to Prefix is: {deliverable[::-1]}")
main()