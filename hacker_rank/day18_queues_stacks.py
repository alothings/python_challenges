#!/bin/python3

'''
Day 18: Stacks and Queues
Goal: Check if word is a palindrome

'''

import sys

class Solution:
    def __init__(self):
        # Should contain stack and queue? initialize empty
        #in python the solution is much simpler though, because a list is a linked list
        #so we can compare elements starting from begining and end.
        self.stack = []
        self.queue = []

    def pushCharacter(self, el):
        # Push el to stack
        self.stack.append(el)

    def popCharacter(self):
        # Push el to stack
        print("Popping: {}".format(self.stack[-1]))
        if len(self.stack) > 0:
            return self.stack.pop(-1)

    def enqueueCharacter(self, el):
        # Enqueue el to queue
        self.queue.append(el)


    def dequeueCharacter(self):
        # Enqueue el to queue
        if len(self.queue) > 0:
            print("Dequeueing: {}".format(self.stack[0]))
            return self.queue.pop(0)



# read the string s
s = input()
# Create the Solution class object
obj = Solution()

l = len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

# print("Stack {}".format(obj.stack))
# print("Queue {}".format(obj.queue))
isPalindrome = True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
'''
for i in range(l//2):
    print("Stack {}".format(obj.stack))
    print("Queue {}".format(obj.queue))
    if obj.popCharacter() != obj.dequeueCharacter():
        print("INSIDE IF")
        isPalindrome = False
        break
# finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, " + s + ", is a palindrome.")
else:
    print("The word, " + s + ", is not a palindrome.")