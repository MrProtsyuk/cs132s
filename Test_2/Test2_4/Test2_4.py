# Vertex Class Borrowed from textbook
class Vertex:
    def __init__(self, key):
        self.key = key
        self.neighbors = {}
        # Added attributes for BFS
        self._color = "white" 
        self._distance = 0
        self._previous = None
        # Added attributes for DFS
        self._discovery_time = 0
        self._closing_time = 0

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

    # Added methods for DFS (discovery_time, closing_time) found in pythonds3: https://github.com/psads/pythonds3/blob/master/pythonds3/graphs/adjacency_graph.py

    def get_discovery_time(self):
        return self._discovery_time
    
    def set_discovery_time(self, discovery_time):
        self._discovery_time = discovery_time

    discovery_time = property(get_discovery_time, set_discovery_time)

    def get_closing_time(self):
        return self._closing_time
    
    def set_closing_time(self, closing_time):
        self._closing_time = closing_time

    closing_time = property(get_closing_time, set_closing_time)

# Graph Class Borrowed from textbook
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
    
# DFSGraph Class Borrowed from textbook 
class DFSGraph(Graph):
    def __init__(self):
        super().__init__()
        self.time = 0

    def dfs(self):
        for vertex in self:
            vertex.color = "white"
            vertex.previous = -1
        for vertex in self:
            if vertex.color == "white":
                self.dfs_visit(vertex)


    def dfs_visit(self, start_vertex):
        start_vertex.color = "gray"
        self.time = self.time + 1
        start_vertex.discovery_time = self.time
        for next_vertex in start_vertex.get_neighbors():
            if next_vertex.color == "white":
                next_vertex.previous = start_vertex
                self.dfs_visit(next_vertex)
        start_vertex.color = "black"
        self.time = self.time + 1
        start_vertex.closing_time = self.time

def main():
    # Try statement: tries to open the file and split the data
    try:
        print("""Reading input file "prereq.txt"...""")
        readFile = open("prereq.txt", "r")
        # Initializes DFS Graph
        newGraph = DFSGraph()

        # Takes each line in the file, splits it, prints the line, 
        # creates a vertex for a class, and creates edges for the prereq classes
        for i in readFile:
            classes, prereq = i.split(":")
            classes = classes.strip()
            prereq = prereq.strip()
            print(f"Processing input file line-> {classes}: {prereq}")
            prereq = prereq.split(" ")
            newGraph.set_vertex(classes)
            for j in prereq:
                newGraph.add_edge(j, classes)
        
        readFile.close()
        print("Performing topological sort...")

        # Starts DFS Algo, initalizes empty list
        newGraph.dfs()
        newList = []

        # Appends each node with its closing time
        for k in newGraph:
            newList.append((k.closing_time, k.get_key()))


        # Sorts the nodes based on their closing time values, then sorts alphabetically
        # Reference: https://stackoverflow.com/questions/10695139/sort-a-list-of-tuples-by-2nd-item-integer-value
        newList = sorted(newList, key=lambda x: (x[1], x[0]))

        # Since the list a bunch of tuples, I used this to print only the class values and not the closing time values
        # Reference: https://www.geeksforgeeks.org/python-get-first-element-in-list-of-tuples/
        orderedList = [y[1] for y in newList]

        # Removes empty space
        while '' in orderedList:
            orderedList.remove('')

        print(f"Ordered List:\n {orderedList}\n ")

    # Looks to catch an IO Error if the file cant be opened.
    except IOError:
        print("Error: prereq.txt does not exist or it can't be opened for input.")
        print("Program exiting now...")

main()