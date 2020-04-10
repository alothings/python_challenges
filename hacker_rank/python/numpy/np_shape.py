"""
#####################################################################
Intro:

Task: givn a space separated list of integers, convert in
3x3 np array

Input:
1 2 3 4 5 6 7 8 9

Output:
[[1 2 3]
 [4 5 6]
 [7 8 9]]

"""
import numpy as np

if __name__ == '__main__':
    n = np.array(list(map(int, input().split()))).reshape(3, 3)
    print(n)



""" Test input:


"""