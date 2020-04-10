"""
Given string S
print all combinations UP TO size k
"""

from itertools import combinations


def print_combination(s, k):
    s = list(s)
    s.sort()
    ret = ()
    for i in range(1, k + 1):
        ret += tuple(combinations(s, i))
    return ret


if __name__ == '__main__':
    s, k = input().split()
    k = int(k)
    ret = print_combination(s, k)
    for el in ret:
        print(''.join(el))