#Is Prime
# input: integer, output: T/F
def is_prime(num):
    ans = True
    n = abs(num)
    c = 2
    if n == 0 or n == 1:
        return False
    if n > 2:
        while n > c:
            # print c
            if n%c == 0:
                # print "c: ",c
                ans = False
                break
            c += 1
    return ans

print is_prime(0)
print is_prime(1)
print is_prime(2)