#!/bin/python3
import sys

'''
Day 22: Binary Search Trees BSTs
BTS:
- Is a binary tree, each node has 0 to 2 children
- All children in left <= node < All children in right

Task: Height or level of a binary search tree
Given a pointer 'root', complete a 'getHeight' method.
'''

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data


class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    count = 0
    def getHeight(self, root):
        if root==None:
            return -1
        else:
            left_height = self.getHeight(root.left)
            right_height = self.getHeight(root.right)
            return max(left_height, right_height) + 1

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height)
