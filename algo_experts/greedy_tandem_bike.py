def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    # Write your code here.
    if fastest:
        redShirtSpeeds.sort()
        blueShirtSpeeds.sort(reversed)
    else:
        redShirtSpeeds.sort()
        blueShirtSpeeds.sort()
    total = 0
    for i in range(len(redShirtSpeeds)):
        speed = max(redShirtSpeeds[i], blueShirtSpeeds[i])
        total += speed


    return total