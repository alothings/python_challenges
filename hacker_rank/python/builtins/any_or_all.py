"""
#####################################################################
Intro:
any() returns True if ANY element of the iterable is true
all() returns True if ALL elements of iterable are true

Task: Given space separated integers. If all ints are positive, 
then check if any int is a palindromic integer

Input: first line is the number if ints
second line is space separated ints

Output: True or False

"""


def is_pal(x):
    x = str(x)
    for i in range(len(x)):
        # print(x[i])
        if x[i] != x[(len(x)-1) - i]: return False
    return True


if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split()))

    if all([x > 0 for x in nums]):
        print(any([is_pal(x) for x in nums]))
    else:
        print(False)




""" Test input:


"""