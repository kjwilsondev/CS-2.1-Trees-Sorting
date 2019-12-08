#!python3

import os
import time

def is_sorted(items):
    """
    Return a boolean indicating whether given items are in sorted order.
    Running time: O(n) - iterates through all elements in array  worst case
    Memory usage: O(1) - no new memory used
    """
    for i in range(0, len(items) - 1):
        if items[i] > items[i+1]:
            return False
    return True

def bubble_sort(items):
    """
    Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    Running time: O(n^2) - for loop within a while loop
    Memory usage: O(logn) - new slice made for every for loop iteration, every slice gets smaller
    """
    size = len(items)
    print(f"size: {size}")

    if is_sorted(items):
        print(f"list already sorted")
        return
    
    while size > 0:
        # i for index
        # e for array[element]
        for i in range(0, size):
            # check if last in list
            if i == size - 1:
                print(f"index {i}: {items[i]} is set!")
                break
            # checks if neighbor is bigger
            print(f"checking index {i+1}, val {items[i+1]}")
            if items[i] > items[i+1]:
                print(f"switching {i}: {items[i]} and {i+1}: {items[i+1]}")
                items[i], items[i+1] = items[i+1], items[i]
                print(items)
        # biggest element has been moved to end
        size -= 1

def selection_sort(items):
    """
    Sort given items by finding minimum item, 
    swapping it with first unsorted item, 
    and repeating until all items are in sorted order.
    Running time: O(n^2) - for loop within a while loop
    Memory usage: O(logn) - new slice made for every for loop iteration, every slice gets smaller
    """
    if is_sorted(items):
        print(f"list already sorted")
        return
    
    start = 0
    switch = False
    for e in range(0, len(items)-1):
        # print(f"current num: {items[e]}")
        # set min_val to first element
        min_val = items[e]
        switch = False
        # print(f"min: {min_val}")
        for i in range(start, len(items)):
            # print(f"checking index {i}, val {items[i]}")
            if min_val > items[i]:
                switch = True
                min_ndx = i
                min_val = items[i]
                # print(items)
                # print(f"new min: {min_val}")
        if switch:
            print(f"switching {items[e]} and {items[min_ndx]}")
            items[min_ndx], items[e] = items[e], min_val
            print(f"array: {items}")
        start += 1


def insertion_sort(items):
    """
    Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    Running time: ??? Why and under what conditions?
    Memory usage: ??? Why and under what conditions?
    """
    # Repeat until all items are in sorted order
    for i in range(0, len(items)-1):
        print(f"i: {i}, {items[i]}")
        # Take first unsorted item
        if items[i] > items[i+1]:
            # Insert it in sorted order in front of items
            for j in reversed(range(0, i)):
                print(f"j: {j}, {items[j]}")
                if items[i] > items[j]:
                    print(f"inserting {items[i]} after {items[j]}")
                    element = items.pop(i)
                    items.insert(j+1, element)
                    print(items)
                print("break")
                break

if __name__ == "__main__":

    arr = [1, 6, 7, 3, 5]
    # arr = [0, -1, 33, 378, 33, 1]
    print(f"array: {arr}")
    print(f"is sorted: {is_sorted(arr)}")
    if is_sorted(arr):
        print(f"array is already sorted")
    else:
        print("b for bubble sort")
        print("s for selection sort")
        print("i for insertion sort")
        method = input("method: ")

        if method == "b":
            print(f"Method: Bubble Sort")
            print(f"Sorting...")
            bubble_sort(arr)
            print(f"Done")
            print(f"array: {arr}")

        if method == "s":
            print(f"Method: Selection Sort")
            print(f"Sorting...")
            selection_sort(arr)
            print(f"Done")
            print(f"array: {arr}")
        
        if method == "i":
            print(f"Method: Insertion Sort")
            print(f"Sorting...")
            insertion_sort(arr)
            print(f"Done")
            print(f"array: {arr}")

        # else:
        #     print("method not found")

    

