""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""
from helper import TreeNode

def check_binary_search_tree_(root):
    pass

def post_order(root):
    if root:
        post_order(root.left)
        post_order(root.right)
        visit(root)

def visit(root):
    return root.data

l = [1, 2, 3, 5, 6]
root = TreeNode(4)

for el in l:
    root.insert(el)

print(root.in_order())


