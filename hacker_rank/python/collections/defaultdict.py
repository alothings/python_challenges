"""
defaultdict: container similar to dict but values fields is specified 
upon initialization. Whenever we want collections as values.

Example:
from collections import defaultdict
d = defaultdict(list)

Task: Given int n and m. There are n words, which might repeat, in a word
group A.
There are m words belonging to word group B. For each m words, check whether
the words has appeared in group A.
Print indices of each occurrence of m in group A. If it does not
appear, print -1.

Input: lines:
1 integers n and m separated by whitespace
2 n lines containing words belonging to A
3 m lines containing words belonging to B

Output:

"""


def func():
    pass

from collections import defaultdict

if __name__ == '__main__':
    n, m = map(int, input().split())
    sets = defaultdict(list)
    for _i in range(n):
        sets['a'].append(input())

    res = defaultdict(list)
    setb = []

    for _i in range(m):
        setb.append(input())

    for _i in range(len(setb)):
        isthere = False
        for _j in range(len(sets['a'])):
            if setb[_i] == sets['a'][_j]:
                isthere = True
                res[_i].append(_j + 1)
        if not isthere:
            res[_i].append(-1)

    for k in res.keys():
        print(' '.join(map(str,res[k])))

"""
Smarter way
n, m = map(int,raw_input().split())

for i in range(0,n):
    d[raw_input()].append(i+1) 

for i in range(0,m):
    list1=list1+[raw_input()]  

for i in list1: 
    if i in d:
        print " ".join( map(str,d[i]) )
    else:
        print -1
        
"""






