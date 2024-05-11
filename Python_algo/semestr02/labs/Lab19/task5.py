# Напишите программу, которая выводит список хорошистов и отличников в классе.

students = []

while True:
    prompt = input().strip()
    if prompt:
        name, grade = prompt.split()
        students.append((name, int(grade)))
    else:
        break

for name, grade in students:
    if grade > 3:
        print(name, grade)

