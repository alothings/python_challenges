# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
def findClosestValueInBst(tree, target):
    # Write your code here.
    return dfs(tree, target, tree.value)
    

def dfs(node, target, current_closest, min_diff):
    # Traverse tree, keep min_diff and current_closest stored
    # Traverse until node.l is none if target is less, or node.r is none else
    current_difference = abs(node.value - target)
    if current_difference == 0:
        current_closest = node.value
        return current_closest

    if current_difference < min_diff:
        min_diff = current_difference
        current_closest = node.value
    

    if target < node.value:
        if node.left:
            current_closest = dfs(node.left, target, current_closest, min_diff)
        else:
            return current_closest
    
    if target > node.value:
        if node.right:
            current_closest = dfs(node.right, target, current_closest, min_diff)
        else:
            return current_closest
    return current_closest

# RECURSIVE uses too much space
# Average Time O(log(n)), worst O(n)
# Average Space O(log(n)), worst O(n)
def dfs(node, target, closest):
    # Traverse tree, keep min_diff and current_closest stored
    # Traverse until node.l is none if target is less, or node.r is none else
    if node is None:
        return closest
    
    if abs(node.value - target) == 0:
        closest = node.value
        return closest

    if abs(closest - target) > abs(node.value - target):
        closest = node.value

    if target < node.value:
        return dfs(node.left, target, closest)
    
    if target > node.value:
        return dfs(node.right, target, closest)
    return closest

# LOOP:

# Average Time O(log(n)), worst O(n)
# Average Space O(1), worst O(1)
def dfs(node, target, closest):
    # Traverse tree, keep min_diff and current_closest stored

    current_node = node
    while current_node is not None:
        if abs(closest - target) > abs(current_node.value - target):
            closest = current_node.value

        if target < current_node.value:
            current_node = current_node.left            
        elif target > current_node.value:
            current_node = current_node.right
        else:
            break
    return closest