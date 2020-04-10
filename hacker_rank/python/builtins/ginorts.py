"""
#####################################################################
Intro:

Task: Given string s, containing alphanumeric characters only.
Sort in the following manner:
- all lowercase are ahead of uppercase
- all uppercase are ahead of digits
- all sorted odd digits ahead of sorted even digits

Input: String s

Output: string sorted

"""
import string


def ginorts(s):
    return sorted(s, key=(string.ascii_letters + '1357902468').index)

if __name__ == '__main__':
    s = input()
    print(*ginorts(s), sep='')

""" Test input:


"""