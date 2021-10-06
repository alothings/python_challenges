def generateDocument(characters, document):
    # Write your code here.
    char = {}

    for el in characters:
        char[el] = 1 if el not in char else char[el] + 1
        print(el, char[el])

    for el in document:
        if el not in char or char[el] == 0: return False
        else:
            char[el] -= 1
        print(el, char[el])

    return True


c = "Bste!hetsi ogEAxpelrt x "
d = "AlgoExpert is the Best!"

print(generateDocument(c, d))