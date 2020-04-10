"""
#####################################################################
Intro:

Task:

Input: by lines:
n: number of rational numbers
the ith of next n lines contains 2 integers each. Numerator and
denominator.

Output: Print one line containing numerator and denominator of the
 product

"""
from fractions import Fraction
from functools import reduce


def product(fracs):
    t = reduce(lambda x, y: x*y, fracs)
    return t.numerator, t.denominator


if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)


""" Test input:


"""