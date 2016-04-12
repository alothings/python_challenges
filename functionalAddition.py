# Given 2 integers pos or neg, find the sum of all the numbers in between, including them.
# if both numbers are equal, return a or b
def get_sum(a,b):
    if a == b:
        return a
    elif a > b:
        return sum(range(b,a)) + a
    elif a < b:
        return sum(range(a,b)) + b


print get_sum(-1, 2)