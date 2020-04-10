"""
#####################################################################
Intro:

Task: Return list of valid email addresses in alph order
It must have the username@websitename.extension format type.
The username can only contain letters, digits, dashes and underscores.
The website name can only have letters and digits.
The maximum length of the extension is 3

Input: 

Output:

"""
import re
import string


def is_valid_email(s):
    try:
        username, website = s.split('@')
        website, ext = website.split('.')
    except:
        return False
    if len(ext) > 3: return False
    if len(username) <= 0 or len(website) <= 0 or len(ext) <= 0:
        return False
    for char in username:
        if char not in string.ascii_letters + string.digits + "-_":
            return False
    for char in website:
        if char not in string.ascii_letters + string.digits:
            return False
    # print(username, website, ext)
    return True

if __name__ == '__main__':
    n = int(input())
    l = [input() for i in range(n)]
    # is_valid_email(input())
    print(sorted(list(filter(is_valid_email, l))))



""" Test input:


"""