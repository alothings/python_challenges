"""
Calendar module allows to output calendars, and provides useful
functions for them

calendar.TextCalendar([firstweekday])
Example:
import calendar
print(calendar.TextCalendar(firstweekday=6).formatyear(2015)

Task: find day given a date.

Input: single line as: MM DD YYYY

Output:

"""


import calendar

if __name__ == '__main__':
    m, d, y = map(int, input().split())

    day_num = calendar.weekday(y, m, d)
    print(calendar.day_name[day_num].upper())


