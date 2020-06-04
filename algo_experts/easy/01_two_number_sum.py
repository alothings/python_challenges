"""
Write a function that takes in a nnon empty array of distnct integers and an integer representing a target sum.

"""

def twoNumberSum(array, targetSum):
    # Write your code here.
    res_map = {}
    for el in array:
        if targetSum - el in res_map:
            return [el, targetSum - el]
        res_map[el] = True
    return []

a = [3,5,-4,8,11,1,-1,6]
target = 10
print(twoNumberSum(a, target))