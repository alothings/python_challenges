# Selection Sort
# Select number, traverse right part of array to find the smallest number
# append smallest number (swap) to left  array

def selectionSort(array):

    idx = 0
    while idx < len(array):
        smallest_idx = find_smallest(array, idx)
        append_smallest(array, idx, smallest_idx)
        idx += 1
    return array

def find_smallest(array, idx):
    idx_smallest = idx
    for i in range(idx, len(array) - 1):
        if array[idx_smallest] > array[i + 1]:
            idx_smallest = i + 1
    
    return idx_smallest

def append_smallest(array, idx, smallest_idx):
    array[idx], array[smallest_idx] = array[smallest_idx], array[idx]
