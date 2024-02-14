"""
Введите статистику частотности букв а,н,е,ф  в кортеже.
Т.Е. пользователь вводит кортеж и нужно посчитать
количество указанных букв.
"""

user_input = tuple(input("Введите кортеж: "))

frequency = {key: 0 for key in 'анеф'}

for ch in user_input:
    if ch in frequency:
        frequency[ch] += 1

print(frequency)

