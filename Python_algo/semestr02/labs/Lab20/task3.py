"""
Замените все символы строки на заглавные буквы, если длина строки больше 10,
 но меньше 20 символов. Если длина символов меньше 10 символов,  то на все строчные буквы.
Если длина строки больше 20 символов, то отформатируйте строку,
чтобы первая буква была заглавная. Используйте методы строк."""

s_list = [
    "КоРоТкая",
    "ДлИнНая До 20",
    "Длиная строка больше 20 символов"
]

for s in s_list:
    l = len(s)
    if l <= 10:
        res = s.lower()
    elif l >= 20:
        res = s.title()
    else:
        res = s.upper()
    print(res, '\n')

