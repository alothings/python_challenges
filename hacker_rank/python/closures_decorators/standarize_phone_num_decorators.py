"""
#####################################################################
Intro:
Let's dive into decorators! You are given N mobile numbers. Sort them
 in ascending order then print them in the standard format shown below:
 
 +91 xxxx xxxxx
 Can start with +91, 91, or 0 but output should be 91
 
Task:

Input: First line n number of numbers
n containing phone numbers


Output:

"""


def wrapper(f):
    def func_wrapper(l):
        new_l = []
        for el in l:
            s = str(el)
            new_s = '+91 ' + s[-10:-5] + ' ' + s[-5:]
            new_l.append(new_s)
        return f(new_l)
    return func_wrapper

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)


""" Test input:


"""