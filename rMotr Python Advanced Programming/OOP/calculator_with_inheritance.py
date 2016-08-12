'''
Calculator using OOP and inheritance.
A calculator can be built with different operations.
Operation is an abstract class. Define subclasses

'''

class Operation(object):
    def __init__(self, *args):
        pass

    def operate(self):
        pass

class AddOperation(Operation):

    def operate(self):
        pass