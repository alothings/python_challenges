"""
Ordereddict: remembers order of the keys as they were inserted.

Task: List of n itesm with their prices that consumers bought.
print each item and price in order of occurence

Input: n items
n lines with items name and price

Output:

"""


def func():
    pass


if __name__ == '__main__':
    from collections import OrderedDict

    n = int(input())
    entries = OrderedDict()

    for i in range(n):
        line = input().split()
        net_price = int(line[-1])
        item_name = ' '.join(line[:-1])
        entries[item_name] = entries.get(item_name, 0) + net_price

    for k, v in entries.items():
        print('{} {}'.format(k, v))