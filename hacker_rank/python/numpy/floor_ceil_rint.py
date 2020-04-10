"""
#####################################################################
Intro:

Task:

Input:
1.1 2.2 3.3 4.4 5.5 6.6 7.7 8.8 9.9


Output:

"""
import numpy as np

if __name__ == '__main__':
    # n = input()
    A = np.array((input().split()), float)
    print(np.floor(A), np.ceil(A), np.rint(A), sep='\n')


