# Задача 6

s = input("Введите строку: ")

first_h = s.find('h')
last_h = s.rfind('h')

result = (s[:first_h+1] +
          s[first_h+1: last_h].replace('h', 'H') +
          s[last_h:])
print(result)
