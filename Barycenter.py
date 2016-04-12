# Barycenter is the intersection of medians in triangle.


def bar_triang(pointA, pointB, pointC): # points A, B and C will never be aligned
    # your code here
    xO = round((pointA[0] + pointB[0] + pointC[0])/3.0,4)
    yO = round((pointA[1] + pointB[1] + pointC[1])/3.0,4)
    return [xO, yO] # coordinates of the barycenter expressed up to four decimals
                    # (rounded result)

print bar_triang([4, 6], [12, 4], [10, 10])