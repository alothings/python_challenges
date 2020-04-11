"""
Three number sum.

Write a function that takes a non-empty array of distinct integers and an integer 
representing a target sum. Function should find all triplets in the array that 
sum up to the target. return a 2-d array of these triplets.
Numbers in each triplet should be in ascending order, and triplets themselves
should also be in ascending order

Space complexity:
Time complexity:
"""


def three_number_sum(array, targetSum):
    a = sorted(array)
    n = len(a)
    result = []
    for i in range(0, n-2):
        l_runner = i+1
        r_runner = n-1
        while l_runner < r_runner:
            if a[i] + a[l_runner] + a[r_runner] > targetSum:
                r_runner = r_runner - 1
            else:
                if a[i] + a[l_runner] + a[r_runner] == targetSum:
                    result.append([a[i], a[l_runner], a[r_runner]])
                l_runner = l_runner + 1
    return result

arr = [12, 3, 1, 2, -6, 5, -8, 6]
print(three_number_sum(arr, 0))



