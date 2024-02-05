# Задача 2
s = input("Введите строку: ").lower()

# first_h = s.find('h')
# last_h = s.rfind('h')

first_h = last_h = -1

for i, ch in enumerate(s):
    if ch == 'h':
        first_h = i
        break

for i, ch in enumerate(s[::-1]):
    if ch == 'h':
        last_h = i
        break

last_h = len(s) - last_h - 1
if first_h == last_h:
    result = s
else:
    result = s[:first_h] + s[last_h + 1:]
print(result)

