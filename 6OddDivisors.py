def oddity(n):
    # given an integer n, return 'odd' if number of its divisors is odd
    # else, return 'even'
    if n == 1:
        counter = 1
    if n == 2:
        counter = 2
    elif n > 2:
        counter = 2
        for i in range(2, (n/2) +1):
            #print i
            if n%i == 0:
                counter += 1
    #print counter
    if counter%2 == 0:
        return 'even'
    else:
        return 'odd'

print oddity(12)
print oddity(4)
print oddity(1)
print oddity(156335841)



