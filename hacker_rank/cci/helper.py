from random import randint

'''
Classes in this library
- Node used in: SinglyLinkedList, DoublyLinkedList
- Stack
- TreeNode
Methods:
- binary_search(array, value)

'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)


class SinglyLinkedList:
    def __init__(self, head = None):
        self.head = head

    def __iter__(self):
        current = self.head
        while current:
            yield current   # yield:
            current = current.next
# iterabable: data is iterable as many times as you wish
# generators: are iterables but can only iterate ONCE
# yield: Similar to return, but returns a generator

    def append(self, value):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = Node(value)
        else:
            self.head = Node(value)

    def get_position(self, position):
        counter = 1
        current = self.head
        if position < 1:
            return None
        while current and counter <= position:
            if counter == position:
                return current
            current = current.next
            counter += 1

    def insert(self, new_element, position):
        counter = 1
        current = self.head
        if position > 1:
            while current and counter < position:
                if counter == position - 1:
                    new_element.next = current.next
                    current.next = new_element
                current = current.next
                counter += 1
        elif position == 1:
            new_element.next = self.head
            self.head = new_element

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

    def __str__(self):
        values = [str(x) for x in self]
        return ' -> '.join(values)

    def add(self, value):
        if self.head is None:
            self.tail = self.head = Node(value)
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        return self.tail

    def add_multiple(self, values):
        for v in values:
            self.add(v)

    def generate(self, n, min, max):
        self.head = self.tail = None
        for i in range(n):
            self.add(randint(min, max))
        return self


class Stack:
    def __init__(self):
        self.stack = []
        self.min = []

    def __str__(self):
        return str(self.stack)

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) <= 0


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

    def add_left(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        elif self.root.left is None:
            self.root.left = TreeNode(value)
        else:
            return False

    def add_right(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        elif self.root.right is None:
            self.root.right = TreeNode(value)
        else:
            return False

    def insert(self, value):
        """
        Insert new node with data
        @param data node data object to insert
        """
        if value < self.data:
            if self.left is None:
                self.left = TreeNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = TreeNode(value)
            else:
                self.right.insert(value)

    def contains(self, value):
        if value == self.data:
            return True
        elif value < self.data:
            if self.left is None:
                return False
            else:
                return self.contains(self.left)
        else:
            if self.right is None:
                return False
            else:
                return self.contains(self.right)

    def in_order(self):
        if self.left:
            self.left.in_order()
        print(self.data)
        if self.right:
            self.right.in_order()


def binary_search(array, value):
    low = 0
    high = len(array)
    mid = int((low + high)/2)

    while low < high:
        if array[mid] == value:
            return mid
        if array[mid] > value:
            high = mid
            mid = int((low + high)/2)
        if array[mid] < value:
            low = mid + 1
            mid = int((low + high)/2)
    return -1






