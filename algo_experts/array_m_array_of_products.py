
# O(n^2) time | O(n) space
def arrayOfProducts1(array):
    # Write your code here.
    output = [1]*(len(array))
    for i in range(len(array)):
        for j in range(len(array)):
            if j != i:
                output[i] = output[i] * array[j]
            else:
                output[i] = output[i] * 1
    print(output)


# O(n) time | O(n) space but uses a bit of space
def arrayOfProducts2(array):
    # Write your code here.
    a = [1]*(len(array))
    b = [1]*(len(array))
    output = [1]*(len(array))
    for i in range(len(array)-1):
        a[i + 1] = a[i] * array[i]
    for i in range(len(array)-1, 0, -1):
        b[i - 1] = b[i] * array[i]
    print([ x * y for x, y in zip(a, b)])

# O(n) time | O(n) space optimized
def arrayOfProducts(array):
    # Write your code here.
    output = [1]*(len(array))
    product = 1

    for i in range(len(array)-1):
        output[i + 1] = output[i] * array[i]

    for i in range(len(array)-1, 0, -1):
        product *= array[i]
        output[i - 1] *= product


    print(output)


a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
arrayOfProducts(a)