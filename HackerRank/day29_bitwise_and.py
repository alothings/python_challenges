#!/bin/python3
"""
Task 
Given set . Find two integers,  and  (where ), from set  such that the value 
of  is the maximum possible and also less than a given integer, . In this case,
  represents the bitwise AND operator.

Input Format

The first line contains an integer, , the number of test cases. 
Each of the  subsequent lines defines a test case as  space-separated integers, 
and , respectively.
"""
import sys

t = int(input().strip())
l = {}
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    l[n] = k

def find_max(n, k):
    l = []
    for i in range(n,0,-1):
        for j in range(i-1, 0, -1):
            l.append(j & i)
    l.sort()
    max = 0
    for el in l:
        if el >= k: break
        if max < el:
            max = el
    return max


for k, v in l.items():
    print(find_max(k, v))


