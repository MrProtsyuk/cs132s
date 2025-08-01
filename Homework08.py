# HOMEWORK08 for CS132SP_2025

# TreeNode Class Borrowed from textbook
class TreeNode:
    def __init__(self, key, value, left=None, right=None, parent=None):
        self.key = key
        self.value = value
        self.left_child = left
        self.right_child = right
        self.parent = parent

    # __str__ method
    def __str__(self):
        return f"{self.key}:{self.value}"

    def is_left_child(self):
        return self.parent and self.parent.left_child is self

    def is_right_child(self):
        return self.parent and self.parent.right_child is self

    def is_root(self):
        return not self.parent

    def is_leaf(self):
        return not (self.right_child or self.left_child)

    def has_any_child(self):
        return self.right_child or self.left_child

    def has_children(self):
        return self.right_child and self.left_child
    
    def replace_value(self, key, value, left, right):
        self.key = key
        self.value = value
        self.left_child = left
        self.right_child = right
        if self.left_child:
            self.left_child.parent = self
        if self.right_child:
            self.right_child.parent = self

    def find_successor(self):
        successor = None
        if self.right_child:
            successor = self.right_child.find_min()
        else:
            if self.parent:
                if self.is_left_child():
                    successor = self.parent
                else:
                    self.parent.right_child = None
                    successor = self.parent.find_successor()
                    self.parent.right_child = self
        return successor

    def find_min(self):
        current = self
        while current.left_child:
            current = current.left_child
        return current
    
    def splice_out(self):
        if self.is_leaf():
            if self.is_left_child():
                self.parent.left_child = None
            else:
                self.parent.right_child = None
        elif self.has_any_child():
            if self.left_child:
                if self.is_left_child():
                    self.parent.left_child = self.left_child
                else:
                    self.parent.right_child = self.left_child
                self.left_child.parent = self.parent
            else:
                if self.is_left_child():
                    self.parent.left_child = self.right_child
                else:
                    self.parent.right_child = self.right_child
                self.right_child.parent = self.parent

    def __iter__(self):
        if self:
            if self.left_child:
                for elem in self.left_child:
                    yield elem
            yield self.key
            if self.right_child:
                for elem in self.right_child:
                    yield elem

# BinarySearchTree Class Borrowed from textbook
class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size
    
    # __str__ method
    def __str__(self):
        if self.root is None:
            return "\n[]"
        # Calling str_print method using root node
        return self._str_print(self.root)

    # Recursive method to print out each node in the tree, including children and parent
    def _str_print(self, node):
        if node is None:
            return "\n[]"
        left = self._str_print(node.left_child)
        right = self._str_print(node.right_child)
        parent_key = node.parent.key if node.parent else ""
        return (f"\n[|K={node.key}|V={node.value}|L={node.left_child.key if node.left_child else ''}|R={node.right_child.key if node.right_child else ''}|P={parent_key}, {left}, {right}]")
        
    def __iter__(self):
        return self.root.__iter__()

    def put(self, key, value):
        if self.root:
            self._put(key, value, self.root)
        else:
            self.root = TreeNode(key, value)
        self.size = self.size + 1
    
    # Fixed Put method to handle duplicate keys
    def _put(self, key, value, current_node):
        if key == current_node.key:
            current_node.value = value

        elif key < current_node.key:
            if current_node.left_child:
                self._put(key, value, current_node.left_child)
            else:
                current_node.left_child = TreeNode(
                    key, value, parent=current_node
                )
        else:
            if current_node.right_child:
                self._put(key, value, current_node.right_child)
            else:
                current_node.right_child = TreeNode(
                    key, value, parent=current_node
                )

    def __setitem__(self, key, value):
        self.put(key, value)

    def get(self, key):
        if self.root:
            result = self._get(key, self.root)
            if result:
                return result.value
        return None
    
    def _get(self, key, current_node):
        if not current_node:
            return None
        if current_node.key == key:
            return current_node
        elif key < current_node.key:
            return self._get(key, current_node.left_child)
        else:
            return self._get(key, current_node.right_child)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        return bool(self._get(key, self.root))

    def delete(self, key):
        if self.size > 1:
            node_to_remove = self._get(key, self.root)
            if node_to_remove:
                self._delete(node_to_remove)
                self.size = self.size - 1
            else:
                raise KeyError("Error, key not in tree")
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1
        else:
            raise KeyError("Error, key not in tree")
        
    def _delete(self, current_node):
        if current_node.is_leaf():  # removing a leaf
            if current_node == current_node.parent.left_child:
                current_node.parent.left_child = None
            else:
                current_node.parent.right_child = None
        elif current_node.has_children():  # removing a node with two children
            successor = current_node.find_successor()
            successor.splice_out()
            current_node.key = successor.key
            current_node.value = successor.value
        else:  # removing a node with one child
            if current_node.left_child:
                if current_node.is_left_child():
                    current_node.left_child.parent = current_node.parent
                    current_node.parent.left_child = current_node.left_child
                elif current_node.is_right_child():
                    current_node.left_child.parent = current_node.parent
                    current_node.parent.right_child = current_node.left_child
                else:
                    current_node.replace_value(
                        current_node.left_child.key,
                        current_node.left_child.value,
                        current_node.left_child.left_child,
                        current_node.left_child.right_child,
                    )
            else:
                if current_node.is_left_child():
                    current_node.right_child.parent = current_node.parent
                    current_node.parent.left_child = current_node.right_child
                elif current_node.is_right_child():
                    current_node.right_child.parent = current_node.parent
                    current_node.parent.right_child = current_node.right_child
                else:
                    current_node.replace_value(
                        current_node.right_child.key,
                        current_node.right_child.value,
                        current_node.right_child.left_child,
                        current_node.right_child.right_child,
                    )

    def __delitem__(self, key):
        self.delete(key)

def main():
    import inspect
    import random

    print("*" * 30 + "\nPrinting main() source code:\n" + "*" * 30)
    print(str(inspect.getsource(main)))
    print("*" * 30 + "\nPrinting main() source output:\n" + "*" * 30)

    myTree = BinarySearchTree()

    data = {"CS121P" : "Introduction to Computer Programming",
            "CS132S" : "Data Structures & Algorithms",
            "CS202H" : "Computer Hardware",
            "CS301A" : "Computer Organization & Architecture",
            "CS312N" : "Networking Principles & Architecture",
            "CS321O" : "Operating Systems",
            "CS321P" : "Programming Languages & Systems",
            "CS322E" : "Software Engineering",
            "CS342D" : "Database Management Systems",
            "CS490I" : "Internship",
            "CS492S" : "Senior Seminar",
            "MA253"  : "Discrete Mathematics"
           }
          
    myRandKeyList = list(data.keys())
    random.shuffle(myRandKeyList)

    print("Binary Search Tree Insertion Test:")
    for i in myRandKeyList:
        print(i,end=' ')
        myTree[i] = "".join(word[0] for word in data[i].split())
        
    print("\n\nBinary Search Tree __str__ Test:")
    print(myTree)
    print("\nBinary Search Tree __iter__ Test:")
    for i in myTree.root:
        print(i + ":" + myTree[i])
    
    print("\nBinary Search Tree Duplicate Key Insertion Test:")
    random.shuffle(myRandKeyList)
    for i in myRandKeyList[:2]:
        print(i,end=' ')
        myTree[i] = data[i]

    print("\n\nBinary Search Tree __str__ Test:")
    print(myTree)
    print("\nBinary Search Tree __iter__ Test:")
    for i in myTree.root:
        print(i + ":" + myTree[i])
    
    print("\nBinary Search Tree __delitem__ Test:")
    random.shuffle(myRandKeyList)
    for i in myRandKeyList[:4]:
        print(i,end=' ')
        del myTree[i]

    print("\n\nBinary Search Tree __str__ Test:")
    print(myTree)
    print("\nBinary Search Tree __iter__ Test:")
    for i in myTree.root:
        print(i + ":" + myTree[i])

main()