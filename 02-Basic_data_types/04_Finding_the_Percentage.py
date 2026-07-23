# HackerRank Problem: Finding the Percentage
# Topic: 02-Basic_data_types
# File Name: 04_Finding_the_Percentage.py

if __name__ == '__main__':
    n = int(input())
    students_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        students_marks[name] = scores
    query_name = input()
    target_scores = students_marks[query_name]
    avg = sum(target_scores) / len(target_scores)
    print(f"{avg:.2f}")