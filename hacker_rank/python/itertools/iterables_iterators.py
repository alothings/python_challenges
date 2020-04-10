"""

TasK:
Given a list of n lowercase letters. FOr an int k, select any 
k indices with a uniform probability from the list.

Find prob that at least one of the k indices selected
will contain the letter a.

Input: 3 lines.
4           n which is length of list
a a c d     n space separated letters
2           k

Output: single line with probability at least on of k, contains "a"
0.8333
"""

import itertools
import random


def select_k_indices(n, l, k):
    perm = list(itertools.combinations(l, k))
    total = len(perm)
    events = 0
    for el in perm:
        if 'a' in el:
            events += 1

    ran_index = random.randrange(k)
    return events/total


if __name__ == '__main__':
    n = int(input())
    l = list(input().split())
    k = int(input())
    # print(n, l, k)
    print(select_k_indices(n, l, k))

