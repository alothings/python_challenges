"""
#####################################################################
Intro: Regex Substitution
re.sub(pattern, repl, string, count=0, flags=0) : evaluates pattern and for 
repl can be a string or function. 
re.sub(pattern, 'def myfunc(): ', string)
re.sub(pattern, myfun, string)


Task: Given n lines, the text contains && and || symbols.
Modify those to "and" and "or"

Input: first line contains integer n
next n lines contain text

Output:

"""
import re

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        line = input()
        m = re.sub(r'(?<= )(&&|\|\|)(?= )', lambda x: 'and' if x.group() == '&&'
                   else 'or', line)
        print(m)


""" Test input:
11
a = 1;
b = input();

if a + b > 0 && a - b < 0:
    start()
elif a*b > 10 || a/b < 1:
    stop()
print set(list(a)) | set(list(b)) 
#Note do not change &&& or ||| or & or |
#Only change those '&&' which have s11
a = 1;
b = input();

if a + b > 0 && a - b < 0:
    start()
elif a*b > 10 || a/b < 1:
    stop()
print set(list(a)) | set(list(b)) 
#Note do not change &&& or ||| or & or |
#Only change those '&&' which have space on both sides.
#Only change those '|| which have space on both sides.pace on both sides.
#Only change those '|| which have space on both sides.

"""