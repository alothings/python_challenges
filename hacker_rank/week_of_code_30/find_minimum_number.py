#!/bin/python3
"""
Program to construct a string that shows how N number of integers
can be compared with nested min functions.

Input: single integer n (# of integers to be compared)
Output: string on a single line of its representation:

i: 2
o: min(int, int)

i:3
o: min(int, min(int, int))
"""


def find_min_representation(n):
    s = "min(int, int)"
    return helper_recursive(n, s)


def helper_recursive(n, s):
    o = "min(int, "
    c = ")"
    if n == 2:
        return s
    else:
        return helper_recursive(n-1, o+s+c)


print(find_min_representation(4))
