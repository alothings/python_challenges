'''
Lesson on Inheritance and Abstract Classes.
Task: GIven a Book class, and a SOlution class, write a MyBook class that does:
Inherits from Book, has constructor with 3 parameters, implements the book abstract
class "display()".
'''

from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author
    @abstractmethod
    def display(): pass

class MyBook(Book):
    def __init__(self, title, author, price):
        Book.__init__(self, title, author)
        self.price = price
        # print("Hi")

    def display(self):
        # print("Test")
        print("Title: {}".format(self.title))
        print("Author: {}".format(self.author))
        print("Price: {}".format(self.price))
        # return("Success")



# title=input()
# author=input()
# price=int(input())
title="Poem"
author="Alo"
price=10
new_novel=MyBook(title,author,price)
new_novel.display()