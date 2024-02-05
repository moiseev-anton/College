# Найдите длину самой продолжительной последователности положительных чисел.
# Числа вводятся через пробел

nums = list(map(int, input("Введите числа через пробел: ").split()))
max_count = count = 0

for num in nums:
    count = count + 1 if num > 0 else 0
    max_count = max(max_count, count)

print(f"Результат: {max_count}")
