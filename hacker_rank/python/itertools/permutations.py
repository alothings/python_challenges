"""
itertools.permutations(iterable[,r]): returns successive r length
permutations of elements in an iterable. Default is length of iterable

Task:
Given string s
pring all possible permutations of size k

"""
from itertools import permutations


def print_permutation_order(s, k):
    s = list(s)
    s.sort()
    return list(permutations(s, k))


if __name__ == '__main__':
    s, k = input().split()
    k = int(k)
    ret = print_permutation_order(s, k)
    for el in ret:
        print(''.join(el))

