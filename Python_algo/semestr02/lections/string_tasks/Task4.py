# Задача 4

s = input("Введите строку: ")

result = s.replace('1', 'one')
print(result)

# без replace
result = ''.join('one' if ch == '1' else ch for ch in s)
print(result)
