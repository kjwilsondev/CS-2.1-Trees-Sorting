#!python3


class PrefixTreeNode:
    """
    PrefixTreeNode: A node for use in a prefix tree that stores a single
    character from a string and a structure of children nodes below it, which
    associates the next character in a string to the next node along its path from
    the tree's root node to a terminal node that marks the end of the string.
    """

    # List data structure to store children nodes in
    # Chose list for constant time searching
    CHILDREN_TYPE = []

    def __init__(self, character=None):
        """
        Initialize this prefix tree node with the given character value, an
        empty structure of children nodes, and a boolean terminal property.
        """
        # Character that this node represents
        self.character = character
        # Data structure to associate character keys to children node values
        # self.children = PrefixTreeNode.CHILDREN_TYPE()
        # https://stackoverflow.com/questions/10712002/create-an-empty-list-in-python-with-certain-size
        self.children = [None] * 26
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
        # Check ascii slot in children list
        # http://www.asciitable.com
        return self.children[ord(character)-97] != None

    # def get_child(self, character):
    #     """Return this prefix tree node's child node that represents the given
    #     character if it is amongst its children, or raise ValueError if not."""
    #     if self.has_child(character):
    #         # TODO: Find child node for given character in this node's children
    #     else:
    #         raise ValueError(f'No child exists for character {character!r}')

    # def add_child(self, character, child_node):
    #     """Add the given character and child node as a child of this node, or
    #     raise ValueError if given character is amongst this node's children."""
    #     if not self.has_child(character):
    #         # TODO: Add given character and child node to this node's children
    #     else:
    #         raise ValueError(f'Child exists for character {character!r}')

    # def __repr__(self):
    #     """Return a code representation of this prefix tree node."""
    #     return f'PrefixTreeNode({self.character!r})'

    # def __str__(self):
    #     """Return a string view of this prefix tree node."""
    #     return f'({self.character})'

if __name__ == "__main__":
    # Create root node
    root = PrefixTreeNode("")
    # Create child node
    a = PrefixTreeNode("a")
    root.children[0] = a
    # has child "a" should be true
    print(root.has_child("a"))
    # has child "b" should be false
    print(root.has_child("b"))


    # raise error if not a letter
    # if not character.isalpha():
    #     raise TypeError("child node is a not a letter")
    # print(node.has_child("1"))