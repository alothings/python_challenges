'''
Day 26: Nested Logic
Objective to understand nested conditional statements.
Task: Given the expected and actual return dates for a library book
Create a program that calculates the fine

Also, Learn about unit testing
'''


def calculate_fine(d, m, y, ed, em, ey):
    # res = [ x - y for x, y in zip(actual_list, expected_list)]
    # print(d, m, .y, ed, em, ey)
    day_diff = d - ed
    month_diff = m - em
    year_diff = y - ey
    if ey - y > 0:
        return 0
    elif ey == y:
        if em - m > 0:
            return 0
        elif em == m:
            if ed - d >= 0:
                # 1. if returned on or before expected return date fine = 0
                return 0
            else:
                # 2. if returned later, but in same month and year fine = 15 * days
                return 15*abs(ed-d)
        else:
            # 3. after month, but same year fine = 500 * days
            return 500*abs(em - m)
    else:
        # 4. else: fine = 10000
        return 10000


def reading():
    # It is guaranteed to have correct dates
    d, m, y = input().split(" ")
    d, m, y = int(d), int(m), int(y)
    ed, em, ey = input().split(" ")
    ed, em, ey = int(ed), int(em), int(ey)
    return d, m, y, ed, em, ey

# print(reading())
# d, m, y, ed, em, ey = reading()
# calculateFine(d, m, y, ed, em, ey)
# print(calculate_fine(*reading()))

# case 0 (day before)
d, m, y, ed, em, ey = 31, 12, 2009, 1, 1, 2010
print(calculate_fine(d, m, y, ed, em, ey))
# case 0 (month before)
d, m, y, ed, em, ey = 5, 4, 2000, 5, 5, 2000
print(calculate_fine(d, m, y, ed, em, ey))

# case 15 (day later, 29 days later)
d, m, y, ed, em, ey = 6, 5, 2000, 5, 5, 2000
print(calculate_fine(d, m, y, ed, em, ey))
d, m, y, ed, em, ey = 30, 5, 2000, 5, 5, 2000
print(calculate_fine(d, m, y, ed, em, ey))

# case 500 (same day one month later, smaller day month later, bigger day months later)
d, m, y, ed, em, ey = 5, 6, 2000, 5, 5, 2000
print(calculate_fine(d, m, y, ed, em, ey))
d, m, y, ed, em, ey = 1, 6, 2000, 5, 5, 2000
print(calculate_fine(d, m, y, ed, em, ey))
d, m, y, ed, em, ey = 20, 10, 2000, 5, 5, 2000
print(calculate_fine(d, m, y, ed, em, ey))

# case 1000
d, m, y, ed, em, ey = 5, 5, 2008, 5, 5, 2000
print(calculate_fine(d, m, y, ed, em, ey))

