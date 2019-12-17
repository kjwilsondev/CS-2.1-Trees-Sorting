import os
from avltreenode import Node

class Tree:
    def __init__(self, items):
        self.root = None
        self.size = 0
        for item in items:
            self.insert(item)

    def insert(self, item, node=None):
        """
        Check if tree is empty -> self.root = Node(item)
        Check if item is already in tree -> if so don't add it
        Check if item < node.data:
            Check if node has left node:
                Recursively call insert(node = left node)
                Add new branch as left node
            If there isnt a left node:
                Add Node(item) as left node
        Check if item > node.data:
            Check if node has right node:
                Recursively call insert(node = right node)
                Add new branch as right node
            If there isnt a right node:
                Add Node(item) as right node
        Update heights
        Balance the tree
        """


if __name__ == '__main__':
    print("tree")