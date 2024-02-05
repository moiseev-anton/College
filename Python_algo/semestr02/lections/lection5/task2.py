"""
Напишите программу, которая определяет правильность записи
целого числа в восьмеричной системе счисления.
"""

s = input("Введите строку: ")
octal_chars = set("01234567")
ans = "YES" if all(ch in octal_chars for ch in s) else "NO"
print(ans)

