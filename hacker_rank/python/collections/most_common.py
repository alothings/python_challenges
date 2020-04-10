"""

Task: Given string S containing only lowercase
find top three most common characters

Input: line containing string

Output:three lines in freq order

"""

from collections import Counter, OrderedDict

class OrderedCounter(Counter, OrderedDict):
    pass


if __name__ == '__main__':
    s = sorted(input())         # sort input
    c = OrderedCounter(s)       # counter in alph order

    l = c.most_common(3)
    for el in l:
        print('{} {}'.format(el[0], el[1]))


"""batch update gnome extensions
aabbbccde
"""