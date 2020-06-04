"""
Given 2 non empty arrays og ints, determine whether the second array is a subsequence of the first

subsequence: Arent necessarily adjacent in the array, but are in the same order as they appear.
"""

a = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]
# output: true

def isValidSubsequence(array, sequence):
    size = len(array)
    ri = 0
    for el in sequence:
        while ri < size and array[ri] != el:
            ri += 1
        if ri == size:
            return False
        ri += 1
    return True

print(isValidSubsequence(a, sequence))

