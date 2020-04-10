#!/bin/python3
"""
A made rules for valid passwords and B needs to write a program to generate all possible passwords
that meet those rules.
Rules
 - exactly n lowercase English letters
 - the password is melodious, meaning that consonants can only be next to vowels, and vowels can only be
 next to consonants.
 - the password cannot contain the letter y.
 - the first letter of the password can be either a vowel or consonant

Given length n, output all possible passwords, 1<=n<=6
"""

def melodious_password_generator(n):
    '''
    n = 1; 20 + 5 = 25
    n = 2; 20*5 + 5*20 = 200
    n = 3; 20*5*20 + 5*20*5 = 2500
    n = 4; 20*5*20*5 + 5*20*5*20 = 20000
    '''
    consonants = 'bcdfghjklmnpqrstvwxz'
    vowels = 'aeiou'
    c = list(consonants)
    v = list(vowels)
    terms = c + v
    while n > 1:
        size = len(terms)
        for i in range(size):
            if terms[i][-1] in v:
                for p in range(len(c)):
                    terms.append(terms[i] + c[p])
            else:
                for p in range(len(v)):
                    terms.append(terms[i] + v[p])
        terms = terms[size:]
        n -= 1
    for el in terms:
        print(el)
    # return terms

# print(melodious_password_generator(n))
print(melodious_password_generator(2))


# a = ['ba', 'be', 'bi', 'bo', 'bu', 'ca', 'ce', 'ci', 'co', 'cu', 'da', 'de', 'di', 'do', 'du', 'fa', 'fe', 'fi', 'fo', 'fu', 'ga', 'ge', 'gi', 'go', 'gu', 'ha', 'he', 'hi', 'ho', 'hu', 'ja', 'je', 'ji', 'jo', 'ju', 'ka', 'ke', 'ki', 'ko', 'ku', 'la', 'le', 'li', 'lo', 'lu', 'ma', 'me', 'mi', 'mo', 'mu', 'na', 'ne', 'ni', 'no', 'nu', 'pa', 'pe', 'pi', 'po', 'pu', 'qa', 'qe', 'qi', 'qo', 'qu', 'ra', 're', 'ri', 'ro', 'ru', 'sa', 'se', 'si', 'so', 'su', 'ta', 'te', 'ti', 'to', 'tu', 'va', 've', 'vi', 'vo', 'vu', 'wa', 'we', 'wi', 'wo', 'wu', 'xa', 'xe', 'xi', 'xo', 'xu', 'za', 'ze', 'zi', 'zo', 'zu', 'ab', 'ac', 'ad', 'af', 'ag', 'ah', 'aj', 'ak', 'al', 'am', 'an', 'ap', 'aq', 'ar', 'as', 'at', 'av', 'aw', 'ax', 'az', 'eb', 'ec', 'ed', 'ef', 'eg', 'eh', 'ej', 'ek', 'el', 'em', 'en', 'ep', 'eq', 'er', 'es', 'et', 'ev', 'ew', 'ex', 'ez', 'ib', 'ic', 'id', 'if', 'ig', 'ih', 'ij', 'ik', 'il', 'im', 'in', 'ip', 'iq', 'ir', 'is', 'it', 'iv', 'iw', 'ix', 'iz', 'ob', 'oc', 'od', 'of', 'og', 'oh', 'oj', 'ok', 'ol', 'om', 'on', 'op', 'oq', 'or', 'os', 'ot', 'ov', 'ow', 'ox', 'oz', 'ub', 'uc', 'ud', 'uf', 'ug', 'uh', 'uj', 'uk', 'ul', 'um', 'un', 'up', 'uq', 'ur', 'us', 'ut', 'uv', 'uw', 'ux', 'uz']
# print("size: ", len(a))
