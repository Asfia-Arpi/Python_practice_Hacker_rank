# HackerRank Problem: Nested Lists
# Topic: 02-Basic_data_types
# File Name: 03_Nested_list.py

if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])
    scores = sorted(list(set([student[1] for student in students])))
    second_lowest_score =scores[1]
    second_lowest_student = [student[0] for student in students if student[1] == second_lowest_score]
    for name in sorted(second_lowest_student):
        print(name)