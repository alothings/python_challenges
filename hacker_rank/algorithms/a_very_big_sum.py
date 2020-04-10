"""
Sum elements in array keeping in mind some integers are large

"""

arr = [1000000001, 1000000002, 1000000003, 1000000004, 1000000005]

def sum_large_num(arr):
    size = len(arr)
    res = 0
    for i in range(int((size + 1) / 2)):
        # print(i)
        if i != size - i - 1:
            res += (arr[i] + arr[size - i - 1])
        else:
            res += arr[i]
    return res

print(sum_large_num(arr))