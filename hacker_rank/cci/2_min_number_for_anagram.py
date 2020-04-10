# Given two strings,a and b, that may or may not be of the same length,
# determine the minimum number of character deletions required to make
# a and b anagrams. Any characters can be deleted from either of the strings.

def number_needed(a, b):
    # Will assume ascii of 128 characters
    st = [0]*128
    # print(st, len(st))
    max_len = max(len(a), len(b))
    # print(max_len)
    for i in range(max_len):
        if i < len(a):
            st[ord(a[i])] += 1
        if i < len(b):
            st[ord(b[i])] -= 1
        # print(st)

    return sum(list(map(abs, st)))      # Pythonian way

a = "abcde"
b = "cded"
print(number_needed(a, b))

# a = input().strip()
# b = input().strip()
#
# print(number_needed(a, b))



# Methods used:
# input(): Gets input from keyboard to string
# strip(): if no arguments, removes extra spaces at begining and end.
#           or removes the characters passed as arguments.
