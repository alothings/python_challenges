def someSort(array):
    # Write your code here.
    for i in range(1, len(array)):
        idx = i
        while idx > 0 and array[idx] < array [idx - 1]:
            swap(idx, idx -1, array)
            idx -= 1
	return array


def swap(idx, array):
    array[idx], array[idx - 1] = array[idx - 1], array[idx]


# Space O(1)
# time O(n^2)
def bubbleSort(array):
    # Write your code here.
    is_sorted = False
    counter = 0
    while not is_sorted and counter < len(array):
        
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                swap(i, i + 1, array)

        is_sorted = True
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                is_sorted = False

        counter += 1
	return array


def swap(idx, j, array):
    array[idx], array[j] = array[j], array[idx]