import itertools


def func(nums):
    return sum(x*x for x in nums) % m


def maximize_function(n, l, m):
    """ maximize k^2 + k2^2 % m"""
    prod = list(itertools.product(*l))
    return max(list(map(func, prod)))

if __name__ == '__main__':
    k, m = map(int, input().split())
    l = []
    for i in range(k):
        # l.append(list(input().split()))
        l.append([int(x) for x in input().split()][1:])
    # print(k, m)
    # print(l, len(l))
    print(maximize_function(k,l,m))

"""
3 100
2 5 4
3 7 8 9 
5 5 7 8 9 10 
"""