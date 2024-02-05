# Задача 1
while True:
    s = input("Введите строку: ").strip()
    if len(s) >= 6: break
    print("Срока слишком короткая")

print(s[2])
print(s[-2])
print(s[:5])
print(s[:-2])
print(s[::2])
print(s[1::2])
print(s[::-1])
print(s[::-2])
print(len(s))
