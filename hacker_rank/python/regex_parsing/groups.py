"""
#####################################################################
Intro:
group(): Retruns one or more subgroups of the match
groups(): returns a tuple containing all subgroups of match
groupdict(): returns dictionary containing named subgroups of the match,
    keyed by subgroup name. 
    
    Example:
    m = re.match(r'(?P<user>\w+)@(?P<website>\w+)\.(?P<extension>\w+)','myname@hackerrank.com')
    m.groupdict()
    {'website': 'hackerrank', 'user': 'myname', 'extension': 'com'}
    
Task: Given string S, find the first occurrence of an alphanumeric char in S
that has consecutive repetitions.

Input: Single line

Output:

"""
import re

def func():
    pass


if __name__ == '__main__':
    # s = input()
    m = re.search(r'([a-zA-Z0-9])\1+', input())
    print(m.group(1)) if m else print(-1)
    # print(s, type(s))

""" Test input:


"""