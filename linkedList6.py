class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def push(head, data):
    n = Node(data)
    n.next = head
    return n

def length(node):   #so I have data and next
    l = 0
    if node == None:
        return 0
    current = node.next
    while current is not None:
        l += 1
        current = current.next
    return l + 1

def print_list(node):
    c = node
    count = 0
    print "Beginning Printing List: \n"
    while c is not None:
        print c.data
        c = c.next
        count += 1
        if count > 15:
            break
    print "Done Printing List"

# Insert data in linked list node with index=index.
def insert_nth(head,index,data):
    if index > length(head):
        raise Exception("index is too large")
    if head is None:
        return Node(data)
    c = head
    result = head
    if head and index > 0:
        for i in range(index-1):
            c = c.next
        new_c = push(c.next,data)
        c.next = new_c
    elif index == 0:
        n = Node(data)    #Creating new node to be inserted
        n.next = result   #Pointing head of node to main list
        return n
    return result

ten = Node(10)
seven = push(ten,7)
six = push(seven,6)
five = push(six,5)
four = push(five,4)

# ten = Node(10)
eleven = Node(1)
three = push(eleven,2)
two = push(three,3)
one = push(two,4)


# print_list(one)
# print "\n",
# one = insert_nth(one,1,12)
# print_list(one)

#------------------------------------------------------------
#Linked List - Append
#Append one linked list to another
def append(listA, listB):
    if listA == None:
        return listB
    elif listB == None:
        return listA
    headA = listA
    headB = listB
    cA = headA
    cB = headB
    count = 0
    while cA.next is not None:
        count += 1
        cA = cA.next
    cA.next = push(cB.next, cB.data)
    return headA

# print_list(one)
# print_list(four)
# append(one,four)
# print_list(one)

#-------------------------------------------------------
# Linked Lists - Sorted Insert
# Insert node in sorted list. Where it corresponds.
def sorted_insert(head, data):
    result = head
    if head == None:
        return push(head,data)
    if head > 0:
        list = head
        c = head
        t = head.next
        count = 0
        while t is not None:
            if data < c.data:
                return insert_nth(list,count,data)
            elif data >= c.data and data < t.data:
                insert_nth(list,count+1,data)
                return result
            count += 1
            c = c.next
            t = t.next
        if data > c.data:
            insert_nth(list,count+1,data)
    return result
#------------------------------------------------------------
#Linked List - Insert Sort
#Sort nodes in increasing order
#uses: Node, push, insert_nth
def insert_sort(head):
    n = length(head)
    c = head
    t = head
    sortedList = c              #sortedList = Head
    c = c.next                  #c = head.next
    sortedList.next = None      #sortedList.next = None
    n = length(head)
    if head == None or n == 1:
        return head

    return c

eleven = Node(1)
four1 = push(eleven, 3)
three1 = push(four1, 4)
two1 = push(three1,2)
one1 = push(two1,5)
#
# print_list(one1)
# n = insert_sort(one1)
# print_list(n)