"""
#####################################################################
Intro:

Task:

Input:

Output:

"""
import re
import email.utils

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        s = email.utils.parseaddr(input())
        if re.search(r'^[a-z0-9][\w._-]+\@[a-z]+\.[a-z]{1,3}$', s[1]):
            print(email.utils.formataddr(s))


""" Test input:
2  
DEXTER <dexter@hotmail.com>
VIRUS <virus!@variable.:p>

"""