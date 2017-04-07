#!/bin/python3
'''
Day 28: RegEx, Patterns, and Databases

Task
Consider a database table Emails, with attributes First Name and Email ID.
Given N rows of data of the Emails table. Print alphabetically ordered list
of people whose address ends in @gmail.com

Input: N total number of rows in table
       2 space-separated strings denoting a persons first name and email
Constrains: first name a-z only lower cases
            emails a-z, @ and .

'''



import sys
import re

N = int(input().strip())
table = {}
for a0 in range(N):
    firstName,emailID = input().strip().split(' ')
    firstName,emailID = [str(firstName),str(emailID)]
    table[emailID] = firstName;

def get_name(table):
    names = []
    pass
    for email in table:
        if re.search(r'@gmail\.com$', email, 0):
            names.append(table[email])
    names.sort()
    for name in names:
        print(name)

get_name(table)


