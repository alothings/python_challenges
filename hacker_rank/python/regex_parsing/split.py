"""
#####################################################################
Intro: re.split() splits the string by occurrence of a pattern

Task: Given s containing [, . 0-9]
split by , and .

Input:

Output:

"""
import re

if __name__ == '__main__':
    s = input()
    l = re.split(r'[,.]+', s)
    print(*filter(None, l), sep='\n')


""" Test input:
100,000,000.000
1,2.3,4.5,
1,.,,.2
"""