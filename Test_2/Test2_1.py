class Binary_Min_Max_Heap:
    def __init__(self, alist):
        self._items = alist

    # Because it is a Binary Heap, the minimum level will always be 1
    def is_min_level(self, i):
        return i % 2 == 1
    
    # https://anesiner.wordpress.com/2007/04/18/heap-structures-min-max-heaps/
    def grandparent(self, i):
        return (i - 3) // 4

    # https://stackoverflow.com/questions/4698338/minmax-heap-implementation-without-an-array
    # Used this to understand how to figure out if something is a parent
    def parent(self, i):
        return (i - 1) // 2
    
    # https://stackoverflow.com/questions/4698338/minmax-heap-implementation-without-an-array
    # Used this to figure out if something was a grand parent
    def left_child(self, i):
        return 2 * i + 1
    
    # https://stackoverflow.com/questions/23573903/checking-for-haschild-in-heap
    # Used this to figure out if something has children
    def has_children(self, i):
        return i < len(self._items) // 2
    
    def has_grandparent(self, i):
        return i > 3

    def index_smallest_child_or_grandchild(self, i):
        if self.has_children(i):
            left = self.left_child(i)
            right = left + 1
            if right < len(self._items):
                if self._items[left] < self._items[right]:
                    return left
                else:
                    return right
            else:
                return left
        else:
            return None

    def index_largest_child_or_grandchild(self, i):
        if self.has_children(i):
            left = self.left_child(i)
            right = left + 1
            if right < len(self._items):
                if self._items[left] > self._items[right]:
                    return left
                else:
                    return right
            else:
                return left
        else:
            return None

    # Most of these functions were extracted from here: https://en.wikipedia.org/wiki/Min-max_heap
    def push_down_min(self, m):
        if self.has_children(m):
            min = self.index_smallest_child_or_grandchild(m)
            if self.has_grandparent(min):
                if self._items[min] < self._items[m]:
                    self._items[min], self._items[m] = self._items[m], self._items[min]
                    if self._items[min] > self._items[self.parent(min)]:
                        self._items[min], self._items[self.parent(min)] = self._items[self.parent(min)], self._items[min]
                    self.push_down(min)

            elif self._items[min] < self._items[m]:
                self._items[min], self._items[m] = self._items[m], self._items[min]

    def push_down_max(self, m):
        if self.has_children(m):
            min = self.index_largest_child_or_grandchild(m)
            if self.has_grandparent(min):
                if self._items[min] > self._items[m]:
                    self._items[min], self._items[m] = self._items[m], self._items[min]
                    if self._items[min] < self._items[self.parent(min)]:
                        self._items[min], self._items[self.parent(min)] = self._items[self.parent(min)], self._items[min]
                    self.push_down(min)

            elif self._items[min] > self._items[m]:
                self._items[min], self._items[m] = self._items[m], self._items[min]

    def push_down(self, i):
        if self.is_min_level(i):
            self.push_down_min(i)
        else:
            self.push_down_max(i)

    def push_up_min(self, i):
        if self.has_grandparent(i) and self._items[i] < self._items[self.grandparent(i)]:
            self._items[i], self._items[self.grandparent(i)] = self._items[self.grandparent(i)], self._items[i]
            self.push_up_min(self.grandparent(i))

    def push_up_max(self, i):
        if self.has_grandparent(i) and self._items[i] > self._items[self.grandparent(i)]:
            self._items[i], self._items[self.grandparent(i)] = self._items[self.grandparent(i)], self._items[i]
            self.push_up_max(self.grandparent(i))
        
    def push_up(self, i):
        if self.parent(i) != 0:
            if self.is_min_level(i):
                if self._items[i] > self._items[self.parent(i)]:
                    self._items[i], self._items[self.parent(i)] = self._items[self.parent(i)], self._items[i]
                    self.push_up_max(self.parent(i))
                else:
                    self.push_up_min(i)
            else:
                if self._items[i] < self._items[self.parent(i)]:
                    self._items[i], self._items[self.parent(i)] = self._items[self.parent(i)], self._items[i]
                    self.push_up_min(self.parent(i))
                else:
                    self.push_up_max(i)

    def insert(self, i):
        self._items.append(i)
        self.push_up(len(self._items) - 1)
        return i
    
    def find_min(self):
        return self._items[0]

    def find_max(self):
        if len(self._items) == 1:
            return self._items[0]
        elif len(self._items) == 2:
            return self._items[1]
        else:
            return max(self._items[1], self._items[2])
        
    def remove_min(self):
        if len(self._items) == 1:
            return self._items.pop(0)
        minValue = self._items[0]
        self._items[0] = self._items.pop()
        self.push_down(0)
        return minValue

    def remove_max(self):
        if len(self._items) == 2:
            return self._items.pop()
        elif len(self._items) == 3:
            return self._items.pop(1)
        else:
            max_index = 1 if self._items[-1] > self._items[1] else 2
            self._items[max_index], self._items[-1] = self._items[-1], self._items[max_index]
            return self._items.pop()
        
    def build_binary_min_max_heap(self, alist):
        self._items = alist
        for i in range(len(alist) // 2, -1, -1):
            self.push_down(i)
        return self._items

class DEPQ:
    # Passing alist to Binary Min Max Heap and then initializing
    def __init__(self, alist):
        self._heap = Binary_Min_Max_Heap(alist)
        self._heap.build_binary_min_max_heap(alist)

    # All functions below used the functions in the Binary Min Max Heap Class
    def is_empty(self):
        return len(self._heap._items) == 0
            
    def size(self):
        return len(self._heap._items)
    
    def get_min(self):
        return self._heap.find_min()
    
    def get_max(self):
        return self._heap.find_max()
    
    def put(self, i):
        return self._heap.insert(i)
        
    def remove_min(self):        
        return self._heap.remove_min()
    
    def remove_max(self):
        return self._heap.remove_max()

def main():
    print("""This program simulates an emergency room with limited capacity.
Event 0 is an available doctor. Other events are arriving patients.
Highest priority patient present is seen first when a doctor is free.
Lowest priority patient present is dismissed when capacity is exceeded.""")
    capacity = int(input("Enter Capacity: "))
    event_list = list(input("Enter event list: "))
    my_deqp = DEPQ(event_list)
    size = 0
    prevVar = 0
    while not my_deqp.is_empty():
            tempVar = int(my_deqp.remove_min())
            if tempVar > 0:
                prevVar = tempVar
                size += 1
                print(f"Enqueue patient with priority {tempVar} (size is {size}).")
                if size > capacity:
                    size -= 1
                    print(f"Dismiss patient with priority {tempVar} (capacity exceeded).")
            elif tempVar == 0 and size > 0:
                size -= 1
                print(f"Dequeue patient with priority {prevVar} (size is {size}).")
            elif size >= 0 and tempVar == 0:
                print(f"Dequeue patient with priority {tempVar} (size is {size}).")

    print("Emergency room is currently empty.")

main()