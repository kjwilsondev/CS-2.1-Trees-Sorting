#!python3


class PrefixTreeNode:
    """
    PrefixTreeNode: A node for use in a prefix tree that stores a single
    character from a string and a structure of children nodes below it, which
    associates the next character in a string to the next node along its path from
    the tree's root node to a terminal node that marks the end of the string.
    """

    # Dict data structure to store children nodes in
    # Chose dict to save memory
    CHILDREN_TYPE = dict

    def __init__(self, character=None):
        """
        Initialize this prefix tree node with the given character value, an
        empty structure of children nodes, and a boolean terminal property.
        """
        # Character that this node represents
        self.character = character
        # Data structure to associate character keys to children node values
        # self.children = PrefixTreeNode.CHILDREN_TYPE()
        self.children = {}
        # tracks number of searches
        self.popularity = 0
        # tracks length of word
        self.depth = 0
        # Marks if this node terminates a string in the prefix tree
        self.terminal = False

    def is_terminal(self):
        """
        Return True if this prefix tree node terminates a string.
        """
        # Determine if this node is terminal
        return self.terminal

    def num_children(self):
        """
        Return the number of children nodes this prefix tree node has.
        """
        # Determine how many children this node has
        return len(self.children)

    def has_child(self, character):
        """
        Return True if this prefix tree node has a child node that
        represents the given character amongst its children.
        """
        # Check if given character is amongst this node's children
        return character in self.children
        
    def get_all_children(self):
        """
        Returns an array of all child nodes
        """
        children = []
        for char in self.children.keys():
            children.append(self.get_child(char))
        return children

    def get_child(self, character):
        """
        Return this prefix tree node's child node that represents the given
        character if it is amongst its children, or raise ValueError if not.
        """
        if self.has_child(character):
            return self.children[character]
        else:
            raise ValueError(f'No child exists for character {character!r}')

    def add_child(self, character, child_node):
        """
        Add the given character and child node as a child of this node, or
        raise ValueError if given character is amongst this node's children.
        """
        if not self.has_child(character):
            # Add given character and child node to this node's children
            self.children[character] = child_node
        else:
            raise ValueError(f'Child exists for character {character!r}')

    def __repr__(self):
        """
        Return a code representation of this prefix tree node.
        """
        return f'PrefixTreeNode({self.character!r})'

    def __str__(self):
        """
        Return a string view of this prefix tree node.
        """
        return f'({self.character})'

if __name__ == "__main__":
    # TEST: Initialize Nodes
    # Create root node
    root = PrefixTreeNode("")
    print(f"root => {root}")

    # TEST: add_child()
    # Create child node
    k = PrefixTreeNode("k")
    root.add_child(k.character, k)
    # Create grandchild node
    j = PrefixTreeNode("j")
    k.add_child(j.character, j)

    # TEST: has_child()
    # root has child "a" should be true
    print(root.has_child("k"))
    print(f"True => {root.has_child('k')}")
    # root has child "b" should be false
    print(f"False => {root.has_child('j')}")

    # TEST: get_child()
    # root get child "a" should return a
    print(f"(k) => {root.get_child('k')}")
    # prints <__main__.PrefixTreeNode object at storage refrence>
    # Let's try to access j from root
    print(f"True => {root.children['k'].has_child('j')}")

    # TEST: get_all_children()
    # root only has one child => (k)
    print(f"(k) => {root.get_all_children()}")