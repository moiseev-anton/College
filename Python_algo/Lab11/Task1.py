# Пусть задана последовательность чисел, оканчивающаяся нулём.
#  Необходимо найти минимальное число в этой последовательности.

num = int(input("n="))
max = num
while num != 0:
    num = int(input("n="))
    if num > max:
        max = num
print(f"max = {max}")
