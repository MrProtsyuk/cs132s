# TEST1_3 for CS132SP_2025

# Queue Class borrowed from the textbook
class Queue:
    """Queue implementation as a list"""
    def __init__(self):
        """Create new queue"""
        self._items = []

    # Allows string output for queue class, joins the list of numbers to then it can become a string
    def __str__(self):
        result = " ".join(self._items)
        return result

    def is_empty(self):
        """Check if the queue is empty"""
        return not bool(self._items)

    def enqueue(self, item):
        """Add an item to the queue"""
        self._items.insert(0, item)

    def dequeue(self):
        """Remove an item from the queue"""
        return self._items.pop()

    def size(self):
        """Get the number of items in the queue"""
        return len(self._items)


# Radix Sort Function, 
def radixSort(radixQueue, maximum_num):
    # Determines the largest number in the queue and then finds the amount of integers in that number
    # maximum_num = max(radixQueue._items)
    num_digits_iter = len(str(maximum_num))

    # List of each letter in the alphabet
    alphabet_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    # Creates a queue for each digit in the range of the alphabet
    base_alpha_queues = [Queue() for i in range(25)]

    # Print inital radix pass, unsorted
    print(f'\nRadix Pass 0: {radixQueue}')

    # Takes main queue, dequeues word from main queue, 
    # calculates where to sort it, sorts word into respected queue
    for j in range(0, num_digits_iter + 1):
        while not radixQueue.is_empty():
            word = radixQueue.dequeue()

            if len(word) <= j:
                letter = word[0]
            else:
                letter = word[-j + 1]
            for k in range(len(alphabet_list)):
                if letter == alphabet_list[k]:
                    letter = k

            base_alpha_queues[letter].enqueue(word)


        # Reversed queue order; had issue with final loop order and printing in ascending order.
        base_alpha_queues = base_alpha_queues[::-1]

        # For each queue in the base_26_queues list it dequeues each word and enqueues into main queue
        for queue in base_alpha_queues:
            while not queue.is_empty():
                radixQueue.enqueue(queue.dequeue())

        # Prints each radix pass, sorting letter by letter
        print(f'Radix Pass {j}: {radixQueue}')


# Creates main queue that will be operated on in radix sort function
def createQueue(user_input):
    
    # Creates queue
    radix_queue = Queue()

    # Loops over user list and enqueues into radix queue 
    for i in user_input:
        radix_queue.enqueue(i)

    return radix_queue
    
# Main Function, Asks for user inputs
def main():
    user_input = str(input("Enter word list: "))
    
    # Turns user input into list
    user_list = user_input.split(" ")
    maximum_num = max(user_list, key=len)
    user_list.reverse()

    # Calls create array function and passes in user list
    radix_queue = createQueue(user_list)

    # Calls Radix sort function
    radixSort(radix_queue, maximum_num)

main()