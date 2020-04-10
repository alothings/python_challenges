"""
#####################################################################
Intro:

Task: Given string N, verify n is a floating point number
can start with +, - or .
must containg at least 1 decimal value. like 12.0, not 12.
must have exactly one .
must not give exceptions when float(n)

Input:

Output:

"""
import re

def is_float(s):
    try:
        n = float(s)
    except:
        return False
    # print(s, type(s))
    match = re.search(r'\.[0-9]+', s)
    return match is not None

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        print(is_float(input()))


""" Test input:


"""