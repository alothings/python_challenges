# Implementing linkedList in Python

# The Node: stores data, points to next,
class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_nodee

    def set_next(self, new_next):
        self.next_node = new_next

# Linked List: will include methods for insert, size, search, delete
class LinkedList(object):

    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    def search(self, data):
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next
        if current is None:
            raise ValueError("Data not in List")


# ten = Node(1)
# nine = push(ten,9)
# eight = push(nine,8)
# seven = push(eight,7)
# six = push(seven,6)
# five = push(six,5)
# four = push(five,4)
# three = push(four,3)
# two = push(three,2)
# one = push(two,1)



class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def push(head, data):
    n = Node(data)
    n.next = head
    return n

def length(node):   #so I have data and next
    count = 0
    if node == None:
        return 0
    current = node.next
    while current is not None:
        count += 1
        current = current.next
    return count + 1

def get_nth(node, index):
    count = 0
    r = None
    if node == None:
        raise Exception("Node is null")
    if index == 0:
        return node
    if index < 0:
        raise Exception("Invalid index")
    current = node.next
    while current is not None and count <= index:
        count += 1
        if (count == index):
            r = current     #r = current.data
        current = current.next
    if current is None and r == None:
        raise Exception("index not found")
    return r

def insert_nth(head,index,data):
    if index > length(head):
        print "index: ",index, "length: ",length
        raise Exception("index is too large")
    if index == 0: return Node(data, head)
    c = head
    result = head
    if head and index >0:
        for i in range(index-1):
            c = c.next
        new_c = push(c.next,data)
        c.next = new_c
    return result.data

































