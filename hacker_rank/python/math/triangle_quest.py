"""
Given positive integer N
Print numerical triangle of height N-1

1
22
333
4444
"""

for i in range(1, int(input())):
    print(((10**i - 1)//9 )* i)
