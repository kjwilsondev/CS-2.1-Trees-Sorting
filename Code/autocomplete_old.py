"""Autocomplete Dictionary Input Challenge"""

import sys

def load(text):
    """
    Loads words from dictionary
    """
    file  = open(text, 'r')
    words = file.readlines()
    file.close()
    return words

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
    words   = select(str(word_part), loads)
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

if __name__ == '__main__':
    game()