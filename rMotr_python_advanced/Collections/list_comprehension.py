'''
Write a function that receives a list and returns a new list without duplicates
List Complrehenssion link:
http://treyhunner.com/2015/12/python-list-comprehensions-now-in-color/

'''

def remove_duplicates_in_order(ls):
    new_ls = []
    for elem in ls:
        if elem not in new_ls:
            new_ls.append(elem)
    return new_ls

def reverse_list(ls):
    new_ls = []
    # new_i = 0
    # for i in range(len(ls)-1, -1, -1):
    #     print(ls[i])
    #     new_ls.append(ls[i])
    #     # new_i += 1
    # return new_ls

    '''Using List Comprehension'''
    return [ls[i] for i in range(len(ls)-1, -1, -1)]

def even_numbers(ls):
    return [x for x in ls if x%2==0]

def square_elements(ls):
    return [x*x for x in ls]

def divisible_numbers(ls, n):
    return [x for x in ls if all([x % el == 0 for el in n])]

def to_fahrenheit(ls):
    '''Using list comprehensions and lambdas to transform temperaturs'''
    return map(lambda x: x*(1.8) + 32, ls)

ls = [2,1,1,3,4]
# print(remove_duplicates_in_order(ls))
# print("Reverse: {}".format(reverse_list(ls)))
# print("Reverse: {}".format(even_numbers(ls)))
print("Conversion: {}".format(to_fahrenheit(ls)))
# print("Revse: {}".format(divisible_numbers([12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [2, 3])))



'''
Lambda functions:

foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]

print filter(lambda x: x % 3 == 0, foo)
[18, 9, 24, 12, 27]

print map(lambda x: x * 2 + 10, foo)
[14, 46, 28, 54, 44, 58, 26, 34, 64]

print reduce(lambda x, y: x + y, foo)
139
'''















