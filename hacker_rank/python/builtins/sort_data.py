"""
#####################################################################
Intro:

Task: Given n rows and m space separated elements
n can be the sample number and m the characteristic. Like height,
weight, etc.
your task is to sort the table on the lth attribute.

Input: by lines:
n and m separated by space
next n lines contain m elements
last line contains k

Output:

"""


def func(row):
    return int(row.split()[k])


if __name__ == '__main__':
    n, m = map(int, input().split())
    rows = [input() for _ in range(n)]
    k = int(input())

    # for row in sorted(rows, key=lambda row: int(row.split()[k])):
    for row in sorted(rows, key=func):
        print(row)

""" Test input:
row for row in rows

"""