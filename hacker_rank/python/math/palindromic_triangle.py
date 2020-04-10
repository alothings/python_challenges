"""
Given a positive integer N
print a palindromic triangle fo size N

Example: N = 5
1
121
12321
1234321
123454321

Note: Complete tasks in 2 lines
"""


# def print_palindromic_triangle(n):
#
#     pass
#
#
# if __name__ == '__main__':
#     ab = int(input())
#     bc = int(input())

for i in range(1,int(input())+1):
    print(((10**i -1)//9)**2)