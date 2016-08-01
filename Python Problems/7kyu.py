#Jaden Casing Strings
# Capitalize first letter of every word in string.
def toJadenCase(string):
    return string.title()

#print toJadenCase("hello there buddy")

# ANother way
def toJadenCase1(string):
    phrase = string.split()
    myList = []
    for words in phrase:
        words = words.capitalize()
        myList.append(words)
    s = ' '.join(myList)
    return s
#print toJadenCase1("hello there buddy")

#------------------------------
# List to Array
#
#u = LinkedList(4, LinkedList(25, LinkedList(30)))
def list_to_array(lst):
    arr = []
    while lst != None:
        arr.append(lst.value)
        lst = lst.next
    return arr

#print list_to_array(u)

#------------------------------------------------------
# Credit Card Mask
# Mask your information! except last 4 digits
def maskify(cc):
    l = list(cc)
    if len(l) <= 4:
        return cc
    else:
        for i in range(0,len(l)-4):
            l[i] = "#"
        cc = ''.join(l)
    return cc

# a = '123'
# b = '1234567'
# print maskify(a)
# print maskify(b)
#

#-------------------------------------------------------
# Linked Lists - Push & Build one two three
# Write push() and buildOneTwoThree()

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def push(head, data):
    n = Node(data)
    n.next = head
    return n

def build_one_two_three():
    # Your code goes here.
    #return push(push(Node(3), 2), 1)
    three = Node(3)
    two = push(three,2)
    return push(two,1)

ten = Node(10)
nine = push(ten,9)
eight = push(nine,8)
seven = push(eight,7)
six = push(seven,6)
five = push(six,5)
four = push(five,4)
three = push(four,3)
two = push(three,2)
one = push(two,1)

#zero = push(two,1)
# 3,None -> 2, three ->
#-------------------------------------------------------
# Linked Lists - Length & Count
# Implement length: count # of nodes
# Implement Count: count occurrences of an integer in a linked list.
def length(node):   #so I have data and next
    l = 0
    if node == None:
        return 0
    current = node.next
    while current is not None:
        l += 1
        current = current.next
    return l + 1
# print length(one)
# print length(None)

def count(node, data):   #so I have data and next
    count = 0
    if node == None:
        return 0
    if node.data == data:
            count += 1
    current = node.next
    while current is not None:
        if current.data == data:
            count += 1
        current = current.next
    return count

#print count(one,1)

#-------------------------------------------------------
# Linked Lists - Get Nth Node
# Returns data given index
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
    # return r
    return r.data

# print get_nth(one,0)
# # print get_nth(one,1)
# # print get_nth(one,2)
# # print get_nth(one,3)
# # print get_nth(one,4)
# # print get_nth(one,5)
# # print get_nth(one,6)
# # print get_nth(one,7)
# print get_nth(one,8)
# print get_nth(one,9)
# print get_nth(one,10)
# print get_nth(one,11)
#print get_nth(None, 0)


#-------------------------------------------------------
# Linked Lists - Insert Nth
# Insert new node at any index within a list
# More General than Push()

def insert_nth(head,index,data):
    if index > length(head):
        raise Exception("index is too large")
    if head is None:
        return Node(data)
    c = head
    result = head
    if head and index > 0:
        print "SUP"
        for i in range(index-1):
            c = c.next
        new_c = push(c.next,data)
        c.next = new_c
    elif index == 0:
        "HELP!!"
        c = head
        c.next = head.next
        result = Node(data)
        result.next = c
        #print "Updated: ",result.data, " ",result.next.data
    return result

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

# def insert_nth(head, index, data):
#     if index == 0: return Node(data, head)
#     if head and index > 0:
#         head.next = insert_nth(head.next, index - 1, data)
#         return head
#     raise ValueError

# print_list(one)
# print "\n",
# insert_nth(one,0,12)
# print_list(one)

# print get_nth(one,10)
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

print_list(one)
print sorted_insert(one, 10.5).data
print_list(one)

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