"""
#####################################################################
Intro:
- re.findall(): returns all non-overlapping matches of patterns in a 
string as a list of strings.

Example: 
    import re
    re.findall(r'\w','http://www.hackerrank.com/')
    ['h', 't', 't', 'p', 'w', 'w', 'w', 'h', 'a', 'c', 'k', 'e', 'r', 'r', 
    'a', 'n', 'k', 'c', 'o', 'm']
    
- re.finditer() : returns an iterator yielding MatchObject instances over
all non-overlapping matches

Example:
    import re   
    re.finditer(r'\w','http://www.hackerrank.com/')
    <callable-iterator object at 0x0266C790>

Task: Given string S (consists of alphanum char, spaces, and +,-
find all substrings of S that contain 2 or more vowels (only vowels)
must lie between 2 consonants

Input:

Output: Print matched substrings in order of occurrence in diff lines

"""
import re

v = 'aeiou'
c = 'qwrtypsdfghjklzxcvbnm'

if __name__ == '__main__':
    s = input()
    l = re.findall(r"(?<=[%s])([%s]{2,})[%s]" % (c, v, c), s, flags=re.I)
    print('\n'.join(l or ['-1']))




""" Test input:

rabcdeefgyYhFjkIoomnpOeorteeeeet

"""