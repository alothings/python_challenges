"""
#####################################################################
Intro:

Task:

Input:

Output:

"""
import numpy as np

def func():
    pass


if __name__ == '__main__':
    # n = input()
    A = np.array(input().split(), int)
    B = np.array(input().split(), int)
    print(np.inner(A,B), np.outer(A,B), sep='\n')
