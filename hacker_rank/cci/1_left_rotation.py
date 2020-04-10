# A left rotation operation on an array of size  shifts each of the array's
# elements  unit to the left. For example, if  left rotations are performed
# on array , then the array would become .
# Given an array of  integers and a number, , perform  left rotations on the
# array. Then print the updated array as a single line of space-separated integers.

def array_left_rotation(a, n, k):   # Time O(n), Memory O(n)
    b = []
    for i in range(n):
        b.append(a[(i+k)%n])
    return b

# n, k = map(int, input().strip().split(' '))
# a = list(map(int, input().strip().split(' ')))
# answer = array_left_rotation(a, n, k)
# print(answer, sep=' ')

a = [1, 2, 3, 4, 5]
n = len(a)
k = 2
print(array_left_rotation(a, n, k))