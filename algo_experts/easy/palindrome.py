# Takes non empty string and returns boolean True if string is palindrome

def isPalindrome(string):
    
    for i in range(len(string) // 2):
        print("i", string[i], string[-i])
        if string[i] != string[-i]:
            return False

    return True