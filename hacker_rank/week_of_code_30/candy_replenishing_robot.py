#!/bin/python3
"""
Alice is hosting a party.
Party lasts t minutes
- n candies at the beginning
- i each minute, a person removes ci candies.
- ci amount of candy removed at minute i.
Algorithm to replenish bowl throughout party.

if party is ending, not refill (time = t),
if bowl contains bi at end of minute i, and bi<5, add n-bi

Given n, t, and c, print the total number of new Candies that boob adds.

"""

def total_added(n, t, c):
    el = n
    res = 0
    for i in range(t-1):
        el = el-c[i]
        if el < 5:
            res += n - el
            el = n

    return res

print(total_added(8, 4, [3, 1, 7, 5]))
