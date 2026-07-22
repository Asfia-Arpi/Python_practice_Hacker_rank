# HackerRank Problem: Find the Runner-Up Score!
# Topic: 02-Basic_data_types
# File Name: 02_FInd_the_runner_up.py

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    unique_scores = set(arr)
    sorted_scores = sorted(unique_scores)
    print(sorted_scores[-2])