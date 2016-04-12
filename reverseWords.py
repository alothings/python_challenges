import re
# reverseWords
# Input: string, reverses each word in the string, spaces should remain.
def reverse_words(str):
    s = str
    l = re.split(r'(\s+)',s)           # make list if string elements
    new_l = []              # initialize empty list
    for item in l:
        item = item[::-1]       # reverse items in list
        new_l.append(item)      # append reversed items to new list
    new = ''.join(new_l)       # join items in list to string
    return new




a = "this  is  an  example"
print reverse_words(a)