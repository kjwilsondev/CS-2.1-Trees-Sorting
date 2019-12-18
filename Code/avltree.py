import os
from avltreenode import Node

class Tree:
    def __init__(self, items):
        self.root = None
        self.size = 0
        for item in items:
            self.insert(item)
    
    def is_empty(self):
        """
        Return True if tree is empty.
        """
        return self.size == 0

    def insert(self, item, node=None):
        # Check if tree is empty -> self.root = Node(item)
        if self.is_empty():
            self.root = Node(item)
            self.size += 1
            return

        # If no node input, assume recursion starting at root 
        if node is None:
            node = self.root
            self.size += 1
        
        # Check if item is already in tree -> if so don't add it
        if item == node.data:
            self.size -= 1
            return



if __name__ == '__main__':
    print("tree")