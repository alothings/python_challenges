"""
#####################################################################
Intro:

Task: 

Input:

Output:

"""
import re

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print("YES") if re.match(r'[789]\d{9}$', input()) else print("NO")


""" Test input:
2
9587456281
1252478965

"""