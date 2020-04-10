"""
Task: Given n words (some may repeat). for each word output,
its number of occurences.
The output should be in order

Input: n
following n lines contain a word

Output:

"""

from collections import OrderedDict, Counter


class OrderedCounter(Counter, OrderedDict):
    'Counter that remembers the order elements are first encountered'
    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, OrderedDict(self))

    def __reduce__(self):
        return self.__class__, (OrderedDict(self),)

if __name__ == '__main__':
    n = int(input())
    l = []
    for i in range(n):
        l.append(input())
    count = OrderedCounter(l)
    print(len(count))
    print(' '.join(map(str, count.values())))
"""
4
bcdef
abcdefg
bcde
bcdef
"""