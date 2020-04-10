"""
User enters string and substring
Return 3 of times substring is contained
"""


def count_substring(string, sub_string):
    index = 0
    counter = 0

    while index <= len(string)-len(sub_string):
        if string[index] == sub_string[0]:
            match = True
            for i in range(1, len(sub_string)):
                if sub_string[i] != string[index + i]:
                    match = False
                    break
            if match: counter += 1
        index += 1

    return counter

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)