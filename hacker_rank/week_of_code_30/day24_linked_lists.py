#!/bin/python3

'''
Day 24: More Linked Lists - Removing Duplicates
Given the head of a Linked List, return the head
of that List without duplicates

'''

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class Solution:
    def insert(self,head,data):
            p = Node(data)
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head

    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def removeDuplicates(self, head):
        if head is None or head.next is None:
            return head
        l = []
        res = head
        previous = Node(None)
        while head is not None:
            if head.data in l:
                previous.next = head.next
            else:
                l.append(head.data)
                previous = head
            head = head.next
        return res

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)
head=mylist.removeDuplicates(head)
mylist.display(head);