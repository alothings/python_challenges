#!/bin/python3

'''
Day 17: More Exceptions
Goal: Through and propagating exceptions.

Task: Write a Calculator class. Method power(int n, int p).
return n^p
if either is negative, throw exception.
'''

class Calculator(object):
    def __init__(self):
        pass

    def power(self, a, b):
        if a < 0 or b < 0:
            raise Exception('n and p should be non-negative')
        return a**b


myCalculator=Calculator()
T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e)