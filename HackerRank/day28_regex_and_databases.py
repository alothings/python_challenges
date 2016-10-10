#!/bin/python3
'''
Day 28: RegEx, Patterns, and Databases

Task
Consider a database table Emails, with attributes First Name and Email ID.
Given N rows of data of the Emails table. Print alphabetically ordered list
of people whose address ends in $gmail.com

Input: N total number of rows in table
       2 space-separated strings denoting a persons first name and email
Constrains: first name a-z only lower cases
            emails a-z, @ and .

'''



import sys


N = int(input().strip())
for a0 in range(N):
    firstName,emailID = input().strip().split(' ')
    firstName,emailID = [str(firstName),str(emailID)]
