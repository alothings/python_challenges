"""
itertools.groupby(): 

Group consecutive numbers in tuples... Stupid explanation

Input: line of the string S
Output: Line of modified string

1222311
(1, 1) (3, 2) (1, 3) (2, 1)

(x, c)

"""
from itertools import groupby


def group_string(s):
    return ' '.join([str((len(list(g)), int(k)))for k,g in groupby(s)])


if __name__ == '__main__':
    print(group_string(input()))