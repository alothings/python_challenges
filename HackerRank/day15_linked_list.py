'''
Day 15: Linked List
Create insert function for linked list

'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def display(self,head):
        current = head
        # print("Test")
        while current:
            # print("In loop")
            print(current.data,end=' ')
            current = current.next

    def insert(self, head, data):
        t = Node(data)
        if not head:
            head = t
            # print("Inserting head: {}".format(head.data))
            return head
        current = head
        while current.next is not None:
            current = current.next
        current.next = t
        return head



mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)
mylist.display(head);