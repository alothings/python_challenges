"""
#####################################################################
Intro:

Task:

Input:

Output:

"""
import numpy

if __name__ == '__main__':
    # n = input()
    N, M = map(int, input().split())
    A = numpy.array([input().split() for _ in range(N)],int)
    print(numpy.max(numpy.min(A, axis=1), axis=0))


