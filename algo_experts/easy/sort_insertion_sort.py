def insertionSort(array):
    # Write your code here.
    for i in range(1, len(array)):
        idx = i
        while idx > 0 and array[idx] < array [idx - 1]:
            swap(idx, idx -1, array)
            idx -= 1
	return array

def swap(idx, j, array):
    array[idx], array[j] = array[j], array[idx]