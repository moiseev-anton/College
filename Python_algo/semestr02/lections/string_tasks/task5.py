# Задача 5

s = input("Введите строку: ")

result = s.replace('@', '')
print(result)

# без replace
result = ''.join(ch for ch in s if ch != '@')
print(result)
