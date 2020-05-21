#!/usr/bin/env python
"""merge_sort.py

A Python implementation of the merge sort algorithm."""

__author__ = "Ryan Morehouse"
__license__ = "MIT"

import random

def merge_sort(array):
    # base cases
    if len(array) == 1:
        return array
    elif len(array) == 2:
        if array[0] > array[1]:
            return [array[1], array[0]]
        else:
            return [array[0], array[1]]
    # split array
    m = len(array) / 2

    # recursion step
    sub_01 = merge_sort(array[:m])
    sub_02 = merge_sort(array[m:])

    result = []
    x = 0
    y = 0

    # merge sorted sub arrays
    while x < len(sub_01) and y < len(sub_02):
        if sub_01[x] < sub_02[y]:
            result.append(sub_01[x])
            x += 1
        else:
            result.append(sub_02[y])
            y += 1
    
    # collect remainders
    if x < len(sub_01):
        for z in sub_01[x:]:
            result.append(z)
    elif y < len(sub_02):
        for z in sub_02[y:]:
            result.append(z)
    
    return result

def main():
    length = random.randint(10,50)
    array = [random.randint(0, 800) for x in range(length)]
    print("Starting Array: {}\n".format(array))
    sorted_array = merge_sort(array)
    print("Sorted Array: {}\n".format(sorted_array))

if __name__ == "__main__":
    main()
