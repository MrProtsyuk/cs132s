#Homework09 for CS132SP_2025

# Vertex Class Borrowed from the Textbook
class Vertex:
    def __init__(self, key):
        self.key = key
        self.neighbors = {}
        # Added attributes for BFS
        self._color = "white" 
        self._distance = 0
        self._previous = None

    def get_neighbor(self, other):
        return self.neighbors.get(other, None)

    def set_neighbor(self, other, weight=0):
        self.neighbors[other] = weight

    def __repr__(self):
        return f"Vertex({self.key})"

    def __str__(self):
        return (
            str(self.key)
            + " connected to: "
            + str([x.key for x in self.neighbors])
        )

    def get_neighbors(self):
        return self.neighbors.keys()

    def get_key(self):
        return self.key
    
    # Added methods for BFS (color, distance, previous) found in pythonds3: https://github.com/psads/pythonds3/blob/master/pythonds3/graphs/adjacency_graph.py
    def get_color(self):
        return self._color

    def set_color(self, color):
        self._color = color

    color = property(get_color, set_color)

    def get_distance(self):
        return self._distance

    def set_distance(self, distance):
        self._distance = distance

    distance = property(get_distance, set_distance)
    
    def get_previous(self):
        return self._previous
    
    def set_previous(self, previous):
        self._previous = previous
    
    previous = property(get_previous, set_previous)

# Graph Class Borrowed from the Textbook
class Graph:
    def __init__(self):
        self.vertices = {}

    def set_vertex(self, key):
        self.vertices[key] = Vertex(key)

    def get_vertex(self, key):
        return self.vertices.get(key, None)

    def __contains__(self, key):
        return key in self.vertices

    def add_edge(self, from_vert, to_vert, weight=0):
        if from_vert not in self.vertices:
            self.set_vertex(from_vert)
        if to_vert not in self.vertices:
            self.set_vertex(to_vert)
        self.vertices[from_vert].set_neighbor(self.vertices[to_vert], weight)

    def get_vertices(self):
        return self.vertices.keys()

    def __iter__(self):
        return iter(self.vertices.values())
    
# Queue Class Borrowed from the Textbook
class Queue:
    """Queue implementation as a list"""

    def __init__(self):
        """Create new queue from Vertex"""
        self._items = Vertex()

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

# BFS Function Borrowed from the Textbook
def bfs(start):
    start.distance = 0
    start.previous = None
    vert_queue = Queue()
    vert_queue.enqueue(start)
    while vert_queue.size() > 0:
        current = vert_queue.dequeue()
        for neighbor in current.get_neighbors():
            if neighbor.color == "white":
                neighbor.color = "gray"
                neighbor.distance = current.distance + 1
                neighbor.previous = current
                vert_queue.enqueue(neighbor)
        current.color = "black"

# Create a graph
def create_graph():
    graph = Graph()
    # Creates a node for each number from 0-511, or 000000000-111111111 in binary
    for i in range(0, 512):
        graph.set_vertex(i)
        for j in range(1, 10):
            vert = int_toBinary(i)
            flip = int_toBinary(assignFlip(j))
            singleBinary = combineValues(vert, flip)
            singleInt = binary_toInt(singleBinary)
            graph.add_edge(i, singleInt)

    return graph

def assignFlip(j):
    flipList = [11, 23, 38, 89, 186, 200, 308, 416, 464]
    return flipList[j - 1]

# Function to convert an integer to a binary string of length 9
def int_toBinary(num):
    output = [0] * 9
    for i in range(9):
        if num % 2 == 1:
            output[i] = 1
        num = num // 2

    # Reverses the output and joins the list of integers into a string
    output.reverse()
    output = "".join(str(x) for x in output)

    return output

def combineValues(vert, flip):
    vert = list(vert)
    flip = list(flip)
    listBin = []
    for i in range(len(vert)):
        if vert[i] == "1" and flip[i] == "1":
            listBin.append(0)
        elif vert[i] == "0" and flip[i] == "0":
            listBin.append(0)
        else:
            listBin.append(1)
    
    return listBin

def grid(input):
    input = list(input)
    result = []
    print()
    for i in range(len(input)):
        if input[i] == "1":
            result.append("T")
        else:
            result.append("H")
    
    print(f"{"".join(result[:3])}\n{"".join(result[3:6])}\n{"".join(result[6:10])}\n")

# Function to convert a binary string to an integer: https://stackoverflow.com/questions/21765779/converting-binary-to-decimal-integer-output
def binary_toInt(binary_str):
    total = 0
    for i in range(len(binary_str)):
            total = total * 2 + binary_str[i]
    return total
        
def main():
    print("""Welcome to Flipper!  

You begin with nine coins, showing "heads", arranged in a 3x3 grid:

HHH    123
HHH    456  <= Coin Choice Options 1-9
HHH    789

Choose a coin to flip it over, along with those vertically and 
horizontally adjacent.

The object of the game is to end up with all coins showing "tails".

If you are stuck, choose Option 0 to show the solution.  :)""")
    graph = create_graph()
    userBoard = 0
    finish = "111111111"
    userLoop = True
    while userLoop:
        print(grid(int_toBinary(int(userBoard))))
        print("Option 0: Solve; Options 1-9: Choose Node")
        print(f"Node {userBoard} ({int_toBinary(userBoard)})")
        print(f"{graph.get_vertex(userBoard)}\n")
        userInput = int(input("Choose Option 0-9: "))
        value = int(userInput)
        print()
        if userInput == 0:
            # really confused on how to do this 
                        
            # intToBin = int_toBinary(userBoard)
            # grid(split_and_list(intToBin))
            print("Success!  :)")
            return
        # if userBoard == finish:
        #     userLoop = False
        #     intToBin = int_toBinary(userBoard)
        #     grid(value, intToBin)
        #     print("Success!  :)")
        #     return
        elif userInput > 0 and userInput < 10:
           

            
            print(userBoard)
        else:
            print("Please enter a valid number between 0-9.\n")
            continue
                

main()