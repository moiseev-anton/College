# 7. Написать программу, которая анализирует данные о 
# возрасте и относит человека к одной из четырех групп:
# дошкольник, ученик, работник, пенсионер. Возраст вводится с клавиатуры.

age = int(input("Введите возраст: "))

if age >= 0 and age <= 6:
    result = "дошкольник"
elif age >= 7 and age <= 18:
    result = "ученик"
elif age >= 19 and age <= 60:
    result = "работник"
else:
    result = "пенсионер"

print(f"Возрастная группа: {result}")