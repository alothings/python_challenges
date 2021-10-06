def nonConstructibleChange(coins):
    # Write your code here.
    k = 0
    coins.sort()
    if len(coins) < 1:
        return 1
    for coin in coins:
        if k + 1 < coin:
            return k + 1
        k += coin
    return k + 1


def sortedSquaredArray(array):
    # Write your code here.
	# -5 -2 1 4 8
	# 25 4 1 16 64

    if array[0] >= 0:
        print("Here")
        return [x*x for x in array]

    else:
        new_array = [None] * len(array)
        left = 0
        right = len(array) - 1  
        for i in range(len(array) - 1, -1, -1):
            print(i)
            if abs(array[left]) > abs(array[right]):
                new_array[i] = array[left] * array[left]
                left += 1
            else:
                new_array[i] = array[right] * array[right]
                right -= 1
        return new_array