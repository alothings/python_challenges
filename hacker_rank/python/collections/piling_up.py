"""

Task: Given a row of n cubes, put them in vertical pile such that
lengh decreases with height.
You can only pick left or right most cube each time.

Input: per lines:
integer T number of test cases
for each test case there are 2 lines
n number of cubes
n space separated integers

Output: Print Yes or No depending whether it is possible or not to
stack the cubes.

"""


def func(n, d):

    i = 0
    j = n-1
    l = []
    while i < j:
        if d[i] > d[j]:
            l.append(d[i])
            i += 1
        else:
            l.append(d[j])
            j -= 1
        if len(l) > 1 and l[-1] > l[-2]:
            # print(l[-1], l[-2])
            return False
    return True

from collections import deque

if __name__ == '__main__':
    trials = int(input())
    for i in range(trials):
        n = int(input())
        d = deque(map(int, input().split()))
        ret = func(n, d)
        print('Yes') if ret else print('No')