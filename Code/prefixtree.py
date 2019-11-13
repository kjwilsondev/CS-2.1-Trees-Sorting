#!python3

from prefixtreenode import PrefixTreeNode


class PrefixTree:
    """
    PrefixTree: 
    A multi-way prefix tree that stores strings 
    with efficient methods to insert a string into the tree:
    check if it contains a matching string,
    and retrieve all strings that start with a given prefix string.

    Time complexity of these methods depends only on the number of strings
    retrieved and their maximum length (size and height of subtree searched),
    but is independent of the number of strings stored in the prefix tree, as
    its height depends only on the length of the longest string stored in it.

    This makes a prefix tree effective for spell-checking and autocompletion.
    Each string is stored as a sequence of characters along a path from the
    tree's root node to a terminal node that marks the end of the string.
    """

    # Constant for the start character stored in the prefix tree's root node
    START_CHARACTER = ''

    def __init__(self, strings=None):
        """
        Initialize this prefix tree and insert the given strings, if any.
        """
        # Create a new root node with the start character
        self.root = PrefixTreeNode(PrefixTree.START_CHARACTER)
        # Count the number of strings inserted into the tree
        self.size = 0
        # Array of strings in tree
        self.strings = []
        # Insert each string, if any were given
        if strings is not None:
            for string in strings:
                self.insert(string)

    def __repr__(self):
        """
        Return a string representation of this prefix tree.
        """
        return f'PrefixTree({self.strings()!r})'

    def is_empty(self):
        """
        Return True if this prefix tree is empty (contains no strings).
        """
        return self.size == 0

    def contains(self, string):
        """
        Return True if this prefix tree contains the given string.
        """
        # Start with root
        node = self.root
        # Iterate through letters in string
        for letter in string:
            # Check if node has child matching letter
            if not node.has_child(letter):
                return False
            # Move to next node
            node = node.get_child(letter)
        # Returns node if it is an ending node
        return node.terminal

    def insert(self, string):
        """
        Insert the given string into this prefix tree.
        """
        # Start with root
        node = self.root
        depth = 0
        # Add string to tree strings
        self.strings.append(string)
        # Iterate through letters in string
        for letter in string:
            # Check if node has child matching letter
            if node.has_child(letter):
                # move on to the next node
                node = node.get_child(letter)
                depth += 1
                node.depth = depth
            else:
                # create a child node
                child = PrefixTreeNode(letter)
                depth += 1
                # add it as a child to the node
                node.add_child(letter, child)
                # move on to the next node
                node = node.get_child(letter)
                node.depth = depth
        # On the last node make terminal true
        node.terminal = True
        # no return statement

    def _find_node(self, string):
        """
        Return a tuple containing:
        (the node that terminates the given string, and the node's depth)
        if the given string is not completely found, 
        return (None, depth of the last matching node)
        Search is done iteratively with a loop starting from the root node.
        """
        # Match the empty string
        if len(string) == 0:
            return self.root, 0
        # Start with the root node
        node = self.root
        # Keep track of depth
        depth = 0
        # Iterate through letters in string
        for letter in string:
            # Check if node has child matching letter
            if not node.has_child(letter):
                return (None, depth)
            else:
                depth += 1
                # move on to the next node
                node = node.get_child(letter)
        print(f"depth: {depth}, node.depth: {node.depth}")
        return(node, depth)
                
    def complete(self, prefix):
        """
        Return a list of all strings stored in this prefix tree that start
        with the given prefix string.
        """
        # Create a list of completions in prefix tree
        completions = []
        # TODO

    def strings(self):
        """Return a list of all strings stored in this prefix tree."""
        # Create a list of all strings in prefix tree
        # return self.strings

    def _traverse(self, node, prefix, visit):
        """Traverse this prefix tree with recursive depth-first traversal.
        Start at the given node and visit each node with the given function."""
        # TODO


def create_prefix_tree(strings):
    print(f'strings: {strings}')

    tree = PrefixTree()
    print(f'\ntree: {tree}')
    print(f'root: {tree.root}')
    print(f'strings: {tree.strings()}')

    print('\nInserting strings:')
    for string in strings:
        tree.insert(string)
        print(f'insert({string!r}), size: {tree.size}')

    print(f'\ntree: {tree}')
    print(f'root: {tree.root}')

    print('\nSearching for strings in tree:')
    for string in sorted(set(strings)):
        result = tree.contains(string)
        print(f'contains({string!r}): {result}')

    print('\nSearching for strings not in tree:')
    prefixes = sorted(set(string[:len(string)//2] for string in strings))
    for prefix in prefixes:
        if len(prefix) == 0 or prefix in strings:
            continue
        result = tree.contains(prefix)
        print(f'contains({prefix!r}): {result}')

    print('\nCompleting prefixes in tree:')
    for prefix in prefixes:
        completions = tree.complete(prefix)
        print(f'complete({prefix!r}): {completions}')

    print('\nRetrieving all strings:')
    retrieved_strings = tree.strings()
    print(f'strings: {retrieved_strings}')
    matches = set(retrieved_strings) == set(strings)
    print(f'matches? {matches}')


if __name__ == '__main__':
    # Create a dictionary of tongue-twisters with similar words to test with
    tongue_twisters = {
        'Seashells': 'Shelly sells seashells by the sea shore'.split(),
        # 'Peppers': 'Peter Piper picked a peck of pickled peppers'.split(),
        # 'Woodchuck': ('How much wood would a wood chuck chuck'
        #                ' if a wood chuck could chuck wood').split()
    }
    # Create a prefix tree with the similar words in each tongue-twister
    for name, strings in tongue_twisters.items():
        print('\n' + '='*80 + '\n')
        print(f'{name} tongue-twister:')
        create_prefix_tree(strings)
