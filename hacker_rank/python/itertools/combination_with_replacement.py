"""
#####################################################################
Intro:
itertools.combinations_with_replacement(iterable, r) 
This tool returns R length subsequences of elements from the input
iterable allowing individual elements to be repeated more than once.

Sample:
    from itertools import combinations_with_replacement 
    print list(combinations_with_replacement('12345',2))
[('1', '1'), ('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'), 
('2', '2'), ('2', '3'), ('2', '4'), ('2', '5'), ('3', '3'), 
('3', '4'), ('3', '5'), ('4', '4'), ('4', '5'), ('5', '5')]
    
    A = [1,1,3,3,3]
    print list(combinations(A,2))
[(1, 1), (1, 3), (1, 3), (1, 3), (1, 3), (1, 3), (1, 3), (3, 3), (3, 3), (3, 3)]

Task:
You are given a string S
Your task is to print all possible size K replacement
combinations of the string in lexicographic sorted order.
Input:

Output:

"""
from itertools import combinations_with_replacement as combs

if __name__ == '__main__':
    s, k = input().split()
    print(*[''.join(p) for p in combs(sorted(s), int(k))], sep='\n')

""" Test input:


"""