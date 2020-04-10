"""
#####################################################################
Intro: Using map and lambda

Task: Find first n fibonacci numbers and return a list containing
the cubes of each number

Input: an integer n

Output: a list on a single line containing cubes of first N
fibonacci numbers

"""


def fib(n):
    nums = [0, 1, 1]
    if n == 0: return []
    if n < 3: return nums[:n]
    for i in range(3, n):
        nums.append(nums[i-2] + nums[i-1])
    return nums


if __name__ == '__main__':
    n = int(input())
    print(list(map(lambda x: x**3, fib(n))))


""" Test input:
cube = lambda x: # complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers

"""