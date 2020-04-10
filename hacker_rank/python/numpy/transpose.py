"""##################################################################
Intro: 

Task: Given matrix, print transpose and flatten results

Input:
2 2
1 2
3 4

Output:

"""
import numpy as np

if __name__ == '__main__':
    n, m = map(int, input().split())
    mat = np.array([list(map(int, input().split())) for row
                    in range(n)])
    print(mat.transpose())
    print(mat.flatten())
