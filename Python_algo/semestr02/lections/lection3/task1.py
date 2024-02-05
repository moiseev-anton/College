from functools import reduce
# Посчитать сумму целых чисел, расположенных
# между числами 1 и N включительно

n = int(input("Введите n: "))
# по формуле
result = n * (n+1)/2
print(int(result))


# циклом
result = 0
for i in range(1, n+1):
    result += i
print(result)


# list comprehension
result = sum(i for i in range(1, n+1))
print(result)


# reduce()
result = reduce(lambda x, y: x + y, range(1, n+1))
print(result)
