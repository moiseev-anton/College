# Пусть задана последовательность чисел, оканчивающаяся нулём.
# Необходимо найти минимальное число в этой последовательности.

num = int(input("n="))
sum = num
while num != 0:
    num = int(input("n="))
    sum += num
print(f"sum = {sum}")