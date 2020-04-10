"""

divmod(a,b): returns tuple containing quotient of a/b and remainder
Task:
first line: integer divission od a and b
second line: resilt of modulo operator
third line:print divmod of a and b

Input 
first line: 
"""
import math


def print_div_mod_divmod(a,b):
    div = a // b
    mod = a % b
    divm = divmod(a,b)
    return div, mod, divm


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    p, q, r = print_div_mod_divmod(a, b)
    print(p)
    print(q)
    print(r)

