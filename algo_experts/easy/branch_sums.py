"""
Easy
Binary trees

Write a function that takes in a binary tree and returns a list of its branch
 sums ordered from leftmost branc sum to rightmost branch sum.


"""

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def branchSums(root):
    # Write your code here.
    branch = []
    traverse(root, 0, branch)
    # print(branch)
    return branch

def traverse(root, sums, branch):
    if root is not None:
        sums += root.value
    # print(root.value, " ", sums)
        if root.left is None and root.right is None:
            branch.append(sums)
        traverse(root.left, sums, branch)
        traverse(root.right, sums, branch)

# print("branch_sums")