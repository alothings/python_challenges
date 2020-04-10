"""
#####################################################################
Intro:

Task:

Input:
3 3 3

Output:

"""
import numpy as np

def func():
    pass


if __name__ == '__main__':
    n = tuple(map(int, input().split()))
    # print(n)
    z = np.zeros(n, dtype=np.int)
    o = np.ones(n, dtype=np.int)
    print(z)
    print(o)


