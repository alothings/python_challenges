# Sum the last 3 numbers of the sequence to generate next
#
def tribonacci(signature, n):
    new_l = signature
    if n <=3:
        res = signature[:n]
        return res
    else:
        for i in range(3,n):
            new_l.append(0)
            new_l[i] = new_l[i-1] + new_l[i-2] + new_l[i-3]
    return new_l


a = [1,1,1]
print tribonacci(a,4)
# 0,1,1,2,4,7