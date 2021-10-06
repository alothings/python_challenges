def classPhotos(redShirtHeights, blueShirtHeights):
    # Write your code here.

    redShirtHeights.sort()
    blueShirtHeights.sort()

    if redShirtHeights[0] == blueShirtHeights[0]:
        return False
    if redShirtHeights[0] < blueShirtHeights[0]:
        for i in range(len(redShirtHeights)):
            if redShirtHeights[i] >= blueShirtHeights[i]:
                return False
    elif  redShirtHeights[0] > blueShirtHeights[0]:
        for i in range(len(redShirtHeights)):
            if blueShirtHeights[i] >= redShirtHeights[i]:
                return False

    return True 