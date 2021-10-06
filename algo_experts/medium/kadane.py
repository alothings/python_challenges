def kadanesAlgorithm(array):
    # Write your code here.
    
    max_ending = float('-inf')
    for i in range(len(array)):
        max_ending = max(max_ending + array[i], array[i])

    return max_ending
