'''
Day 14: Scope

Difference class. Finds the largest absolute difference between a set of integers
1. Constructure that takes array of integers and saves to the elements variable
2. computeDifference that finds maximum absolute and store in instance variable.
'''

class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0

    def computeDifference(self):
        '''Computes maximum difference '''
        l = sorted(self.__elements)
        print(l)
        self.maximumDifference = l[-1] - l[0]

_ = "8 19 3 2 7"
a = [int(e) for e in _.split(' ')]
# a = [1,2,3,4,5]
d = Difference(a)
d.computeDifference()
print(d.maximumDifference)