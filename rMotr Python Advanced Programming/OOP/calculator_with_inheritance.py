'''
Calculator using OOP and inheritance.
A calculator can be built with different operations.
Operation is an abstract class. Define subclasses

'''
from functools import reduce

class OperationInvalidException(Exception):
    def __init__(self):
        Exception.__init__(self)


class Operation(object):
    def __init__(self, *args):
        self.numbers = args

    def operate(self):
        pass


class AddOperation(Operation):
    def operate(self):
        return reduce(lambda x,y: x+y, self.numbers)


class SubtractOperation(Operation):
    def operate(self):
        return reduce(lambda x,y: x-y, self.numbers)


class Calculator(object):
    def __init__(self, operations=None):
        self.operations = operations

    def calculate(self, *args):
        if args[-1] not in self.operations:
            raise OperationInvalidException()

        # Creates instance of Operation requested with arguments
        temp_op = self.operations[args[-1]](*args[:-1])
        # Operate
        return temp_op.operate()



calc1 = Calculator(operations={
    'add': AddOperation,
    'subtract': SubtractOperation})

print(calc1.calculate(5, 2, 1, 'subtract'))

calc2 = Calculator(operations={
    'add': AddOperation})
print(calc2.calculate(1, 5, 'add'))






