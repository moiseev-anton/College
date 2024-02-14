"""
На вход программе подается строка текста.
Напишите программу, которая выводит на экран символ,
который появляется наиболее часто.
"""

s = input()
char_count = {}

for ch in s:
    char_count[ch] = char_count.get(ch, 0) + 1

max_char = max(char_count, key=char_count.get)
print(max_char)

