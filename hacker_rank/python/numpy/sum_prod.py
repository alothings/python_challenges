"""
#####################################################################
Intro:

Task:
You are given a 2-D array with dimensions NxM. 
Your task is to perform the SUM tool over axis 0 and 
then find the PRODUCT of that result.
Input:

Output:

"""

import numpy
if __name__ == '__main__':
    # n = input()
    N, M = map(int, input().split())
    A = numpy.array([input().split() for _ in range(N)],int)
    print(numpy.prod(numpy.sum(A, axis=0), axis=0))
