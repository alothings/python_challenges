"""##################################################################
Intro:
Clothing store sales socks. Each i sock, has ci color.

Task: Count number of pairs such that ci = cj.

Input: # of socks and colors of socks.
9
10 20 20 10 10 30 50 10 20

Output: Print total number of matching pairs
3

10 2
20 2
30 0
50 0
counter
for v in d.keys():
    if v%2 == 0: 
        counter += v-1
        
10

"""
from collections import Counter


def func():
    pass

if __name__ == '__main__':
    n = int(input())
    socks = Counter(input().split())
    print(sum(map(lambda x: x//2, socks.values())))

