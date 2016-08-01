''' Object Oriented Programming
Implementation fo simple bookstore
Create methods for search_books, etc'''


class Author(object):
    authors_dict = {}

    def __new__(cls, *args, **kwargs):
        

    def __init__(self, name=None, nationality=None):
        if "%s %s" % (name, nationality) not in Person.persons_dict:
            self.name = name
            self.nationality = nationality
            author_info = "%s %s" % (self.name, self.nationality)
            Author.authors_dict[author_info] = self


class Person(object):

    persons_dict = {}
    '''Creates a person object'''
    def __init__(self, firstname, lastname):
        self.lname = lastname.title()
        self.fname = firstname.title()
        fullname = "%s %s" % (self.fname, self.lname)
        Person.persons_dict[fullname] = self

class Book(object):
    books = {}
    def __init__(self, title=None, author=None):
        if title in books and author == books[title]:
            return self
        else:
            self.__class__.books[title] = author
            return self
            # def __repr__(self):
            #     print str(self)
        self.author = author

# class BookStore(object, Author, Book):
class BookStore(object):

    def __init__(self):
        self.books = []
        self.authors = []

    def add_book(self, book_object):


        if book_object not in self.books:
            self.books.append(book_object)
        if book_object.author not in self.authors:
            self.authors.append(book_object.author)
        print("Book obj {} and type: {}".format(str(book_object), type(book_object)))
        print("Author obj {} and type: {}".format(str(book_object.author), type(book_object.author)))



    def search_books(self, **kargs):
        if len(kargs)==0:
            raise AttributeError()
        result = []
        if 'title' in kargs:
            print("insde if")
            # result.append(book for book in self.books if self.books.name == kargs['title'])
            for book in self.books:
                # print("Book: {}".format(str(book)))
                # print("Type: {}".format(type(book)))
                # print(kargs['title'])
                # print(book.name)
                # if str(book) == kargs['title']:
                if book == kargs['title']:
                    result.append(book)
                # result.append(self.books[])
            # print("Re: {}".format(type(result[0])))
        if 'author' in kargs:
            for book in self.books:
                if book.author == eval(kargs['author']):
                    result.append(book)


            #
            # for author in self.authors:
            #     if author == eval(kargs['author']):
            #     # if str(author) == kargs['author']:
            #         result.append(author)
            # print("Res: {}".format(type(eval(result[0]))))
            # print(result[0])
        # print("type: {}".format(type(result[0])))
        return result
#######
store = BookStore()

# Authors
poe = Author(name="Edgar Allan Poe", nationality="American")
poe2 = Author(name="Edgar Allan Poe", nationality="American")

doyle = Author(name="Arthur Conan Doyle", nationality='British')

# Books
raven = Book(title="The Raven", author=poe)
study_in_scarlet = Book(title='A Study in Scarlet', author=doyle)

# main
store.add_book(raven)
store.add_book(study_in_scarlet)

results1 = store.search_books(title='raven')
print(poe==poe2)
print(len(results1))
print("Res1: {}".format(results1))
# print(results[0])
#
# print(assertEqual(len(results), 1))
# print(assertEqual(results[0], raven))
#
results2 = store.search_books(author='doyle')
print(len(results2))
print("Res1: {}".format(results2))
# self.assertEqual(len(results), 1)
# self.assertEqual(results[0], study_in_scarlet)