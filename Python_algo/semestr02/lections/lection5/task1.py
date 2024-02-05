# Найдите количество знаков препинания в строке
s = input("Введите строку: ")
marks = set(".,;:!?")

ans = sum(1 for ch in s if ch in marks)
print(ans)


# простой вариант
count = 0
for ch in s:
    if ch in marks:
        count += 1
print(count)
