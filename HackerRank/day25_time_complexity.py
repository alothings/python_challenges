'''
Day 25: Running time and complexity
Given a number n, determine whether it's prime or not.
'''
import math

def isPrime(n):
    if n == 1:
        return("Not prime")
    if n > 2 and n%2 == 0:
        return("Not prime")
    elif n > 3 and n%3 == 0:
        return("Not prime")
    else:
        for i in range (3, int(math.sqrt(n)) + 1, 2):
        # for i in range (3, n ,2):
            # print(i)
            if n % i == 0:
                return("Not prime")
    return("Prime")


T=int(input())
for i in range(T):
    num = int(input())
    print(isPrime(num))
