"""

Task: Given 2 timestamps, print absolute difference. Timestamps
are in the format:
Day dd Mon yyyy hh:mm:ss +xxxx

Input: per lines:
n number of test cases
next lines are the timestamps

Output: absolute difference in seconds

"""

from datetime import datetime

if __name__ == '__main__':
    n = int(input())

    for i in range(n):
        t1 = datetime.strptime(input(), '%a %d %b %Y %H:%M:%S %z')
        t2 = datetime.strptime(input(), '%a %d %b %Y %H:%M:%S %z')
        delta = int(abs((t1 - t2).total_seconds()))
        # print(t1, t2)
        print(delta)