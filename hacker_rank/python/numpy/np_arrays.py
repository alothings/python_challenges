"""
#####################################################################
Intro: NumPy = Numeric Python
Helps manipulate large arrays and matrices
usage: import numpy

Task: Given space separated list of numbers, 
print a reversed np array with type float

Input:
1 2 3 4 -8 -10

Output:
[-10.  -8.   4.   3.   2.   1.]

"""
import numpy as np

if __name__ == '__main__':
    l = np.array(input().split(), dtype=float)
    print(l[::-1])


""" Test input:


"""