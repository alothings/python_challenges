#!/bin/python3

'''
Day 23: BST Level Order Traversal
Level Order Traversal (aka Breadth-first traversal) visits each node from
left to right, top to bottom.


Depth-First: First visits node "a", then iterates over its neighbors. When
visits node "b", which is a neighbor of "a", it visits all of "b"s neighbors,
before continuing with "a's neighbors.

Breath-First: Visits node "a" and all of it's neighbors before visiting any
of the neighbors of "a"s neighbors. Uses a "queue"
'''

import queue

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data


class Solution:
    def insert(self, root, data):
        if root is None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self, root):
        self.q = queue.Queue()
        if root is None:
            return
        self.q.put(root)
        while not self.q.empty():
            # pop from queue to visit node. enqueue its children
            temp = self.q.get()         # pop first element in queue
            print(temp.data, end=" ")   # visit (print) first element in queue
            if temp.left is not None:
                self.q.put(temp.left)   # enqueue left child if it exist
            if temp.right is not None:
                self.q.put(temp.right)  # enqueue right child if it exists

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)