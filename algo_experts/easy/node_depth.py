"""
Easy
Binary trees

Node's depth: Distance between node and the root
Write a function tat takes a BT and returns the sum of its nodes' depth
"""

# Recursive ########
def nodeDepths(root):
    # Write your code here.
    return breadth_first(root, 0)

def breadth_first(node, depth = 0):
    if node is None: return 0
    return depth + breadth_first(node.left, depth + 1) + breadth_first(node.right, depth + 1)

# Iterative #########
def nodeDepths(root):
    q = [(root, 0)]
    total = 0
    while q:
        print("len: ", len(q))
        node, d = q.pop(0)
        total += d
        if node.left is not None:			
            q.append([node.left, d + 1])
        if node.right is not None:	
            q.append([node.right, d + 1])
        print("node: ", node.value, "depth: ", d)
    print(total)
    return total

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None