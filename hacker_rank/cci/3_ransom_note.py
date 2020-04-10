# Given the words in the magazine and the words in the ransom note,
# print Yes if he can replicate his ransom note exactly using whole
# words from the magazine; otherwise, print No.


def ransom_note(magazine, ransom):
    n = {}
    magazine = magazine.split()
    ransom = ransom.split()
    if len(magazine) < len(ransom):
        return False
    for word in ransom:
        n[word] = n.get(word, 0) + 1
    for word in magazine:
        if word in n.keys():
            n[word] -= 1
    # print(n)
    for val in n.values():
        if val > 0:
            return False
    return True

# m, n = map(int, input().strip().split(' '))
# magazine = input().strip().split(' ')
# ransom = input().strip().split(' ')
# answer = ransom_note(magazine, ransom)
# if (answer):
#     print("Yes")
# else:
#     print("No")

m = "give give me one grand today Night Night"
n = "give give one grand today night"
# m = "ola amigo que tal como estas"
# n = "ola"
print(ransom_note(m,n))