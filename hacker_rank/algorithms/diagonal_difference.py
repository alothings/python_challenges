"""
Given square matrix of size NxN. Calculate absolute difference
between the sum of diagonals

"""

import sys


# n = int(input().strip())
# a = []
# for a_i in range(n):
#     a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
#     a.append(a_t)

a = [[11, 2, 4],
     [4, 5, 6],
     [10, 8, -12]]

def diagonal_difference(matrix):
    n = len(matrix)             # Getting the NxN value
    # Method 1: start diagonals in lists, and perform operation
    # Method 2: subtract during loop
    first_diag = 0
    second_diag = 0
    for i in range(n):
        first_diag += matrix[i][i]
        second_diag += matrix[i][n-i-1]
    return abs(first_diag-second_diag)

print(diagonal_difference(a))
