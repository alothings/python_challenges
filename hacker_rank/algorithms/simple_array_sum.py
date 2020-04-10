"""
Find sum of elements..

"""


import sys

# n = int(input().strip())
# arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

arr = [1, 2, 3, 4, 10, 11]


def find_sum(arr):
    size = len(arr)
    res = 0
    for i in range(int((size+1)/2)):
        # print(i)
        if i != size-i-1:
            res += (arr[i] + arr[size-i-1])
        else:
            res += arr[i]
    return res

print(find_sum(arr))