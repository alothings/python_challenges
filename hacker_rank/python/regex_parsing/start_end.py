"""
#####################################################################
Intro:
start() and end() return indices of the start and end of the substring 
matched.

Example:
    import re
    m = re.search(r'\d+','1234')
    m.end()
     4
    m.start()
     0

Task: Given string S, find indices of start and end of string K in S

Input: first line S, second line K

Output:

"""
import re


def func():
    pass


if __name__ == '__main__':
    s = input()
    k = input()
    l = []
    pattern = re.compile(k)
    m = pattern.search(s)
    if not m: print("(-1, -1)")

    while m:
        print("({}, {})".format(m.start(), m.end() - 1))
        m = pattern.search(s, m.start() + 1)


    # print(m)
    # print(m.end())


""" Test input:
aaadaa
aa

"""