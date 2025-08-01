# HOMEWORK07 for CS132SP_2025
# Had to use a lot of outside resources for this one because I was mad confused

class Binary_Min_Max_Heap:
    def __init__(self, alist):
        self._items = alist

    # Because it is a Binary Heap, the minimum level will always be 0
    def is_min_level(self, i):
        return i % 2 == 0
    
    # https://anesiner.wordpress.com/2007/04/18/heap-structures-min-max-heaps/
    # If i is less than 3 that means i must have a parent but cannor have a grandparent
    def grandparent(self, i):
        if i < 3:
            return None
        return (i - 1) //4
    
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
        return 2 * i + 1 < len(self._items)
    
    # If i is less than 3 that means i must have a parent but cannot have a grandparent
    def has_grandparent(self, i):
        return i >=3
    
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
        self._items[0], self._items[-1] = self._items[-1], self._items[0]
        return self._items.pop()

    def remove_max(self):
        if len(self._items) == 2:
            return self._items.pop()
        elif len(self._items) == 3:
            return self._items.pop(1)
        else:
            max_index = 1 if self._items[1] > self._items[2] else 2
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

# Starter code that was given
def main():
    import inspect
    import random

    print("*" * 30 + "\nPrinting main() source code:\n" + "*" * 30)
    print(str(inspect.getsource(main)))
    print("*" * 30 + "\nPrinting main() source output:\n" + "*" * 30)

    print("This program implements a double-ended priority queue class using a min-max heap.")
    max_range = int(input("Enter max range: "))
    list_size = int(input("Enter list size: "))

    my_list = [random.randrange(1, max_range+1, 1) for i in range(list_size)]
    print("Original List:", my_list)

    my_depq = DEPQ(my_list)
    print("DEPQ min-max heap:", my_depq)

    print("size() = ", my_depq.size())
    print("is_empty() = ", my_depq.is_empty())
    print("remove_min() = ", my_depq.remove_min())
    print("DEPQ min-max heap:", my_depq)
    print("remove_max() = ", my_depq.remove_max())
    print("DEPQ min-max heap:", my_depq)
    print("remove_min() = ", my_depq.remove_min())
    print("DEPQ min-max heap:", my_depq)
    print("remove_max() = ", my_depq.remove_max())
    print("DEPQ min-max heap:", my_depq)
    print("put(max_range) = ", my_depq.put(max_range))
    print("DEPQ min-max heap:", my_depq)
    print("get_min() = ", my_depq.get_min())
    print("get_max() = ", my_depq.get_max())
    print("DEPQ min-max heap:", my_depq)

main()