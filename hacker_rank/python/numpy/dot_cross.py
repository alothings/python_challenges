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
    n=int(input())
    a = [list(map(int,input().split())) for _ in range(n*2)]
    print (numpy.dot(a[:n],a[n:]))

