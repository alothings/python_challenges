n = [[10, 0], [3, 5], [5, 8]]

# kata 8, function takes list of list(size 2), containing number
# of inputs (0), and outputs(1). Find the last eresponse.
def number(bus_stops):
    # Good Luck!
    n = len(bus_stops)
    [x, y] = [0, 0]
    for i in range(n):
        x = x + bus_stops[i][0]
        y = y + bus_stops[i][1]
    return x - y
print number(n)

# Another solution
def number1(bus_stops):
    return sum(stop[0] - stop[1] for stop in bus_stops)
