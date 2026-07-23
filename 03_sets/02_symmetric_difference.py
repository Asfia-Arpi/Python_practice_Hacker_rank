# HackerRank Problem: Symmetric Difference
# Topic: 03-Sets
# File Name: 02_symmetric_difference.py

m = int(input())
a = set(map(int,input().split()))
n = int(input())
b = set(map(int,input().split()))

symmetric_set = a.symmetric_difference(b)
symmetric_set = sorted(symmetric_set)
for num in symmetric_set:
    print(num)
