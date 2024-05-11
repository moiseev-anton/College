"""
Дан список, заполненный произвольными целыми числами.
Найдите в этом списке два числа, произведение которых максимально.
Выведите эти числа в порядке не убывания."""

from random import randint

nums = [randint(-30, 30) for _ in range(10)]
print(*nums)

max1 = max2 = float('-inf')
min1 = min2 = float('inf')

for num in nums:
    if num < min1:
        min2 = min1
        min1 = num
    elif num < min2:
        min2 = num

    if num > max1:
        max2 = max1
        max1 = num
    elif num > max2:
        max2 = num

if max1 * max2 < min1 * min2:
    print(min(min1, min2), max(min1, min2))
else:
    print(min(max1, max2), max(max1, max2))
