"""##################################################################
Intro:
Alice and Bob each created one problem for HackerRank. A reviewer 
rates the two challenges, awarding points on a scale from 1 to 100
for 3 categories: problem clarity, originality, and difficulty.

Alice and Bobs challenge:
A = (a0, a1, a2)
B = (b0, b1, b2)

for each attribute if ai > bi Alice +1 point
for each attribute if ai < bi Bob +1 point
if ai = bi, then no one receives a point

Task: Given A and B, print comparison points

Input:
5 6 7
3 6 10

Output:
1 1

"""
import sys


# def solve(a0, a1, a2, b0, b1, b2):
def solve(a, b):
    a_points = 0
    b_points = 0
    for i in range(len(a)):
        if a[i] > b[i]: a_points += 1
        if a[i] < b[i]: b_points += 1
    return a_points, b_points

    pass

if __name__ == '__main__':
    # a0, a1, a2 = map(int, input().strip().split(' '))
    # b0, b1, b2 = map(int, input().strip().split(' '))
    a = list(map(int, input().strip().split(' ')))
    b = list(map(int, input().strip().split(' ')))
    result = solve(a, b)
    print(" ".join(map(str, result)))
    # print(a0, a1, a2)