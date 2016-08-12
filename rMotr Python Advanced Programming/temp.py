for book in self.books:
    print(eval(str(kwargs['title'])))
    print(type(eval(str(kwargs['title']))))
    print(type(book))

    # print("Loop! {}".format(book))
    if eval(str(kwargs['title'])) == book:
        print("Yay again! {}".format(book.title))
        res.append(book)
        # else:
        #     print("Nope")