def binarySearch(array, target):
    # Write your code here.
    p_first = 0
    p_last = len(array) - 1
    p_middle = int((p_last - p_first) / 2)

    if target < array[p_first] or target > array[p_last]:
        return -1

    while p_last >= p_first:

        if target > array[p_middle]:
            
            p_first = p_middle + 1
            p_middle = p_first + int((p_last - p_first) / 2)
        
        elif target < array[p_middle]:

            p_last = p_middle - 1
            p_middle = int((p_last - p_first) / 2)
        
        else:
            return p_middle
    
    return -1