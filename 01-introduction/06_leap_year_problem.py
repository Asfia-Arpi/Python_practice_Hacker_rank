# HackerRank Problem: Leap Year
# Topic: 01-introduction
# File Name: 06_leap_year_problem.py

def is_leap(year):
    leap = False
    if (year % 400 == 0) or(year % 100 != 0 and year % 4 == 0):
        leap = True
    return leap

year = int(input())
print(is_leap(year))
