# Complete the function provided in the editor below. It has
# one parameter: a pointer to a Node object named  that points
# to the head of a linked list. Your function must return a boolean
# denoting whether or not there is a cycle in the list. If there
# is a cycle, return true; otherwise, return false.
# Max list size is 100!!
from helper import LinkedList

# class Node(object):
#     def __init__(self, data=None, next_node=None):
#         self.data = data
#         self.next = next_node

def has_cycle(node):
    max_size = 100
    for i in range(max_size):
        node = node.next
        if not node:
            return False
    return True

ll = LinkedList()
# ll.add_multiple([1,2,3,4,5])
one = ll.add(1)
two = ll.add(2)
three = ll.add(3)
three.next = two

print(has_cycle(ll.head))