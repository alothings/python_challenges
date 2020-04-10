"""
Counter: container that stores elements as dictionary keys, and their
counts as dictionary values. Counter(iterable) has methods items(), keys().
and values()

Example
from collections import Coutner

myList = [1,1,2,3,4,4]
print(Counter(mylist).items())
[(1,2),(2,1),(3,1),(4,2)]

Task: x number of items, n number of customers willing to pay x

Input: by lines:
1 contains x # of shoes
2 contains space separated list of all shoe sizes in shop
3 n customers
following lines contain size and price x of each customer

Output:

"""
from collections import Counter


if __name__ == '__main__':
    x = int(input())        # # of shoes available
    # shoe_sizes = list(map(int, input().split()))
    shoes = Counter(map(int, input().split()))

    n = int(input())        # # of customers
    total = 0
    customers = {}
    for i in range(n):
        size, price = map(int, input().split())
        customers[size] = price
        if shoes[size]:
            shoes[size] -= 1
            total += price

    print(total)
