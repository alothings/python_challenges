"""
#####################################################################
Intro:

Task:

Input:

Output:

"""
import numpy as np

if __name__ == '__main__':

    coeff = np.array(input().split(), float)
    x = int(input())
    print(np.polyval(coeff, x))
