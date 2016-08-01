#
def int_cube_sum_div(n):
    # Its cube is divisible by the sum of its divisors (ie 6)
    # 6^3 % (1+2+3+6) -> 216%12

    counter = 0
    k = 2
    while True:


        divs = [1]
        k += 1
        for i in range (2,k/2 +1):
            if k%i == 0:
                divs.append(i)
        divs.append(k)
        print divs

        if k*k*k%sum(divs) == 0:

            print 'k and k^3',k,  k*k*k
            print divs
            counter += 1


        if counter == n:
            print 'n',  n
            print 'counter', counter
            break
    return k

#print int_cube_sum_div(1)
#int_cube_sum_div(2)
print int_cube_sum_div(3)
#int_cube_sum_div(4)
