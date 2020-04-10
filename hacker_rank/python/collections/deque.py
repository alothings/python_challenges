"""
Deque: is a double-ended queue. 
Thread safe, memory efficient for appends and pops.
Task: Append, pop, popleft and appendleft on empty deque
Input: by lines:
n containing # of instructions
isntructions and values

Output: print space separated elements of dequeue

"""


from collections import deque


if __name__ == '__main__':
    n = int(input())
    d = deque()
    ops = {'append': d.append, 'pop': d.pop, 'popleft': d.popleft,
           'appendleft': d.appendleft}
    for i in range(n):
        k, *v = input().split()
        if v: v = v[0] # v: print(v, type(v))
        if k in ops:
            ops[k](v) if v else ops[k]()

    print(' '.join(d))
    # print(d)