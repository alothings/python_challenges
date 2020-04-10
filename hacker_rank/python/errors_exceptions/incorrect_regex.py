"""

Task: Given string S, find out whether S is a valid regex or not

Input: T containing number of test cases
next t lines are strings s

Output: return True or False

"""

import re


if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        try:
            re.compile(input())
            print('True')
        except re.error:
            print('False')
