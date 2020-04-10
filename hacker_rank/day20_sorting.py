#!/bin/python3
import sys

'''
Day 20: Sorting Algorithms - Bubble Sort

Task: Given array a, of size n.
sort array in ascending order.
Print:
Array is sorted in 'numSwaps' swaps
First Element: 'firstElement'
Last Element: 'lastElement'
'''

n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]

def bubble_sort(arr):
    count_swaps = 0
    arr_len = len(arr)
    for i in range(arr_len):
        for j in range(arr_len - 1):
            if(arr[j] > arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                count_swaps += 1
        if count_swaps == 0:
            break
    print("Array is sorted in {} swaps.".format(count_swaps))
    print("First Element: {}".format(arr[0]))
    print("Last Element: {}".format(arr[-1]))

bubble_sort(a)
