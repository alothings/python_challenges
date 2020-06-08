"""

Invert a binary tree. The method should swap every left node for its corresponding right node.

"""

def invertBinaryTree(tree):
    # Write your code here.
    q = [tree]
    while len(q) > 0:
        node = q.pop(0)
        swapNodes(node)

        if node.right is not None:
            q.append(node.right)
        if node.left is not None:
            q.append(node.left)

# Recursive
def invertBinaryTree(tree):
    # Write your code here.
    if tree is None:
		return
    swapNodes(tree)
    invertBinaryTree(tree.left)
    invertBinaryTree(tree.right)
	
def swapNodes(tree):
	tree.left, tree.right = tree.right, tree.left

