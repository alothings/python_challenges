'''
Simple random password generator using iterators. The generator can accept two parameters:
available_chars: The characters to use to generate the password. OPTIONAL.
Default: A set of lowercase characters, digits and symbols. (hint, check the string module)

length: The length of the password. OPTIONAL. Default: 8

support: python2.7 and python3
'''
import random
import string

class SimplePasswordGenerator(object):
    # DEFAULT_CHARS = "abcdefghijklmnopqrstuvwxyz0123456789$%".split()
    DEFAULT_CHARS = string.digits + string.punctuation + string.ascii_letters

    def __init__(self, available_chars=DEFAULT_CHARS, length=8):
        self.available_chars = available_chars
        self.length = length
        # self.password = random.sample(self.available_chars, self.length)
        pass

    def __iter__(self):
        return iter(self)

    def __next__(self):
        password = ''.join([random.SystemRandom().choice(self.available_chars) for _ in range(self.length)])
        # return random.sample(self.available_chars, self.length)
        return password
    next = __next__

## TEST PART
pass_generator = SimplePasswordGenerator()
print(next(pass_generator))  # '%58a$d8a' (length=8)

pass_generator = SimplePasswordGenerator(available_chars=['a', 'b'], length=4)
print(next(pass_generator))
print(next(pass_generator))
print(next(pass_generator))


'''
pass_generator = SimplePasswordGenerator()
next(pass_generator)  # %58a$d8a (length=8)

pass_generator = SimplePasswordGenerator()
next(pass_generator)  # '%58a$d8a' (length=8)

pass_generator = SimplePasswordGenerator(available_chars=['a', 'b'], length=4)
next(pass_generator)  # 'abba
'''