# HackerRank Problem: Sets
# Topic: 03-Sets
# File Name: 01_introduction_to_sets.py

def average(array):
    distinct_height = set(array)
    avg = sum(distinct_height) /len(distinct_height)
    return round(avg, 3)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int,input().split()))
    result = average(arr)
    print(result)
