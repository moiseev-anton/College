# Даны два списка чисел, которые могут содержать до 10000 чисел каждый.
# Выведите все числа, которые входят как в первый, так и во второй список,
# в порядке возрастания.Вводятся два списка целых чисел.
# Все числа каждого списка находятся на отдельной строке.

# nums1 = "3 2 5 1 9 4 2 3"
# list1 = list(map(int, nums1.split()))
# nums2 = "9 5 17 5 11 12 1"
# list2 = list(map(int, nums2.split()))

list1 = list(map(int, input("Cписок 1\nВведите числа через пробел: ").split()))
list2 = list(map(int, input("Cписок 2\nВведите числа через пробел: ").split()))

set1 = set(list1)
set2 = set(list2)

result = sorted(set1.intersection(list2))
print(result)