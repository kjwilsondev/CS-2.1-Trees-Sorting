import os
from avltreenode import Node

class Tree:
    def __init__(self, items):
        self.root = None
        self.size = 0
        for item in items:
            self.insert(item)

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
    
        elif item < node.data:
            # check if there is something in the nodes left spot
            if node.has_left():
                # if so recursively call insert on that node and store its subtree
                new_subtree = self.insert(item, node.left)
                # check if a new subtree was returned by the insertion
                if new_subtree is not None:
                    # if so update its left child with the new subtree
                    node.left = new_subtree
            # otherwise (the node has no left child)
            else:
                # instantiate a new node object with item
                new_node = AVLNode(item)
                # add the new node to the left
                node.left = new_node
        # otherwise (the item is greater than the current node)
        else:
            # check if there is something in the nodes right spot
            if node.has_right():
                # if so recursively call insert on that node and store its subtree
                new_subtree = self.insert(item, node.right)
                # check if a new subtree was returned by the insertion
                if new_subtree is not None:
                    # if so update its left child with the new subtree
                    node.right = new_subtree
            # otherwise (the node has no right child))
            else:
                # instantiate a new node object with item
                new_node = AVLNode(item)
                # add the new node to the right
                node.right = new_node
        # update the weights of the node
        node.update_height()
        # balance the node's subtrees
        return self.balance(node)


if __name__ == '__main__':
    print("tree")