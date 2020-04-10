'''
Build a calculator using only static and class methods.

'''

class Calculator(object):

    def __init__(self):
        pass

    @classmethod
    def add(cls, x, y):
        return x + y

    @classmethod
    def subtract(cls, x, y):
        return cls.add(x, -y)

    @classmethod
    def multiply(cls, *args):
        res = 1
        for el in args:
            res *= el
        return res

    @classmethod
    def divide(cls, x, y):
        return float(x)/float(y)

print(Calculator.add(2, 4))
print(Calculator.subtract(4, 2))

'''
@classmethod: Allows to use the class without need to instantiate
it. A particular use is inheritable alternative constructors

@staticmethod: Used to group functions which have a logical connection
with a class to the class. It knows nothing about the class or instance.
'''