# Входные данные
# В первой строке входного файла записаны числа N и M — количество
# кубиков у Ани и Бори соответственно. В следующих N строках заданы
# номера цветов кубиков Ани. В последних M строках номера цветов
# кубиков Бори.
# Выходные данные
# Выведите сначала количество, а затем отсортированные по
# возрастанию номера цветов таких, что кубики каждого цвета
# есть в обоих наборах, затем количество и отсортированные по
# возрастанию номера остальных цветов у Ани, потом количество
# и отсортированные по возрастанию номера остальных цветов у Бори.

n = int(input("Кубиков у Ани: "))
m = int(input("Кубиков у Бори: "))

anya_colors = set()
borya_colors = set()

print(f"Введите последовательно номера цветов для {n} кубиков Ани")
for _ in range(n):
    color = int(input())
    anya_colors.add(color)

print(f"Введите последовательно номера цветов для {n} кубиков Бори")
for _ in range(m):
    color = int(input())
    borya_colors.add(color)

common_colors = anya_colors & borya_colors

anya_colors -= common_colors
borya_colors -= common_colors

print("Результат:")
print(len(common_colors))
print(*sorted(common_colors))
print(len(anya_colors))
print(*sorted(anya_colors))
print(len(borya_colors))
print(*sorted(borya_colors))