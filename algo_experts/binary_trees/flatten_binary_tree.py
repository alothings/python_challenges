"""

"""

# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# Easy solution. time O(N), space O(N)
def flattenBinaryTree(root):
    # Write your code here.
    flat = inorder(root, [])
    for i in range(len(flat) - 1):
		left = flat[i]
		right = flat[i + 1]
		left.right = right
		right.left = left
    return flat[0]
        
def inorder(node, arr):
	if node is not None:
		inorder(node.left, arr)
		arr.append(node)
		inorder(node.right, arr)
	return arr


# Optimal Solution. Time O(N), Space O(depth)
def flattenBinaryTree(root):
    # Write your code here.
    leftMost, _ = flattenTree(root)
    return leftMost

def flattenTree(node):
    if node.left is None:
        leftMost = node
    else:
        leftSubtreeLeftMost, leftSubtreeRightMost = flattenTree(node.left)
        connectNodes(leftSubtreeRightMost, node)
        leftMost = leftSubtreeLeftMost 

    if node.right is None:
        rightMost = node
    else:
        rightSubtreeLeftMost, rightSubtreeRightMost = flattenTree(node.right)
        connectNodes(node, rightSubtreeLeftMost)
        rightMost = rightSubtreeRightMost

    return [leftMost, rightMost]

def connectNodes(left, right):
    left.right = right
    right.left = left