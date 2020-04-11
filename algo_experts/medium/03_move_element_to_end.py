"""
Mve element to end.

You are given an array of integers and an integer. Write a function that moves all
the instances of that integer in the array to the end of the array and returns the
array.

Perform this in place, no need to mantainer the order of other integers

Space complexity:
Time complexity:
"""

def move_element_to_end(array, toMove):
    l = 0
    r = len(array) - 1
    while l < r:
        if array[l] == toMove:
            while array[r] == toMove and l < r:
                r -= 1
            array[l], array[r] = array[r], array[l]
            print("here", array)
        l += 1
    return array
            
a = [2, 3, 2, 2, 2, 3, 4, 2]
print(move_element_to_end(a, 2))