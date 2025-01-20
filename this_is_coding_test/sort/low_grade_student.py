n = int(input())
students = []

for _ in range(n):
    name, grade = list(input().split())
    grade = int(grade)
    students.append((name, grade))
    
sorted_students = sorted(students, key=lambda x: x[1])

for student in sorted_students:
    print(student[0], end=' ')