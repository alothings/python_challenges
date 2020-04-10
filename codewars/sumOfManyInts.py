# Function takes n and m
# Sum numbers in function i%m, from i=1 to n
def f(n, m):
    m = int(m)
    n = int(n)
    t1 = (m)*(m-1)/2
    if n%m == 0:
        res = int(n/m)*t1
    else:
        res = int(n/m)*t1 +(n%m)*((n%m)+1)/2
    return res

print f(10,5)
print f(15,10)
print f(20,20)
# print f(6171541, 52296672)