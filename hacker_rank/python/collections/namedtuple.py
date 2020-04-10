"""
Named tuples: assign meaning to each position for more readable/self
documenting code.

Point = namedtuple('Point', ['x', 'y'])
p = Point(11, y=22)


Task: Given spreadsheet containing list of students:
ids, marks, class, name
calculate average marks of students. 

Input: lines in order:
n the total number of students
names of the columns in any order
following n lines contain: marks, ids, name and class in the order
mentioned above.

Output: Print average   

"""
from collections import namedtuple

def func():
    pass


if __name__ == '__main__':
    num_students = int(input())
    col_names = input().split()
    # print(num_students, col_names)
    # print(type(col_names))

    Records = namedtuple('Records', col_names)
    total = 0
    for i in range(num_students):
        t = Records(*input().split())
        total += int(t.MARKS)

    print(total/num_students)

"""
5
ID         MARKS      NAME       CLASS     
1          97         Raymond    7         
2          50         Steven     4         
3          91         Adrian     9         
4          72         Stewart    5         
5          80         Peter      6   
"""
