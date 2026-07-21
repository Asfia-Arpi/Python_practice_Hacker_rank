# HackerRank Problem: Python If-Else
# Topic: 01-introduction
# File Name: 02_python_if_else.py
n = int(input())
if n % 2 != 0:
    print("Weird")
else:
    if 2<= n <=5:
        print("Not Weird")
    elif 6<= n <=20: 
        print("Weird")
    elif n>20:
        print("Not Weird")