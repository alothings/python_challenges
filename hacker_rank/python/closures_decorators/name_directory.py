"""
#####################################################################
Intro: Use decorators to build a name directory.

Task: Given some info about N people (first and last names, age, sex)
Print their names in a specific format sorted by age (ascending). 
If same age, print in order of input.

Input:
3
Mike Thomson 20 M
Robert Bustle 32 M
Andria Bustle 30 F

Output:
Mr. Mike Thomson
Ms. Andria Bustle
Mr. Robert Bustle
"""
import operator

def person_lister(f):
    def inner(people):
        p = []
        # print("before: ", people)
        # sorted(people, key=lambda row: int(row[2]))
        people.sort(key=lambda row: int(row[2]))
        # print("after, ",people)
        for el in people:
            p.append(f(el))
        return p
    return inner


@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')
    # print(people)


""" Test results:
Mr. Mike Thomson
Mr. Robert Bustle
Ms. Andria Bustle


"""