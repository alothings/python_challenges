def findThreeLargestNumbers(array):
    # Write your code here.
    largest = [0, 0, 0]

    for i in range(len(array)):

        if array[i] >= largest[0]:
            largest[0] = array[i]
            new = 0
            while new < 2 and largest[new] > largest[new + 1]:
                largest[new], largest[new  + 1] = largest[new + 1], largest[new]
                new += 1

    return largest


def findThreeLargestNumbers(array):
    # Write your code here.
    largest = [None, None, None]
    for num in array:
        update_largest(largest, num)
    return largest

def update_largest(largest, num):
    
    if largest[2] is None or num > largest[2]:
        shift_and_update(largest, num, 2)
    elif largest[1] is None or num > largest[1]:
        shift_and_update(largest, num, 1)
    elif largest[0] is None or num > largest[0]:
        shift_and_update(largest, num, 0)

def shift_and_update(largest, num, idx):

    for i in range(idx + 1):
        if i == idx:
            largest[i] = num
        else:
            largest[i] = largest[i+1]
