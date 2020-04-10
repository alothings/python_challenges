from helper import Stack

# Given  strings of brackets, determine whether each sequence of brackets is
# balanced. If a string is balanced, print YES on a new line; otherwise,
# print NO on a new line.

def is_matched(expression):
    b = ["(", "{", "["]
    e = [")", "}", "]"]
    if len(expression)%2 != 0:
        return False
    brackets_stack = Stack()
    for char in expression:
        if char in b:
            brackets_stack.push(e[b.index(char)])
        if char in e:
            if char != brackets_stack.peek():
                return False
            brackets_stack.pop()
    return brackets_stack.is_empty()


t = int(input().strip())
for a0 in range(t):
    expression = input().strip()
    if is_matched(expression) == True:
        print("YES")
    else:
        print("NO")