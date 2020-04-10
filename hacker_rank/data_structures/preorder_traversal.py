class Node:
    def __init__(self, left, right, data):
        self.left = left
        self.right = right
        self.data = data


def preorder(root):
    if root:
        print(root.data, end=" ")       # to print in same line
        preorder(root.left)
        preorder(root.right)


def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(root.data, end=" ")       # to print in same line


def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.data, end=" ")       # to print in same line
        inOrder(root.right)
