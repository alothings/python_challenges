"""
#####################################################################
Intro: zip(*iterables) 
Makes an iterator that aggregates elements from each of the iterables
RETURNS an iterator of tuples. the ith tuple contains the ith element
from each of the arguments.
It truncates at the shortest input iterable.
Example:
    x = [1, 2, 3]
    y = [4, 5, 6]
    zipped = zip(x, y)
    list(zipped)
    [(1, 4), (2, 5), (3, 6)]

Task: n students, x subjects. Compute average score of each student
avg = sum(scores in subjects)/ total subjects

Input: by lines:
n and x separated by space
next x lines contains marks of each student

Output: return average of each student

"""


def func():
    pass


if __name__ == '__main__':
    n, x = map(int, input().split())
    subs = []
    avgs = []
    for i in range(x):
        subs.append(list(map(float, input().split())))
    for student in zip(*subs):
        print(*student)
        avgs.append(sum(student)/x)
    print('\n'.join(map(str, avgs)))

""" Test input:
5 3
89 90 78 93 80
90 91 85 88 86  
91 92 83 89 90.5

"""