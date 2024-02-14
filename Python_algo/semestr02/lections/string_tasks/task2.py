# Задача 2
s = input("Введите строку: ").lower()

# first_h = s.find('h')
# last_h = s.rfind('h')

first_h = last_h = -1

for i in range(len(s)):
    if s[i] == 'h':
        first_h = i
        break

for i in range(len(s)-1, -1, -1):
    if s[i] == 'h':
        last_h = i
        break

if first_h == last_h:
    result = s
else:
    result = s[:first_h] + s[last_h + 1:]
print(result)

