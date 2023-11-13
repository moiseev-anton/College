# Дан список, заполненный произвольными целыми числами. 
# Найдите в этом списке два числа, произведение которых максимально. 
# Выведите эти числа в порядке неубывания, сортировку использовать нельзя.

nums = list(map(int, input("Введите числа через пробел: ").split()))
max1 = max2 = float('-inf')
min1 = min2 = float('inf')

for n in nums:
    if n > max1:
        max2 = max1
        max1 = n
    elif n > max2:
        max2 = n
    if n < min1:
        min2 = min1
        min1 = n
    elif n < min2:
        min2 = n

if min1 * min2 > max1 * max2:
    print(min1, min2)
else:
    print(max2,max1)