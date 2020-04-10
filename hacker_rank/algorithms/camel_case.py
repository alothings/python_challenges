"""##################################################################
Intro:
Alice wrote a sequence of words in CamelCase as a string of letters
S having the following properties:

It is a concatenation of one or more words consisting of English letters.
All letters in the first word are lowercase.
For each of the subsequent words, the first letter is uppercase and
rest of the letters are lowercase.
Given S, print the number of words in  on a new line.

Task: Count number of words in camel case

Input:
saveChangesInTheEditor

Output:
5

"""


def func():
    pass

if __name__ == '__main__':
    s = input()
    count = 1
    for ch in s:
        if ch.isupper(): count += 1
    print(count)
