"""
Examples for handling exceptions:

try:
    print(1/0)
except ZeroDivisionError as e:
    print("Error code:", e)
    
Task: given two values a and b,
perform integer division

Input: lines:
t = test cases:
t lines with a and b

Output:
print result or zerodivisionerror or value error
"""


import sys

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        try:
            a, b = map(int, input().split())
            print(a//b)
        except (ZeroDivisionError, ValueError) as e:
            print("Error Code: {}".format(e))



