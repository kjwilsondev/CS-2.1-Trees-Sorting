#!python3

from sorting_iterative import is_sorted, selection_sort

def merge(items1, items2):
    """
    Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    Running time: O(m) or O(n), iterates all the way through the shorter input list
    Memory usage: O(m + n) - new array output
    """
    items = []
    # Repeat until one list is empty
    while len(items1) > 0 and len(items2) > 0:
        # Find minimum item in both lists and append it to new list
        if items1[0] < items2[0]:
            items.append(items1[0])
            del items1[0]
        else:
            items.append(items2[0])
            del items2[0]
    # Append remaining items in non-empty list to new list
    if len(items1) > 0:
        items.extend(items1)
        return items
    items.extend(items2)
    return items

def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # Split items list into approximately equal halves
    mid = (len(items)-1)//2
    half1, half2 = items[:mid], items[mid:]
    print(half1, half2)
    # Sort each half using any other sorting algorithm
    selection_sort(half1)
    selection_sort(half2)
    # Merge sorted halves into one list in sorted order
    merged = merge(half1, half2)
    return merged

def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if list is so small it's already sorted (base case)
    # TODO: Split items list into approximately equal halves
    # TODO: Sort each half by recursively calling merge sort
    # TODO: Merge sorted halves into one list in sorted order


def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (TODO: document your method here) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Choose a pivot any way and document your method in docstring above
    # TODO: Loop through all items in range [low...high]
    # TODO: Move items less than pivot into front of range [low...p-1]
    # TODO: Move items greater than pivot into back of range [p+1...high]
    # TODO: Move pivot item into final position [p] and return index p


def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: ??? Why and under what conditions?
    TODO: Worst case running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if high and low range bounds have default values (not given)
    # TODO: Check if list or range is so small it's already sorted (base case)
    # TODO: Partition items in-place around a pivot and get index of pivot
    # TODO: Sort each sublist range by recursively calling quick sort

if __name__ == "__main__":

    print("run tests")
    print("merge for merge test")
    print("split for split sort merge test")
    method = input("method: ")

    if method == "merge":
        print("...")
        print("merge test")
        print("...")
        arr1 = [1, 3, 5, 6, 7]
        arr2 = [-1, 0, 1, 33, 33, 378]
        len_arr = len(arr1) + len(arr2)
        # print(f"array: {arr1}")
        # print(f"1st list has {len(arr1)} elements")
        # print(f"is sorted: {is_sorted(arr1)}")
        # print(f"array: {arr2}")
        # print(f"2nd list has {len(arr2)} elements")
        # print(f"is sorted: {is_sorted(arr2)}")
        result = (merge(arr1, arr2))
        # print(f"merged array: {merged}")
        # print(f"return string has {len(merged)} elements")
        # print(f"return string should have {len_arr} elements")
        if len_arr == len(result):
            print("...PASS")
        else:
            print("...FAIL")
    
    if method == "split":
        print("...")
        print("split sort merge test")
        print("...")
        arr = [8, 3, 7, 6, 1]
        len_arr = len(arr)
        result = split_sort_merge(arr)
        if len_arr == len(result):
            print("...PASS")
        else:
            print("...FAIL")

