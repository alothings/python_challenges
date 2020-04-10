#!/bin/python3

'''
Day 16: Exceptions
Parsing integer from a string and printing a custom error message
Note: In python BaseException is the base class for Exceptions

Task: Read string s, print integer value. if S cannot be converted, print
"Bad String."
'''

import sys

S = input().strip()

def stringToInt(S):
    try:
        return int(S)
    except Exception:
        print("Bad String")

print(stringToInt(S))
