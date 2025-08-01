# HOMEWORK02 for CS132SP_2025

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

# PostFix conversion function; Modified version of what was seen in 3.9 if the textbook
def postFix(userExp):
    # Create Stack
    postfix_stack = Stack()
    # Split String into List
    token_list = userExp.split()

    # Reverses order because postfix is just prefix reversed with a couple 
    # other things, thats why we have the loop below lol k-bye
    token_list = token_list[::-1]

    # Iteration over prefix
    for i in token_list:
        # If i is an operator, pop from the postfix stack, add together with i and push result.
        if i in "+*/":
            operator1 = postfix_stack.pop()
            operator2 = postfix_stack.pop()
            result = operator1 + operator2 + i + " "
            postfix_stack.push(result)

        else:
            # If not operator, then push i to the stack
            postfix_stack.push(i + " ")
            

    return postfix_stack

# Main Function, does main function things.
def main():
    userInput = str(input("Enter Prefix Expression: "))
    output = postFix(userInput)
    print(f'Converted to Postfix is: {output}')

main()

