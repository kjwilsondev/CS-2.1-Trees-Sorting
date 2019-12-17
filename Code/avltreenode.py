import os

class AVLNode:
    def __init__(self, items):
        self.root = None
        self.size = 0
        for item in items:
            self.insert(item)