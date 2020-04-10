"""
Sets have: union, intersection, difference and symmetric difference,
but this operations don't make changes to the set.

To mutate set:

Adding Elements: .update() or |=
example:
H = set("Hacker")
R = set("Rank")
H.update(R)
print(H)
> set(['a', 'c', 'e', 'H', 'k', 'n', 'r', 'R'])

Intersection: .intersection_update() or &=
.difference_update() or -=
.symmetric_difference_update() or ^=

Task: Given set A and N number of other sets. Perform specific operations
on set A. Execute operations and print sum of elements from set A
"""

number_elements_a = int(input())
set_a = set(map(int, input().split()))
n_number_of_sets = int(input())

# print(set_a, type(set_a))

for i in range(n_number_of_sets):
    instruction, set_size = input().split()
    set_size = int(set_size)
    new_set = set(map(int, input().split()))

    if "intersection_update" == instruction:
        set_a.intersection_update(new_set)
    elif "update" == instruction:
        set_a.update(new_set)
    elif "symmetric_difference_update" == instruction:
        set_a.symmetric_difference_update(new_set)
    elif "difference_update" == instruction:
        set_a.difference_update(new_set)

print(sum(set_a))
# print(instruction, set_size, type(set_size))
