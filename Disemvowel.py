# Remove vowels of string

def disemvowel(string):
    string = string.replace("a","")
    string = string.replace("e","")
    string = string.replace("i","")
    string = string.replace("o","")
    string = string.replace("u","")
    string = string.replace("A","")
    string = string.replace("E","")
    string = string.replace("I","")
    string = string.replace("O","")
    string = string.replace("U","")
    return string

print disemvowel("This website is for losers LOL!")

def disemvowel1(string):
    remove = "aeioAEIOU"
    string = string.translate(None, remove)
    return string

print disemvowel1("This website is for losers LOL!")