#!python3
"""Autocomplete Dictionary Input Challenge"""
# to play the game:
# uncomment the game function
# to compare iterative and tree autocomplete functions
# uncomment the benchmark function

import sys
from prefixtree import PrefixTree
import timeit

def load(text):
    """
    Loads words from dictionary
    """
    file  = open(text, 'r')
    words = file.readlines()
    file.close()
    return words

# Old iterative method
def select(word_part, text):
    """
    Adds words in text that match beginning to words list
    Stops game if no words found
    """
    # initialize autocomplete word list
    words = list()
    # iterates through text to find matches
    for line in text:
        if line.startswith(word_part):
            words.append(line)

    if len(words) == 0:
        print("No words found!")
        sys.exit(1)

    return words

def game():
    print("\nWelcome to Autocomplete\n")

    word_part = input("Give me a word part\n\n")
    # checks emptiness
    if not word_part:
        print("You must enter a word part\n")
        sys.exit(1)

    loads   = load("/usr/share/dict/words")
    tree    = PrefixTree(loads)
    words   = tree.complete(word_part)
    results = print("{} results were found".format(len(words)))
    number  = input("How many results would you like?\n")

    # checks edge cases for results display
    if (len(number) <= 0) or not (number.isdigit()):
        print("You must input a positive number :)")
        sys.exit()

    count = 0

    # retrives set number of results
    if 0 < len(words):
        if len(words) < int(number):
            print("Sorry there's not that many but here's what we got\n")
            number = len(words)

        print()

        while (count < int(number)):
            sentence = "    {}.    {}".format((count + 1), words[count])
            print(sentence)
            count += 1

def benchmark():
    print("Let's compare our iterative and prefix tree autocomplete methods")
    print("...")

    print("First lets compare set up time")
    print("Set up for iterative autocomplete:")
    print("...")
    setup = "from __main__ import load"
    i_setup_time = timeit.timeit("load('/usr/share/dict/words')", setup=setup, number=1)
    print("Done")
    print("Set up for tree autocomplete:")
    print("...")
    setup = """from __main__ import load, PrefixTree"""
    t_setup_time = timeit.timeit("PrefixTree(load('/usr/share/dict/words'))", setup=setup, number=1)
    print("Done")

    print("Now let's compare processing time!")
    print("Lets see how long it takes to gather all words")
    print("starting with the letter a")
    print("Processing time for iterative autocomplete:")
    print("...")
    setup = "from __main__ import load, select"
    i_process = timeit.timeit("select('a', load('/usr/share/dict/words'))", setup=setup, number=1)
    i_process -= i_setup_time
    print("Done")
    print("Processing time for tree autocomplete:")
    print("...")
    setup = "from __main__ import load, PrefixTree"
    t_process = timeit.timeit("PrefixTree(load('/usr/share/dict/words')).complete('a')", setup=setup, number=1)
    t_process -= t_setup_time
    print("Done")

    print("iterative set up: {}".format(i_setup_time))
    print("iterative processing: {}".format(i_process))
    print("tree set up: {}".format(t_setup_time))
    print("tree process: {}".format(t_process))

if __name__ == '__main__':
    game()
    # benchmark()