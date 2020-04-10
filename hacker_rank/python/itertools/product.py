"""

itertools.product(): Computes cartesian product of iterables
* is the "splat" operator for arguments. Takes a list and expands
it into actual positional arguments.

Example:
    product(a,b) = ((x,y) for x in A for y in B)
    
Task: Output space separated tuples of cartesian product
Input: space separated elements of A

print list(product([1,2,3],[3,4]))
[(1, 3), (1, 4), (2, 3), (2, 4), (3, 3), (3, 4)]

A = [[1,2,3],[3,4,5]]
print list(product(*A))
[(1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 3), (3, 4), (3, 5)]

"""
from itertools import product

def cartesian_product(a, b):
    """ a and b are iterables"""
    prod = list(product(a, b))
    return prod

if __name__ == '__main__':
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    # print(a)
    ret = cartesian_product(a, b)
    print(' '.join([str(el) for el in ret]))
